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


class CreateUser(graphene.Mutation):
    '''
    Create user mutation
    '''

    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)

    # return values
    user = graphene.Field(UserObject)

    def mutate(self, info, **kwargs):
        with make_session_scope() as session:
            user = User(**kwargs)
            session.add(user)
            session.commit()
            return CreateUser(
                user=user
            )
