from tornado import gen
from traitlets import Dict
from jupyterhub.auth import Authenticator


class DictAuthenticator(Authenticator):

    passwords = Dict(
        {"a": "b"},
        config=True
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        if self.passwords.get(data['username']) == data['password']:
            return data['username']
