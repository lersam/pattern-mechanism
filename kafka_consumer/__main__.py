import asyncio

from consumer import ConsumerConfig, KafkaConsumer


async def main():
    config = ConsumerConfig(
        bootstrap_servers="localhost:9092",
        group_id="demo-group",
        auto_offset_reset="earliest",
    )

    consumer = KafkaConsumer(config)
    consumer.subscribe(["demo-topic"])

    try:
        while True:
            messages = await consumer.consume(num_messages=10, timeout=1.0)
            for msg in messages:
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue
                print(f"Received message: key={msg.key()}, value={msg.value()}, "
                      f"topic={msg.topic()}, partition={msg.partition()}, "
                      f"offset={msg.offset()}")
    except KeyboardInterrupt:
        pass
    finally:
        await consumer.close()


if __name__ == "__main__":
    asyncio.run(main())
