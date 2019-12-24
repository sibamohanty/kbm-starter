FROM python:3.6.1-alpine

RUN apk update\
  && apk add \
     build-base \
    postgresql \
    postgresql-dev \
    libpq

RUN mkdir /usr/src/app

COPY ./setup.py /usr/src/app/setup.py

WORKDIR /usr/src/app

RUN pip install  --upgrade pip setuptools
COPY . /usr/src/app
RUN pip install -r requirements.txt
RUN pip install -e .

#RUN python initialize_db.py
#RUN initialize_kbm_db development.ini
#ENTRYPOINT [ "pserve" ]
###
