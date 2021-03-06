FROM python:slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry

WORKDIR /ledger
COPY poetry.lock pyproject.toml /ledger/

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /ledger

CMD ["sh", "-c", "alembic upgrade head && poetry run start"]
