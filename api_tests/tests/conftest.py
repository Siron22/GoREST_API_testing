import json
import random
import allure
import pytest
from randomuser import RandomUser
from api_tests.utilities.user import User
from api_tests.source.users_requests import UsersRequest
from api_tests.utilities.url_sections import UrlSection
from api_tests.utilities.useful_func import get_base_url, get_api_version, get_headers_with_autorization

# print(f'{get_base_url()}{get_api_version()}{UrlSection.USERS}')

@pytest.fixture()
def users_url():
    return f'{get_base_url()}{get_api_version()}{UrlSection.USERS}'

@pytest.fixture()
def headers():
    return get_headers_with_autorization()

@allure.step('Prepare user`s data')
@pytest.fixture()
def user_with_random_data():
    randomuser = RandomUser()
    name = randomuser.get_full_name()
    email = randomuser.get_email()
    gender = randomuser.get_gender()
    status = random.choice(['active', 'inactive'])
    data = User(name, email, gender, status).get_json()
    return json.dumps(data)

@pytest.fixture()
def user_with_manual_data():
    data = User("Awiane Sirko", "awiane.sirko@example.com", "female", "active").get_json()
    return json.dumps(data)

@pytest.fixture()
def new_random_user(user_with_random_data):
    request = UsersRequest(user_with_random_data)
    response = request.create_new_user()
    yield response
    request.delete_user()

@pytest.fixture()
def new_manual_user(user_with_manual_data):
    request = UsersRequest(user_with_manual_data)
    response = request.create_new_user()
    yield response
    request.delete_user()