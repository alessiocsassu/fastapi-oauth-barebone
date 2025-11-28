# 🧱 Barebone FastAPI OAuth2

[![Use this template](https://img.shields.io/badge/GitHub-Use%20this%20template-success?style=for-the-badge&logo=github)](https://github.com/alessiocsassu/fastapi-oauth-barebone/generate)
[![Latest Release](https://img.shields.io/github/v/release/alessiocsassu/fastapi-oauth-barebone?style=for-the-badge&logo=github)](https://github.com/alessiocsassu/fastapi-oauth-barebone/releases)
[![License](https://img.shields.io/github/license/alessiocsassu/fastapi-oauth-barebone?style=for-the-badge)](./LICENSE)


## ⚙️ Key Technologies

| Component | Technology |
|-----------|-------------|
| **Language** | Python 3.12+ |
| **API Framework** | FastAPI |
| **Server** | Uvicorn (ASGI) |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Migrations** | Alembic |
| **Data Validation** | Pydantic |
| **Authentication** | JWT (JSON Web Token) |

---

## 🧰 Tooling & DevOps

| Area | Tool |
|-------|--------|
| **Development Environment** | Docker + Docker Compose |
| **Testing** | Pytest |
| **DB Migrations** | Alembic |
| **Security** | JWT + bcrypt |
| **Environment Management** | .env |

---

## 🗂️ Project Structure

```text
fastapi-oauth-base/
│
├── alembic
│   ├── versions
│   ├── env.py
│   └── script.py.mako
├── app
│   ├── api
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   │   └── __init__.py
│   ├── auth
│   │   ├── api
│   │   │   ├── routes
│   │   │   │   ├── __init__.py
│   │   │   │   └── auth.py
│   │   │   └── __init__.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   └── security.py
│   │   ├── managers
│   │   │   ├── __init__.py
│   │   │   └── auth_manager.py
│   │   ├── schemas
│   │   │   └── auth_schema.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   └── auth_service.py
│   │   └── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   └── session.py
│   ├── managers
│   │   ├── __init__.py
│   │   ├── base_manager.py
│   │   └── user_manager.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── user.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── base_service.py
│   │   └── user_service.py
│   ├── __init__.py
│   ├── main.py
│   └── pytest.ini
├── tests
│   ├── __pycache__
│   ├── __init__.py
│   └── test_users.py
├── CHANGELOG.md
├── Dockerfile
├── README.md
├── __init__.py
├── alembic.ini
├── docker-compose.yml
└── pyproject.toml
```
---

## 🚀 Setup Commands

1. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Select the Python version from the virtual environment (in your IDE)

3. Install and update poetry

```bash
pip install poetry
poetry install --no-root
```

4. Create the `.env` file

```bash
cp .env.example .env
```

5. Build and start services with docker
```bash
docker compose up --build -d
```

6. Run alembic migrations inside the container
```bash
docker exec -it fastapi_app_container alembic revision --autogenerate -m "init schema"
docker exec -it fastapi_app_container alembic upgrade head
```

7. Run automated tests (opzionale)
```bash
docker exec -it fastapi_test_container pytest tests/
```

---

## 📌 Guide on how to create Model, Schema, Service, Manager and Endpoints

This project uses a modular architecture based on reusable **base classes** (`BaseService`, `BaseManager`, `BaseSchema`, `Base`) designed to avoid repeating the same logic in every new module.

Thanks to these base classes, adding a new entity (e.g., `Product`, `Article`, `Category`, etc.) becomes fast and consistent.

Below is a step-by-step guide for anyone who clones this repository.

---

### 🧱 1. Create a New Model (SQLAlchemy)

All models inherit from the `Base` class:

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

To create a new model, add a file inside:

```bash
app/db/models/
```

Example: `Product` model

```python
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    code: Mapped[str]
```

After creating the model generate and apply migrations:

```bash
alembic revision --autogenerate -m "add product"
alembic upgrade head
```

### 📄 2. Create the Pydantic Schemas

Schemas define the request/response structure of your API.

Create a file inside:

```bash
app/schemas/product.py
```

Example:

```python
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    code: str

class ProductRead(BaseModel):
    id: int
    name: str
    code: str
```

### ⚙️ 3. Create the Service (CRUD Layer)

Services handle database operations only.
They inherit from BaseService, so you don’t need to rewrite CRUD logic.

Create:

```bash
app/services/product_service.py
```

Example:

```python
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.product import Product
from app.services.base_service import BaseService

class ProductService(BaseService[Product]):
    model = Product

    @staticmethod
    async def get_by_code(db: AsyncSession, code: str) -> Optional[Product]:
        result = await db.execute(
            select(Product).where(Product.code == code)
        )
        return result.scalar_one_or_none()
```

#### Why BaseService exists?

It provides generic methods such as:

- `get_list()`
- `get_by_id()`
- `create()`
- `update()`
- `delete()`

This keeps your code DRY and consistent across the project.

### 🧠 4. Create the Manager (Business Logic Layer)

Managers sit above Services and handle:

- validation
- error handling
- workflows
- business rules
- orchestration

Create:

```bash
app/managers/product_manager.py
```

Example:

```python
from app.managers.base_manager import BaseManager
from app.services.product_service import ProductService
from app.db.models.product import Product

class ProductManager(BaseManager[Product, ProductService]):
    service = ProductService
```

#### Why BaseManager exists?

It provides:

- `get_or_404()`
- `get_all()`
- `create()` with safe error handling
- `update()` with existence checks
- `delete()` returning a standardized `BaseDelete` schema

This ensures a consistent behavior across all endpoints.

### 🚀 5. Create Routes (API Endpoints)

Create a route file:

```bash
app/api/routes/product.py
```

Example:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.managers.product_manager import ProductManager
from app.schemas.product import ProductCreate, ProductRead
from app.db.session import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[ProductRead])
async def list_products(db: AsyncSession = Depends(get_db)):
    return await ProductManager.get_all(db)

@router.post("/", response_model=ProductRead)
async def create_product(
    payload: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    return await ProductManager.create(db, payload.model_dump())
```

Finally, register the router inside:

```bash
app/main.py
```
---
