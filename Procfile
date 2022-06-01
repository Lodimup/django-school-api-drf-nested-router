release: python src/app/manage.py migrate
web: gunicorn --chdir src/app/ app.wsgi
