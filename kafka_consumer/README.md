# Kafka Consumer Wrapper

An async Kafka consumer wrapper built on top of `confluent_kafka.aio.AIOConsumer`.

## Overview

This module provides a clean, config-driven wrapper around the `AIOConsumer` from the
[confluent-kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
library. It accepts a structured `ConsumerConfig` object that maps to the underlying
confluent-kafka configuration dictionary, keeping consumer setup explicit and reusable.

## Structure

```
kafka_consumer/
├── __init__.py
├── __main__.py          # Demo entry point
├── README.md
└── consumer/
    ├── __init__.py
    ├── consumer_config.py   # ConsumerConfig dataclass
    └── kafka_consumer.py    # KafkaConsumer async wrapper
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

    consumer = KafkaConsumer(config)
    consumer.subscribe(["my-topic"])

    try:
        while True:
            messages = await consumer.consume(num_messages=10, timeout=1.0)
            for msg in messages:
                if msg.error():
                    print(f"Error: {msg.error()}")
                    continue
                print(f"key={msg.key()}, value={msg.value()}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

asyncio.run(main())
```

## ConsumerConfig

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `bootstrap_servers` | `str` | *required* | Comma-separated list of Kafka brokers |
| `group_id` | `str` | *required* | Consumer group identifier |
| `auto_offset_reset` | `str` | `"earliest"` | Offset reset policy (`"earliest"` or `"latest"`) |
| `enable_auto_commit` | `bool` | `True` | Automatically commit offsets |
| `session_timeout_ms` | `int` | `10000` | Session timeout in milliseconds |
| `max_poll_interval_ms` | `int` | `300000` | Maximum interval between polls |
| `extra` | `dict` | `None` | Additional raw confluent-kafka config keys |

## Installation

```bash
pip install confluent-kafka
```
