import asyncio

from consumer import ConsumerConfig, KafkaConsumer


async def main():
    config = ConsumerConfig(
        bootstrap_servers="localhost:9092",
        group_id="demo-group",
        auto_offset_reset="earliest",
    )

    consumer = KafkaConsumer(config, topics=["demo-topic"])
    await consumer.start()

    try:
        while True:
            msg = await consumer.next_message()
            print(
                f"Received message: topic={msg.topic}, partition={msg.partition}, "
                f"offset={msg.offset}, key={msg.key}, value={msg.value}, "
                f"headers={msg.headers}, timestamp={msg.timestamp}"
            )
            await consumer.commit()
    except KeyboardInterrupt:
        pass
    finally:
        await consumer.close()


if __name__ == "__main__":
    asyncio.run(main())
