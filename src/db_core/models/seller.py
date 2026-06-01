from sqlalchemy import Float, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from db_core.models.base import Base

class SellerORM(Base):
    __tablename__ = "sellers"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    categories: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=False)
    portrait: Mapped[str] = mapped_column(Text, nullable=False)
    portfolio: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(64), nullable=False)
    instagram: Mapped[str | None] = mapped_column(String(255), nullable=True)
    distance_km: Mapped[float | None] = mapped_column(Float, nullable=True)
