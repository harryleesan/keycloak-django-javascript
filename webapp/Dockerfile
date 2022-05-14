# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./ca.crt /code/
RUN cat /code/ca.crt >> /usr/local/lib/python3.10/site-packages/certifi/cacert.pem

COPY . /code/
