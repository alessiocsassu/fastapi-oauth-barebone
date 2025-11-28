FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /
ENV PYTHONPATH=/

COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry add python-multipart passlib[bcrypt] python-jose[cryptography] && \
    poetry install --no-root --no-interaction --no-ansi && \
    pip install debugpy

COPY . .

EXPOSE 8000
EXPOSE 5678

CMD ["bash", "-c", "python -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --port 8000"]
