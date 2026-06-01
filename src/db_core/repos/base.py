from abc import ABC, abstractmethod
from typing import List, Optional

# Abstract repository contracts used by service-layer business logic.

class BaseRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: str):
        ...

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List:
        ...

    @abstractmethod
    async def create(self, entity: dict) -> dict:
        ...

    @abstractmethod
    async def update(self, id: str, entity: dict) -> Optional[dict]:
        ...

    @abstractmethod
    async def delete(self, id: str) -> bool:
        ...


class CustomerEmailLookupRepository(BaseRepository, ABC):
    @abstractmethod
    async def get_by_email(self, email: str):
        ...
