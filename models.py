# create connection to the db
# create a session object for queries
# session object to be attached to the base class
import os
import psycopg2
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from utils import validate_empty_values

engine = create_engine(os.getenv('DATABASE_URL'),  convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

DeclarativeBase = declarative_base()
# attaching the session obj for querying
DeclarativeBase.query = db_session.query_property()


class Base(DeclarativeBase):
    '''
    common functionality available
    to each of my DB table classes
    '''
    __abstract__ = True  # skip the production of a table or mapper
    date_created = Column(DateTime, server_default=func.now())
    date_updated = Column(DateTime, server_default=func.now(),
                          onupdate=func.now())


class User(Base):
    """ User Model """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)

    def __init__(self, **kwargs):
        validate_empty_values(**kwargs)

        self.email = kwargs['email']
        self.username = kwargs['username']


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref(
        'news', uselist=True, cascade='delete,all'))


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
