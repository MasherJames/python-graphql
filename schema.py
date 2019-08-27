import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from database import db_session
from models import News as NewsModel, User as UserModel


class News(SQLAlchemyObjectType):
    class Meta:
        model = NewsModel
        interfaces = (relay.Node, )


class NewsConnection(relay.Connection):
    class Meta:
        node = News


# class createNews(graphene.Mutation):
#     class Input:
#         title = graphene.String()
#         content = graphene.String()
#     ok = graphene.Boolean()
#     news = graphene.Field(News)

#     @classmethod
#     def mutate(cls, _, args, context, info):
#         news = NewsModel(title=args.get('title'), content=args.get('content'))
#         db_session.add(news)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_news = SQLAlchemyConnectionField(NewsConnection, sort=None)


schema = graphene.Schema(query=Query)
