# base image
FROM python:3.6-alpine

RUN mkdir -p /srv

# set working directory
WORKDIR /srv

# add requirements
COPY ./requirements.txt /srv/requirements.txt

# install requirements
RUN pip install --upgrade pip setuptools && \
    pip install --upgrade --requirement requirements.txt
