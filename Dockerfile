FROM python:3.7-alpine
MAINTAINER Wahyu

ENV INSTALL_PATH /web_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

#copy requirements.txt to workdir at container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "web_app.app:create_app()"
