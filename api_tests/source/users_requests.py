import allure
import requests
from api_tests.utilities.url_sections import UrlSection
from api_tests.utilities.useful_func import get_base_url, get_api_version, get_headers_with_autorization


class UsersRequest:

    def __init__(self, user_data):
        self.user_data = user_data
        self.user_id = None

    @property
    def headers(self):
        return get_headers_with_autorization()

    @property
    def url(self):
        return f'{get_base_url()}{get_api_version()}{UrlSection.USERS}'

    @property
    def url_id(self):
        return f'{self.url}/{self.user_id}'

    @allure.step('Send requirement Create new user')
    def create_new_user(self):
        response = requests.post(self.url, data=self.user_data, headers=self.headers)
        self.user_id = response.json()['id']
        return response

    def get_user_id(self):
        return self.user_id

    @property
    def url_post(self):
        return f'{get_base_url()}{get_api_version()}{UrlSection.USERS}/{self.user_id}/{UrlSection.POSTS}'

    @allure.step('Send requirement Get user details')
    def get_users_details(self):
        return requests.get(self.url_id, headers=self.headers)

    @allure.step('Send requirement Update user details')
    def update_user_details(self, changed_data):
        return requests.put(self.url_id, changed_data, headers=self.headers)

    @allure.step('Send requirement Delete user')
    def delete_user(self):
        return requests.delete(self.url_id, headers=self.headers)



