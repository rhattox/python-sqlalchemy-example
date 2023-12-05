FROM python:3.10-bookworm

USER root

WORKDIR /home/python/src

COPY ./src ./

RUN pip install -r requirements.txt

