from seller_core.models import Customer
from seller_core.repositories import CustomerEmailLookupRepository


async def create_customer_if_email_available(
    payload: Customer,
    repo: CustomerEmailLookupRepository,
) -> Customer:
    existing = await repo.get_by_email(payload.email)
    if existing:
        raise ValueError("A customer with this email already exists.")

    created = await repo.create(payload.model_dump())
    return Customer(**created)
