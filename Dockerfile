FROM python:3.7.7-alpine3.11

WORKDIR /urs/src/app

COPY . .

RUN pip install 