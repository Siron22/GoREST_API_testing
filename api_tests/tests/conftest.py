import json
import random
import allure
import pytest
from randomuser import RandomUser
from api_tests.source.posts_requests import PostsRequest
from api_tests.utilities.user import User
from api_tests.source.users_requests import UsersRequest
from api_tests.utilities.url_sections import UrlSection
from api_tests.utilities.useful_func import get_base_url, get_api_version, get_headers_with_autorization



@pytest.fixture()
def users_url():
    return f'{get_base_url()}{get_api_version()}{UrlSection.USERS}'


@pytest.fixture()
def headers():
    return get_headers_with_autorization()


@pytest.fixture()
def post_data():
    post_data = {
        "title": "Cumque voluptas ut dolor laboriosam praesentium temporibus dolores iste doloribus.",
        "body": "Aliquam est quis nostrum nostrum consequatur beatae.Illo et nihil. Quia sunt alias et et."
        }
    return json.dumps(post_data)


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
def user_with_static_data():
    data = User("Ayiane Sirko", "ayiane.sirko@example.com", "female", "active").get_json()
    return json.dumps(data)


@allure.story("Create new user with random data")
@pytest.fixture()
def new_random_user(user_with_random_data):
    request = UsersRequest(user_with_random_data)
    response = request.create_new_user()
    yield response
    request.delete_user()


@allure.story("Create new user with static data")
@pytest.fixture()
def new_user_static_data(user_with_static_data):
    request = UsersRequest(user_with_static_data)
    response = request.create_new_user()
    yield response
    request.delete_user()


@allure.story('Create new user and make a post')
@pytest.fixture()
def make_new_post(user_with_random_data, post_data):
    user = UsersRequest(user_with_random_data)
    user.create_new_user()
    url_post = user.url_post
    request = PostsRequest(post_data, url_post)
    response = request.create_new_post()
    yield response
    user.delete_user()
    
@allure.story('Create new user and make a post request')
@pytest.fixture()
def post_request(user_with_random_data, post_data):
    user = UsersRequest(user_with_random_data)
    user.create_new_user()
    url_post = user.url_post
    user_id = user.get_user_id()
    request = PostsRequest(post_data, url_post, user_id=user_id)
    yield request
    user.delete_user()
