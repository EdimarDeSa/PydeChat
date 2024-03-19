from os import environ

import pytest

from src.utilitarios.dot_env import load_env

from src.pydechat import Session
from src.auth.exceptions import FalhaDeLogin

class TestSession:
    session = None
    
    @classmethod
    def atualizar_sessao(cls, session):
        cls.session = session
    
    def test_login_mal_sucedido(self):
        load_env('./.env')

        URL_BASE = environ.get('URL_BASE')
        email = environ.get('EMAIL')
        password = "environ.get('PASSWORD')"
        device_token = environ.get('DEVICE_TOKEN')

        with pytest.raises(FalhaDeLogin) as exepinfo:
            Session(URL_BASE, email, password, device_token)
            
        assert exepinfo.value.args[0] == 'Falha ao realizar login'

    def test_login_bem_sucedido(self):
        URL_BASE = environ.get('URL_BASE')
        email = environ.get('EMAIL')
        password = environ.get('PASSWORD')
        device_token = environ.get('DEVICE_TOKEN')

        session = Session(URL_BASE, email, password, device_token)

        assert bool(session.headers['Authorization'])
        
        self.atualizar_sessao(session)
    
    def test_atualiza_token(self):
       resp = self.session.atualizar()
       
       assert resp == 200
    
    def test_buscar_contato(self):
        ...


    def test_logout_bem_sucedido(self):
        resp = self.session.close()
        
        assert resp.message == 'Usuário deslogado com sucesso'