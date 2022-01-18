FROM python:3.10-alpine3.15
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt