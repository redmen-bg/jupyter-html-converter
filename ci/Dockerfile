FROM python:3.7-alpine

RUN apk add zip
RUN apk add gcc
RUN apk update && apk add build-base libzmq python3 python3-dev zeromq-dev
RUN ["ln", "-s", "/usr/lib/x86_64-linux-musl/libc.so", "/lib/libc.musl-x86_64.so.1"]

RUN python --version
