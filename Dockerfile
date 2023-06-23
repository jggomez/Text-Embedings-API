FROM python:3.10 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY poetry.lock pyproject.toml /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM python:3.10
WORKDIR /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY src/ /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
