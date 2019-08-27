from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import backref, relationship
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    data_posted = Column(DateTime, default=func.now())
    # owner_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User, backref=backref(
    #     'news', uselist=True, cascade='delete,all'))
