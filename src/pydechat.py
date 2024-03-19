from httpx import Client


from .auth.auth import login, logout, refresh
from .auth.models import LoginData, LogoutContent

from .channels.channels import get_channels


class Session(Client):
    def __init__(self, host: str, email: str, password: str, device_token: str) -> None:
        Client.__init__(self, verify=False, base_url=host)

        self.user_data = login(self, LoginData(email, password, device_token))

        self.channels = get_channels(self)

    def atualizar(self) -> int:
        return refresh(self)

    def close(self) -> LogoutContent:
        return logout(self)
