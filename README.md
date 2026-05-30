# seller_core (Reusable backend module)

This folder contains reusable backend logic separated from FastAPI route wiring and SQLAlchemy storage details.

## What is reusable here

- `models.py` → shared domain models (`Artist`, `Customer`)
- `repositories.py` → contracts/interfaces for repository behavior
- `services.py` → use-case logic (`create_customer_if_email_available`)

## Usage

1. install the distribution

   ```
   pip install "marketplacecore @ git+https://github.com/OliShah/MarketplaceCore.git@v0.1.0"
   ```

2. from the package.module:

   ```
   from seller_core.repository
   ```

3. import the class:

   ```
   import BaseRepository
   ```

# Workflows

## release

On every push to master, the `version` string is read from `pyproject.toml` and a new distribution will be released to the git with named `Release vX.X.X`

## checklist before each push

1. Update package version in pyproject.toml.

Stable example: 1.2.0
Pre-release example: 1.2.0rc1 or 1.2.0-dev.1

2. Commit:
   ```
   git add .
   git commit -m "Bump version to X.Y.Z"
   ```
3. Push to master

4. Confirm release on GitHub:
   - Tag should be v<version>.
   - Pre-release versions are auto-marked as pre-release.
   - Stable versions are marked latest.
