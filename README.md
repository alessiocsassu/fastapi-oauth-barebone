# 🧱 Barebone FastAPI OAuth2

## ⚙️ Tecnologie principali

| Componente | Tecnologia | Descrizione |
|-------------|-------------|--------------|
| **Linguaggio** | Python 3.12+ | Moderno, leggibile e con tipizzazione statica |
| **Framework API** | FastAPI | Framework asincrono per la creazione di API REST |
| **Server** | Uvicorn (ASGI) | Server leggero e performante per FastAPI |
| **Database** | PostgreSQL | Database relazionale robusto e scalabile |
| **ORM** | SQLAlchemy | Gestione delle entità e query tramite oggetti Python |
| **Migrazioni** | Alembic | Gestione versioning e rollback dello schema database |
| **Validazione dati** | Pydantic | Tipizzazione e validazione automatica di input/output |
| **Autenticazione** | JWT (JSON Web Token) | Gestione token di accesso e refresh |
| **Configurazione** | python-dotenv | Gestione variabili d’ambiente (.env) |

---

## 🧰 Tooling e DevOps

| Area | Strumento | Descrizione |
|------|------------|-------------|
| **Ambiente sviluppo** | Docker + Docker Compose | Contenitori per API e DB |
| **Testing** | Pytest | Test unitari e d’integrazione |
| **Migrazioni DB** | Alembic | Gestione versioning schema database |
| **Sicurezza** | JWT + bcrypt | Crittografia password e token-based authentication |
| **Gestione env** | .env / dotenv | Gestione configurazioni locali e segreti |

---

## 🗂️ Struttura

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

## Lista comandi per iniziare

1. Creazione e attivazione venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Selezionare la versione di python del venv
   
3. Installare e aggiornare poetry

```bash
pip install poetry
poetry install --no-root
```

4. Creare file .env

```bash
cp .env.example .env
```

5. Buildare con docker
```bash
docker compose up --build -d
```

6. Da dentro il container lanciare le migration con alembic
```bash
docker exec -it fastapi_app_container alembic revision --autogenerate -m "init schema"
docker exec -it fastapi_app_container alembic upgrade head
```

7. Verificare che tutto sia andato a buon fine con i test automatici (opzionale)
```bash
docker exec -it fastapi_test_container pytest tests/
```