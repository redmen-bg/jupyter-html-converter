FROM python:3.7-alpine

RUN apk add zip
RUN apk add gcc

RUN apk update 

RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev zeromq
RUN pip install cython
RUN apk del .build-deps gcc musl-dev

RUN python --version
