import asyncio
import logging
from typing import List, Optional, Union

from confluent_kafka.aio import AIOConsumer

from .consumer_config import ConsumerConfig
from .kafka_message import KafkaMessage

logger = logging.getLogger(__name__)


class KafkaConsumer:
    def __init__(self, config: ConsumerConfig, topics: Union[str, List[str]]):
        raw_config = config.to_dict()
        # Always disable auto-commit — callers must use commit() explicitly
        raw_config["enable.auto.commit"] = False

        self._consumer = AIOConsumer(raw_config)
        self._topics: List[str] = [topics] if isinstance(topics, str) else list(topics)
        self._queue: asyncio.Queue[KafkaMessage] = asyncio.Queue()
        self._heartbeat_task: Optional[asyncio.Task] = None
        self._running = False

        self._consumer.subscribe(self._topics)

    async def start(self) -> None:
        """Start the background heartbeat loop."""
        self._running = True
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())

    async def _heartbeat_loop(self) -> None:
        """Poll continuously to keep the consumer alive and enqueue received messages."""
        while self._running:
            try:
                rcv_msg = await self._consumer.poll(timeout=1.0)
                if rcv_msg is None:
                    continue
                if rcv_msg.error():
                    logger.error("Consumer poll error: %s", rcv_msg.error())
                    continue

                msg = KafkaMessage(
                    topic=rcv_msg.topic(),
                    value=rcv_msg.value(),
                    headers=dict(rcv_msg.headers() or {}),
                    key=rcv_msg.key(),
                    offset=rcv_msg.offset(),
                    partition=rcv_msg.partition(),
                    # timestamp() returns (timestamp_type, timestamp_ms); index [1] is the ms value
                    timestamp=rcv_msg.timestamp()[1] if rcv_msg.timestamp() else None,
                )
                await self._queue.put(msg)
            except asyncio.CancelledError:
                break
            except Exception:
                logger.exception("Unexpected error in heartbeat loop")
                await asyncio.sleep(1.0)

    async def next_message(self) -> KafkaMessage:
        """Wait for and return the next available message."""
        return await self._queue.get()

    async def commit(self) -> None:
        """Manually commit the current offsets."""
        await self._consumer.commit(asynchronous=False)

    async def close(self) -> None:
        """Stop the heartbeat loop and close the underlying consumer."""
        self._running = False
        if self._heartbeat_task is not None:
            self._heartbeat_task.cancel()
            try:
                await self._heartbeat_task
            except asyncio.CancelledError:
                pass
        await self._consumer.close()

