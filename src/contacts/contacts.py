from httpx import Client

from .models import ContactsPage, asdict, NewContact


class StartEndException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def search_contact(session: Client, name=None, email=None, platform=None, platform_id=None, start_created_at=None, end_created_at=None) -> ContactsPage:
    URL_SEARCH_CONTACT = '/contacts/search'

    params = {}

    if name:
        params['name'] = name

    if email:
        params['email'] = email

    if platform:
        params['platform'] = platform

    if platform_id:
        params['platform_id'] = platform_id

    if start_created_at and end_created_at:
        params['start_created_at'] = start_created_at
        params['end_created_at'] = end_created_at
    elif not start_created_at and not end_created_at:
        pass
    else:
        raise StartEndException('Se for usar o campo start_created_at ou end_created_at, devem ser usados juntos!')

    resp = session.get(URL_SEARCH_CONTACT, params=params)

    return ContactsPage(**resp.json())


def create_contact(session: Client, contact: NewContact) -> str:
    URL_NEW_CONTACT = '/contacts/'

    resp = session.post(URL_NEW_CONTACT, params=asdict(contact))
    ...