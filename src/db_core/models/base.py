# Base is the registry + metadata for SQLAlchemy
# Every db model in the application should inherit from this base class
#SQLalchemy now knows: “These are all the tables in this application.”

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass