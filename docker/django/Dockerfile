FROM python:3.10.3

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND noninteractive

# 明示しておく
ENTRYPOINT ["/bin/bash", "-c"]

WORKDIR /test_django

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y curl gettext postgresql-client dos2unix

ADD . /test_django
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv lock --dev
RUN pipenv install --system --dev

# コンテナ軽量化
RUN rm -rf /var/lib/apt/lists/*

# CRLF対策
COPY docker/django/entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh
RUN chmod 777 /entrypoint.sh