import allure
import requests
from api_tests.utilities.url_sections import UrlSection
from api_tests.utilities.useful_func import get_base_url, get_api_version, get_headers_with_autorization

class PostsRequest:

    def __init__(self, post_data, url_post, user_id=None):
        self.post_data = post_data
        self.post_id = None
        self.url_post = url_post
        self.user_id = user_id

    @property
    def headers(self):
        return get_headers_with_autorization()

    @property
    def url_post_id(self):
        return f'{get_base_url()}{get_api_version()}{UrlSection.POSTS}/{self.post_id}'

    @allure.step('Send request Create new post')
    def create_new_post(self):
        response = requests.post(self.url_post, data=self.post_data, headers=self.headers)
        self.post_id = response.json()["id"]
        return response

    @allure.step('Send request Get user post')
    def get_users_posts(self):
        return requests.get(self.url_post, headers=self.headers)


