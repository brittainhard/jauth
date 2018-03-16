from tornado import gen
from jupyterhub.auth import Authenticator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables import User


class DBAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self, handler, data):
        engine = create_engine('sqlite:///db/home/users.sqlite', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(username=data["username"]).first()
        session.close()
        if user:
            if data["password"] == user.password:
                return data['username']
        else:
            return None
