FROM python:3.9.7-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install psycopg2
WORKDIR /src
COPY requirements.txt /src
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /src
