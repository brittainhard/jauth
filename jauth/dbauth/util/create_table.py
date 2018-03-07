from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from jauth.dbauth.tables import *

engine = create_engine('sqlite:///users.sqlite', echo=True)

Base.metadata.create_all(engine)
