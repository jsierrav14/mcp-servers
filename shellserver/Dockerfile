FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

# Copy the project (pyproject.toml's uv_build backend needs src/ present to build)
COPY . .

RUN uv sync --frozen --no-dev

# Make sure the venv's binaries are used
ENV PATH="/app/.venv/bin:$PATH"

# MCP talks over stdio, so this container is meant to be run with -i
# (e.g. `docker run -i shellserver`), not as a long-running network service.
ENTRYPOINT ["uv", "run", "server.py"]
