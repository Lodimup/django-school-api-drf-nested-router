FROM python:3.9.7-alpine
EXPOSE 8000
RUN apk update && apk add bash postgresql-dev gcc python3-dev musl-dev
RUN pip3 install psycopg2
WORKDIR /src
COPY requirements.txt /src
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /src
CMD  sh -c "gunicorn --chdir app app.wsgi --workers 4 -b 0.0.0.0:8000 --timeout 120 --log-level=debug"
