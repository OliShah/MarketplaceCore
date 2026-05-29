import uuid
from typing import List, Optional

from pydantic import BaseModel, Field


class seller(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    city: str
    categories: List[str]
    bio: str
    portrait: str
    portfolio: List[str]
    email: str
    phone: str
    instagram: Optional[str] = None
    distance_km: Optional[float] = None


class buyer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    password: str
