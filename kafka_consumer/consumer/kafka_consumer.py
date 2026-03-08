from typing import Callable, List, Optional

from confluent_kafka.aio import AIOConsumer

from .consumer_config import ConsumerConfig


class KafkaConsumer:
    def __init__(self, config: ConsumerConfig):
        self._config = config
        self._consumer = AIOConsumer(config.to_dict())

    def subscribe(self, topics: List[str], on_assign: Optional[Callable] = None) -> None:
        self._consumer.subscribe(topics, on_assign=on_assign)

    async def consume(self, num_messages: int = 1, timeout: float = 1.0):
        return await self._consumer.consume(num_messages=num_messages, timeout=timeout)

    async def poll(self, timeout: float = 1.0):
        return await self._consumer.poll(timeout=timeout)

    async def commit(self, asynchronous: bool = True) -> None:
        await self._consumer.commit(asynchronous=asynchronous)

    def unsubscribe(self) -> None:
        self._consumer.unsubscribe()

    async def close(self) -> None:
        await self._consumer.close()

    @property
    def config(self) -> ConsumerConfig:
        return self._config
