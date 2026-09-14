import warnings

import pytest
import requests
from urllib3.exceptions import InsecureRequestWarning

from data.test_data import DEFAULT_PASSWORD
from helpers.api_helpers import register_user
from helpers.email_generator import generate_email

warnings.simplefilter("ignore", InsecureRequestWarning)


@pytest.fixture
def api_client():
    session = requests.Session()
    session.verify = False
    yield session
    session.close()


@pytest.fixture
def new_user(api_client):
    email = generate_email()
    password = DEFAULT_PASSWORD

    response, _, _ = register_user(api_client, email=email, password=password)
    response.raise_for_status()
    payload = response.json()

    return {
        "client": api_client,
        "email": email,
        "password": password,
        "token": payload["access_token"]["access_token"],
        "user": payload["user"],
    }


@pytest.fixture
def second_user(api_client):
    email = generate_email()
    password = DEFAULT_PASSWORD

    response, _, _ = register_user(api_client, email=email, password=password)
    response.raise_for_status()
    payload = response.json()

    return {
        "client": api_client,
        "email": email,
        "password": password,
        "token": payload["access_token"]["access_token"],
        "user": payload["user"],
    }
