# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Builder stage: install dependencies in a venv
FROM base AS builder

# Install system dependencies required for pip packages (e.g., for pymongo, fastapi, strawberry)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /app/.venv

# Copy requirements file(s) if present, else fallback to inline install
# (Assume requirements.txt is not present, so install directly)
RUN --mount=type=cache,target=/root/.cache/pip \
    /app/.venv/bin/pip install --upgrade pip && \
    /app/.venv/bin/pip install fastapi strawberry-graphql[fastapi] pydantic pymongo

# Copy application code
COPY --link server.py ./

# Final stage: minimal image with non-root user
FROM base AS final

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code from builder
COPY --from=builder /app/server.py ./

# Set environment so venv is used
ENV PATH="/app/.venv/bin:server.py"

USER appuser

EXPOSE 8000

FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn
RUN pip install 'strawberry-graphql[debug-server]'


COPY server.py ./

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
