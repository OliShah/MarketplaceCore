# artist_core (Reusable backend module)

This folder contains reusable backend logic separated from FastAPI route wiring and SQLAlchemy storage details.

## What is reusable here

- `models.py` → shared domain models (`Artist`, `Customer`)
- `repositories.py` → contracts/interfaces for repository behavior
- `services.py` → use-case logic (`create_customer_if_email_available`)
