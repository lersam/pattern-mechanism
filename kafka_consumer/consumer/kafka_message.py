from dataclasses import dataclass
from typing import Optional


@dataclass
class KafkaMessage:
    topic: str
    value: Optional[bytes]
    headers: dict
    key: Optional[bytes]
    offset: int
    partition: int
    timestamp: Optional[int]
