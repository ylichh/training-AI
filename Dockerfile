FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml  ./
RUN poetry install --no-root

COPY . .

CMD ["python", "app/main.py"]
