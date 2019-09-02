import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User, News

# Return type classes


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User


class NewsObject(SQLAlchemyObjectType):
    class Meta:
        model = News
