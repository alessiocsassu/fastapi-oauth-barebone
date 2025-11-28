# 🧱 Barebone FastAPI OAuth2

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