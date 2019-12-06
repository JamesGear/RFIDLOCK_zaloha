FROM python:3.6.3

MAINTAINER Corey Burmeister "burmeister.corey@gmail.com"

RUN mkdir -p /var/www/flask-bones
WORKDIR /var/www/flask-bones

ADD requirements.txt /var/www/flask-bones/
RUN pip install -r requirements.txt --proxy http://192.168.1.1:800

ADD . /var/www/flask-bones
