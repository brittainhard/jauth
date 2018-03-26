import os
import json
import requests

from tornado import gen
from jupyterhub.auth import Authenticator


class DBAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self, handler, data):
        dbauth_url = "http://" + os.environ.get("DBAUTH_SERVICE_HOST") + ":" + os.environ.get("DBAUTH_SERVICE_PORT") + "/users/"
        r = requests.get(dbauth_url, json={"username": data["username"], "password": data["password"]})
        user = json.loads(r.text)
        if user:
            return data['username']
        else:
            return None
