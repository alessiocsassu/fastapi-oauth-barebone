# Changelog
All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)**  
and this project adheres to **Semantic Versioning (SemVer)**.

---

## [1.0.1] - 2025-01-01

### Added Licence MIT

[1.0.1]: https://github.com/alessiocsassu/fastapi-oauth-barebone/releases/tag/v1.0.1

---

## [1.0.0] - 2025-01-01
### 🎉 Initial stable release

This is the first official release of the **FastAPI OAuth2 Barebone Template**, designed to provide a clean and scalable starter project for backend applications.

### 🚀 Added
- FastAPI application structure with modular architecture
- JWT-based authentication (access + refresh tokens)
- Base classes:
  - `BaseService` (generic CRUD)
  - `BaseManager` (business logic layer)
  - `BaseSchema` (shared schema)
  - `Base` SQLAlchemy model
- Users module (model, service, manager, routes)
- Asynchronous SQLAlchemy + PostgreSQL setup
- Alembic migrations ready out of the box
- Docker + Docker Compose (API + DB)
- Pydantic schemas with proper validation
- Settings/environment management with `.env`
- Pytest configuration for tests
- Template repository enabled
- Recommended folder structure for scalable APIs

### 📦 Included Tooling
- Poetry for dependency management
- Uvicorn ASGI server
- bcrypt for password hashing
- python-dotenv for environment management

---

[1.0.0]: https://github.com/alessiocsassu/fastapi-oauth-barebone/releases/tag/v1.0.0
