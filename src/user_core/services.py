from user_core.models import buyer
from db_core.repos.base import CustomerEmailLookupRepository


async def create_customer_if_email_available(
    payload: buyer,
    repo: CustomerEmailLookupRepository,
) -> buyer:
    exists = await repo.get_by_email(payload.email)
    if exists:
        raise ValueError("A customer with this email already exists.")

    created = await repo.create(payload.model_dump())
    return buyer(**created)
