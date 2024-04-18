FROM python:3.12


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install poetry


WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev


COPY . /app/