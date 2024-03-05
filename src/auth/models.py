from dataclasses import dataclass, asdict, field
from typing import Optional


@dataclass
class LoginData:
    email: str
    password: str
    device_token: str


@dataclass
class AdminContent:
    _id: str
    _type: str
    email: str
    name: str
    groupId: str
    token: str


@dataclass
class User:
    _id: str
    attendances: Optional[str]
    begin: str
    codename: str
    created_at: str
    default_language: Optional[str]
    email: str
    enable_login_with_remote_auth: bool
    end: str
    history: str
    last_login: str
    logged_at: str
    msTeams: Optional[str]
    name: str
    password_callcenter: Optional[str]
    pause: Optional[str]
    photo: Optional[str]
    ramal: Optional[str]
    username_callcenter: Optional[str]
    teamsGtw: Optional[str]
    session_token: str
    status: str
    type: str
    updated_at: str
    campaigns: list = field(default_factory=list)
    campaigns_online: list = field(default_factory=list)
    groups: list = field(default_factory=list)


@dataclass
class UserContent:
    socket_token: str
    token: str
    user: User


@dataclass
class LogoutContent:
    message: str

