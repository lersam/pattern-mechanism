from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsumerConfig:
    bootstrap_servers: str
    group_id: str
    auto_offset_reset: str = "earliest"
    enable_auto_commit: bool = True
    session_timeout_ms: int = 10000
    max_poll_interval_ms: int = 300000
    extra: Optional[dict] = field(default=None)

    def to_dict(self) -> dict:
        config = {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": self.auto_offset_reset,
            "enable.auto.commit": self.enable_auto_commit,
            "session.timeout.ms": self.session_timeout_ms,
            "max.poll.interval.ms": self.max_poll_interval_ms,
        }
        if self.extra:
            config.update(self.extra)
        return config
