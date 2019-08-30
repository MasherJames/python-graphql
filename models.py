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

engine = create_engine(os.getenv('DATABASE_URL'),  convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# attaching the session obj for querying
Base.query = db_session.query_property()


class User(Base):
    """ User Model """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    data_posted = Column(DateTime, default=func.now())
    owner_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref(
        'news', uselist=True, cascade='delete,all'))


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
