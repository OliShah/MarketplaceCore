# Defines schema for buyers table in the database using SQLAlchemy ORM.

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db_core.models.base import Base

class BuyerORM(Base):
    __tablename__ = "buyers"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)