#!/bin/bash

if [ ! -d "./alembic/versions" ]; then
  mkdir -p ./alembic/versions
fi

python3 -m venv .venv
source .venv/bin/activate

pip install poetry
poetry install --no-root

cp .env.example .env

docker-compose up --build -d

docker exec -it app alembic revision --autogenerate -m "init schema"
docker exec -it app alembic upgrade head

docker exec -it test pytest tests/