FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    bash curl \
    && rm -rf /var/lib/apt/lists/*
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache uv sync --frozen --no-install-project

COPY README.md ./
COPY server.py ./

RUN --mount=type=cache,target=/root/.cache uv sync --frozen

RUN useradd -m -u 1000 mcpuser && chown -R mcpuser:mcpuser /app
USER mcpuser

CMD ["uv", "run", "python", "server.py"]
