# Author: Henrique Malta
FROM python:3.10.12-slim-buster

# Metadata
LABEL maintainer="Henrique Malta <Silvinohenrique.Malta@merkle.com>"
LABEL version="0.0.1"
LABEL name="FastAPI app"

# FastAPI app
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080", "--log-level=debug"]