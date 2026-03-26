FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH = "/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

RUN pip install pandas pyarrow

COPY pipeline.py .

ENTRYPOINT ["python","pipeline.py"]


# PowerShell one-off command to run Postgres (keeps working even if you rerun it):
# - does not use a named volume (fresh init every run)
# - sets `POSTGRES_HOST_AUTH_METHOD=trust` so host connections don't require a password
# - PowerShell line continuation uses ` (backtick), not `\`.
# docker run -it --rm `
#   -e POSTGRES_USER="root" `
#   -e POSTGRES_PASSWORD="root" `
#   -e POSTGRES_DB="ny_taxi" `
#   -e POSTGRES_HOST_AUTH_METHOD="trust" `
#   # no named volume: forces a fresh init every run (avoids "old password" issues)
#   -p 5433:5432 `
#   postgres:18


######good postgreinitiation (PowerShell)
docker run -it --rm `
  -e POSTGRES_USER="root" `
  -e POSTGRES_PASSWORD="root" `
  -e POSTGRES_DB="ny_taxi" `
  -e POSTGRES_HOST_AUTH_METHOD="trust" `
  -p 5433:5432 `
  postgres:18

#uv run pgcli -h localhost -p 5433 -u root -d ny_taxi