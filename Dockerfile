FROM python:3.8.12

ENV PYTHONUNBUFFERED 1

RUN apt-get -u update
RUN apt-get -y install vim

COPY . /django/app
WORKDIR /django/app

#RUN mkdir /srv/docker-server
#ADD . /srv/docker-server

#WORKDIR /srv/docker-server


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
