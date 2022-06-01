
# Development note

Please see note for detailed exaplanations:

https://cheerful-olivine-ef5.notion.site/Django-School-Management-System-DSMS-cf3cdecb4362416f91cbc2aa3ea4a3e4
# django-school-api-drf-nested-router
Sample usage of Django, Django Rest Framework, drf-nested-routers
DEUBG=True is intentionally left on, to disable change environmental variable ENV to anything other thatn staging
This is intended to be backend, all non matched routes are 404 by default
# Milestones
- [x]  Create Django App
- [x]  Use Postgres
- [x]  Use Pipenv
- [x]  Stores sensitive information in .env (and not committing them!)
- [x]  models: student, first_name, last_name, student identification id as UUID4() but only 20 chars
- [x]  models: school, name, max_student
- [x]  Use DRF
- [x]  Enable DRF API views
- [x]  use ModelViewSet
- [x]  use ModelSerializer
- [x]  endpoint /students/ GET, POST
- [x]  endpoint /schools/ GET, POST
- [x]  endpoint /students/:id PUT, PATCH, DELETE
- [x]  endpoint /schools/:id PUT, PATCH, DELETE
- [x]  Automatic UUID for student upon creation
- [x]  Disallow student to overflow school
- [x]  Use Django Nested Routers
- [x]  /schools/:id/students GET
- [x]  /schools/:id/students POST
- [x]  /schools/:id/students/:id GET, POST, PATCH, PUT, DELETE
- [x]  /students/ still works
# Deployments
## Heroku
https://django-school-api.herokuapp.com/api/v1/students/
## AWS ECS Fargate
http://18.141.202.26:8000/api/v1/students/
## docker-compose
Docker compose with quick tunnel to the internet for collaboration
cloudflare argo tunnels your applications to the internet through Cloludflare without exposing any ports
```

docker compose --env-file ./src/app/app/.env up --build --force-recreate

```
## pipenv with postgres in docker
```
cd postgres
docker compose up --build --force-recreate
cd src/app
conda activate <env>
pipenv run python manage.py runserver

```
Look for a url similar to https://savage-co**********cloudflare.com in logs
## Notice
AWS and Heroku deployments will be taken down by the end of June.
# Testings
## usage
Make sure to change BASE_URL according to which deployment you want to test
```
conda create --name pytest python=3.9.7
conda activate pytest
pip install -r requirements.txt
cd tests
pytest -vv test_*

```
# Bonus
1.  Notion development documentation
2.  Use deploy Postgres via docker with data persistence
3.  admin view for debugging/ quick edits
4.  Test driven design with pytest (with conda plus pip install -r requirements.txt)
5.  AWS Fargate serverless docker hosting
6.  Docker compose local deploy with automatic exposing to the internet through cloudflare Argi (suitable for short client demo, team demo)
7.  Heroku database setup (does this count as a bonus ?)
8.  gunicorn was used in AWS deployment

# Time logging
-   Preparing, reading some documentations, and thinking how to tackle this problem: about 1-2 days on, and off while driving, showering (best methods!)
-   Setting up the development environment: 15 minutes, I do thins everyday
-   Writing Django models up to working api routes 30 minutes, I do this everyday, too
-   Django Nested Routers: about 2 hours of trying to understand the sparse documentations and how data is passed, I have never used this before. I think of this as a challenge to see how I learn new techs.
-   Writing helper functions: less than 15 minutes
-   Pytest normal cases and requirements, catching bugs: about 1.5 - 2 hours
-   Pytest edge cases: 30 minutes
-   Heroku deplotment: 30 minutes
-   AWS deployment: 2 hours
-   Docker local deployment with tunnels to the internet: 30 minutes


# Caviets
Some config files are duplicated to root to make Heroku happy.
