import os
import json
import requests

from tornado import gen
from jupyterhub.auth import Authenticator


class DBAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self, handler, data):
        dbauth_url = "http://" + os.environ.get("DBAUTH_SERVICE_HOST") + ":" + os.environ.get("DBAUTH_SERVICE_PORT") + "/users"
        r = requests.get(dbauth_url, json={"username": data["username"]})
        user = json.loads(r.text)
        if user:
            if data["password"] == user[0]["password"]
                return data['username']
        else:
            return None
