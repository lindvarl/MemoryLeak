FROM python:3.7-slim

COPY . /srv/flask_app
WORKDIR /srv/flask_app

#RUN apt-get clean \
#    && apt-get -y update
#RUN apt-get -y install nginx \
#    && apt-get -y install python3-dev \
#    && apt-get -y install build-essential \
#    && apt-get install -y git \
#    && apt-get -y install swig \
#    && apt-get -y install wget \
#    && apt-get -y install cmake

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --src /usr/local/src
#RUN pip install -r requirements_private_repos.txt --src /usr/local/src


# Set the port number the container should expose
EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]