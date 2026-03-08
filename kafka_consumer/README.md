# Kafka Consumer Wrapper

An async Kafka consumer wrapper built on top of `confluent_kafka.aio.AIOConsumer`.

## Overview

This module provides a clean, config-driven wrapper around the `AIOConsumer` from the
[confluent-kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
library. It accepts a structured `ConsumerConfig` object, subscribes to topics on
construction, runs a background heartbeat loop to prevent the consumer from leaving
the group, and exposes `next_message()` / `commit()` for a clean manual-commit workflow.

## Structure

```
kafka_consumer/
├── __init__.py
├── __main__.py              # Demo entry point
├── README.md
└── consumer/
    ├── __init__.py
    ├── consumer_config.py   # ConsumerConfig dataclass
    ├── kafka_consumer.py    # KafkaConsumer async wrapper
    └── kafka_message.py     # KafkaMessage dataclass
```

## Usage

```python
import asyncio
from consumer import ConsumerConfig, KafkaConsumer

async def main():
    config = ConsumerConfig(
        bootstrap_servers="localhost:9092",
        group_id="my-group",
        auto_offset_reset="earliest",
    )

    # topics can be a string or a list of strings
    consumer = KafkaConsumer(config, topics=["my-topic"])
    await consumer.start()   # starts the background heartbeat loop

    try:
        while True:
            msg = await consumer.next_message()
            print(f"topic={msg.topic} offset={msg.offset} value={msg.value}")
            await consumer.commit()   # manual commit after processing
    except KeyboardInterrupt:
        pass
    finally:
        await consumer.close()

asyncio.run(main())
```

## ConsumerConfig

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `bootstrap_servers` | `str` | *required* | Comma-separated list of Kafka brokers |
| `group_id` | `str` | *required* | Consumer group identifier |
| `auto_offset_reset` | `str` | `"earliest"` | Offset reset policy (`"earliest"` or `"latest"`) |
| `session_timeout_ms` | `int` | `10000` | Session timeout in milliseconds |
| `max_poll_interval_ms` | `int` | `300000` | Maximum interval between polls |
| `extra` | `dict` | `None` | Additional raw confluent-kafka config keys |

> **Note:** `enable.auto.commit` is always set to `False` by the wrapper —
> callers are expected to call `commit()` explicitly after processing each message.

## KafkaMessage

| Field | Type | Description |
|-------|------|-------------|
| `topic` | `str` | Source topic name |
| `value` | `bytes \| None` | Message payload |
| `headers` | `dict` | Message headers |
| `key` | `bytes \| None` | Message key |
| `offset` | `int` | Partition offset |
| `partition` | `int` | Partition number |
| `timestamp` | `int \| None` | Message timestamp (ms) |

## KafkaConsumer API

| Method | Description |
|--------|-------------|
| `__init__(config, topics)` | Creates and subscribes the consumer. `topics` can be `str` or `List[str]` |
| `start()` | Starts the background heartbeat/poll loop |
| `next_message()` | Awaitable — returns the next `KafkaMessage` |
| `commit()` | Manually commits the current offsets |
| `close()` | Stops the heartbeat loop and closes the consumer |

## Installation

```bash
pip install confluent-kafka
```
