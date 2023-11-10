FROM python:3-slim-buster

ENV PYTHONUNBUFFERD=1
RUN mkdir /src
WORKDIR /src


COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY ./src /src 




