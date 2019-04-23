FROM python:3.7-alpine

RUN apk add zip
RUN apk add gcc
RUN apk update && apk add build-base libzmq musl-dev python3 python3-dev zeromq-dev
RUN python --version