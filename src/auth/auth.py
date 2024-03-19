from httpx import Client, Response

from .models import LoginData, LogoutContent, UserContent, AdminContent, asdict
from .exceptions import FalhaDeLogin

URL_LOGIN = '/auth/login'
URL_LOGOUT = '/auth/logout'
URL_ME = '/auth/me'
URL_REFRESH = '/auth/refresh'


def update_token(session: Client, token: str) -> None:
    session.headers.update({'Authorization': f'Bearer {token}'})


def login(session: Client, login_data: LoginData) -> UserContent:
    data = asdict(login_data)

    resp: Response = session.post(URL_LOGIN, data=data)
    
    if resp.status_code != 200:
        raise FalhaDeLogin('Falha ao realizar login')

    content = resp.json()

    if content['user']['type'] == 'admin':
        user_data = AdminContent(**content)
    else:
        user_data = UserContent(**content)

    update_token(session, user_data.token)

    return user_data


def logout(session: Client) -> LogoutContent:
    resp = session.get(URL_LOGOUT)

    if resp.status_code != 200:
        raise Exception(resp.content)

    return LogoutContent(**resp.json())


def me(session: Client) -> UserContent:
    resp = session.get(URL_ME)

    if resp.status_code != 200:
        raise Exception(resp.content)
    
    return UserContent(**resp.json())


def refresh(session: Client) -> int:
    resp = session.get(URL_REFRESH)

    token = resp.json()['token']

    update_token(session, token)

    return resp.status_code