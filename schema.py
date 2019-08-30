import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, News as NewsModel, User as UserModel
from mutations import CreateUser


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode


class NewsNode(SQLAlchemyObjectType):
    class Meta:
        model = NewsModel
        interfaces = (relay.Node, )


class NewsConnection(relay.Connection):
    class Meta:
        node = NewsNode


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserConnection)
    all_news = SQLAlchemyConnectionField(NewsConnection)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
