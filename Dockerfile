FROM python:3

ADD . /code

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt
#COPY crontab /etc/cron.d/crontab


CMD [ "python", "main.py"]
