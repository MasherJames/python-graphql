# create connection to the db
# create a session object for queries
# session object to be attached to the base class
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv('DATABASE_URL'),  convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# attaching the session obj for querying
Base.query = db_session.query_property()
