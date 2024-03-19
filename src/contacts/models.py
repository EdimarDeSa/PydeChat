from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Platform:
    platform: str
    platform_id: str


@dataclass
class Contact:
    _id: Optional[str]
    name: str
    ddi: str
    email: Optional[str]
    final_number: str
    number: str
    statusWhatsapp: int
    updated_at: str
    created_at: str
    photo: str
    lastChannel: str
    group_: list[str] = field(default_factory=list, alias='group')
    platforms: list[Platform] = field(default_factory=list)


@dataclass
class Channels:
    Whatsapp: Optional[str]
    Telegram: Optional[str]
    Messenger: Optional[str]
    ChatWeb: Optional[str]
    Email: Optional[str]
    WhatsappBusiness: Optional[str]


@dataclass
class NewContact:
    name: str
    email: str
    groups: list[str] = field(default_factory=list)
    ddi: str
    final_number: str
    channels: Channels

@dataclass
class ContactsPage:
    current_page: int
    first_page_url: str
    last_page: int
    last_page_url: str
    next_page_url: str
    path: str
    per_page: int
    prev_page_url: str
    to: int
    total: int
    from_: int = field(alias='from')
    data: list[Contact] = field(default_factory=list)
