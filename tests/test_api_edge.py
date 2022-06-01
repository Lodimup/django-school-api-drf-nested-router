import requests
import random

# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://18.141.202.26:8000'
# BASE_URL = 'https://django-school-api.herokuapp.com'

def test_school_invalid_name_():
    # name too long
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': 'AAAAAAAAaaAAaaaaaaaaaAAAAAAAAaaAAaaaaaaaaaaaaa',
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 400

    # symbol in name
    payload = {
        'name': 'AAAAAAAAa@',
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 400


def test_space_in_name():
    # space in name is ok
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': 'AAAAA AAAa',
        'max_student': random.randint(1, 24)
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 201


def test_school_max_student_0():
    # 0 should be valid! The school is not open!
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': 'NotOpenYet',
        'max_student': 0
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 201


def test_school_invalid_max_student():
    # -1 should be valid! The school is not open!
    url = BASE_URL + '/api/v1/schools/'
    payload = {
        'name': 'DoesNotCompute',
        'max_student': -1
    }
    r = requests.post(url, json=payload)
    assert r.status_code == 400
