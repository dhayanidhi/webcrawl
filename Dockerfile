FROM python:3.7

ENV LANG C.UTF-8

RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    build-essential \
    python3-dev

COPY requirements.txt /srv/requirements.txt

WORKDIR /srv

RUN pip3 install -r requirements.txt

COPY webscrap /srv/webscrap
COPY scrapy.cfg /srv/scrapy.cfg
COPY execute.sh /srv/execute.sh

ENV PYTHONPATH $PYTHONPATH:/srv

# start our service
CMD ["bash", "./execute.sh"]