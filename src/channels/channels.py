from httpx import Client

from .models import RegisteredChannels

URL_REGISTER = '/channels'


def get_channels(session: Client):
    resp = session.get(URL_REGISTER)
    return RegisteredChannels(resp.json())