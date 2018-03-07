from tornado import gen
from jupyterhub.auth import Authenticator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class DBAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self, handler, data):
        engine = create_engine('sqlite:///users.sqlite', echo=True)
        session = sessionmaker(engine)
        username = data["username"]
        user = session.query(User).filter(username=username).first()
        if user:
            if data["password"] == user.password
                return data['username']
        else:
            return None
