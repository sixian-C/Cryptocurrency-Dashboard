FROM python:3


#RUN apt-get update
#RUN apt-get install vim
#
#RUN apt-get update && \
#    apt-get install -y openjdk-8-jdk && \
#    apt-get install -y ant && \
#    apt-get clean;
#
## Fix certificate issues
#RUN apt-get update && \
#    apt-get install ca-certificates-java && \
#    apt-get clean && \
#    update-ca-certificates -f;
#
## Setup JAVA_HOME -- useful for docker commandline
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
#
#RUN export JAVA_HOME

ADD . /code

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt
#COPY crontab /etc/cron.d/crontab


CMD [ "python", "main.py"]
