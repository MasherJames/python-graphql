import graphene
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from models import db_session, User
from objects import UserObject, NewsObject


@contextmanager
def make_session_scope(Session=db_session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    session.expire_on_commit = False

    try:
        yield session
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


# class UserInput(graphene.InputObjectType):
#     """Arguments to create a user."""
#     username = graphene.String()
#     email = graphene.String()

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    email = graphene.String()
    username = graphene.String()
    # User fileds

    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)

    # return values
    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, email, username):
        with make_session_scope() as session:
            user = User(email=email, username=username)
            session.add(user)
            session.commit()
            return CreateUser(
                user=user
            )
