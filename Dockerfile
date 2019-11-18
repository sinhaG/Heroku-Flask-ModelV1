FROM ubuntu:18.04

MAINTAINER Your Name "gaurav@atrium.ai"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]