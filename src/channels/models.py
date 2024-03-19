from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Channel:
    _id: str
    platform: str
    flow_id: str
    receptive: bool
    description: str
    updated_at: str
    created_at: str
    status: str
    number: Optional[str]
    provider: Optional[str]
    bot_token: Optional[str]

@dataclass
class RegisteredChannels:
    channels: list[Channel] = field(default_factory=list)
