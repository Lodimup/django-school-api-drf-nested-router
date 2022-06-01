import requests
from faker import Faker
import random

fake = Faker()
# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://18.141.202.26:8000'
# BASE_URL = 'https://django-school-api.herokuapp.com'

def test_server_isonline():
    url = BASE_URL + '/admin'
    assert requests.get(url).status_code == 200


def test_schools_get():
    url = BASE_URL + '/api/v1/schools/'
    r = requests.get(url)
    assert r.status_code == 200


def test_schools_post():
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 201


def test_schools_put():
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.put(url, json=payload)
    assert r.status_code == 200


def test_schools_patch():
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/'
    payload = {
        'max_student': random.randint(1, 24)
    }
    r = requests.patch(url, json=payload)
    assert r.status_code == 200
    school_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/'
    payload = {
        'max_student': random.randint(1, 24)
    }
    r = requests.patch(url, json=payload)
    assert r.status_code == 200


def test_students_get():
    url = BASE_URL + '/api/v1/students/'
    r = requests.get(url)
    assert r.status_code == 200


def test_students_post():
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + '/api/v1/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 201


def test_school_student_get():
    """
    test get on /schools/:id/students/
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    r = requests.get(url)
    assert r.status_code == 200


def test_school_student_post():
    """
    test create on /schools/:id/students/
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 201


def test_school_student_delete():
    """
    test delete on /schools/:id/students/:id
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/{student_id}'
    r = requests.delete(url)
    assert r.status_code == 204


def test_school_student_put():
    """
    Disallow test when the school is full on create on /schools/:id/students/
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/{student_id}/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.put(url, json=payload)
    assert r.status_code == 200


def test_school_student_patch():
    """
    Disallow test when the school is full on create on /schools/:id/students/
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/{student_id}/'
    payload = {
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.patch(url, json=payload)
    assert r.status_code == 200
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/{student_id}/'
    payload = {
        'first_name': fake.first_name()[:20],
        'school': school_id,
    }
    r = requests.patch(url, json=payload)
    assert r.status_code == 200
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/{student_id}/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
    }
    r = requests.patch(url, json=payload)
    assert r.status_code == 200


def test_school_student_post_school_full():
    """
    Disallow test when the school is full on create on /schools/:id/students/
    """
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': 1
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']

    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 400

def test_school_student_put_school_full():
    """
    Disallow test when the school is full on create on /schools/:id/students/
    """
    # create school 1 with full student
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': 1
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']
    # assign the student to the school
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']

    # create school 2 with one student then move the student to shool 1
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': 1
    }
    r = requests.post(url, json=payload)
    school_id_2 = r.json()['id']

    # assign the student to the school
    url = BASE_URL + f'/api/v1/schools/{school_id_2}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id_2,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']

    # move the student to the 1 st school
    url = BASE_URL + f'/api/v1/schools/{school_id_2}/students/{student_id}/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.put(url, json=payload)

    assert r.status_code == 400

def test_school_student_patch_school_full():
    """
    Disallow test when the school is full on create on /schools/:id/students/
    """
    # create school 1 with full student
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': 1
    }
    r = requests.post(url, json=payload)
    school_id = r.json()['id']
    # assign the student to the school
    url = BASE_URL + f'/api/v1/schools/{school_id}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']

    # create school 2 with one student then move the student to shool 1
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': fake.company()[:20],
        'max_student': 1
    }
    r = requests.post(url, json=payload)
    school_id_2 = r.json()['id']

    # assign the student to the school
    url = BASE_URL + f'/api/v1/schools/{school_id_2}/students/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id_2,
    }
    r = requests.post(url, json=payload)
    student_id = r.json()['id']

    # move the student to the 1 st school
    url = BASE_URL + f'/api/v1/schools/{school_id_2}/students/{student_id}/'
    payload = {
        'first_name': fake.first_name()[:20],
        'last_name': fake.last_name()[:20],
        'school': school_id,
    }
    r = requests.put(url, json=payload)

    assert r.status_code == 400
