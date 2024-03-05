import time
from httpx import Client

from auth.auth import login, logout, me, refresh
from auth.models import LoginData, LogoutContent


class Session(Client):
    def __init__(self, host: str, email: str, password: str, device_token: str) -> None:
        Client.__init__(self, verify=False, base_url=host)

        self.user_data = login(self, LoginData(email, password, device_token))

    def atualizar(self) -> int:
        return refresh(self)

    def close(self) -> LogoutContent:
        return logout(self)


if __name__ == "__main__":    
    URL_BASE = 'https://itec_demo.widechat.com.br/api/v4'
    email='comunicacaocoen@gmail.com'
    password='G$Qjuaon3T*xnAs7DWYL3Y#fBLFDGz'
    device_token='cdf13bef224dbf4e88aff62548b4a272'
    
    session = Session(URL_BASE, email, password, device_token)
    
    time.sleep(2)

    resp = session.atualizar()
    
    time.sleep(2)

    resp = session.close()
    print(resp)
    