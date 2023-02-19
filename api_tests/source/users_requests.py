import requests
from api_tests.utilities.url_sections import UrlSection
from api_tests.utilities.useful_func import get_base_url, get_api_version, get_headers_with_autorization


class UsersRequest:

    def __init__(self, user_data):
        self.user_data = user_data

    @property
    def headers(self):
        return get_headers_with_autorization()

    @property
    def url(self):
        return f'{get_base_url()}{get_api_version()}{UrlSection.USERS}'

    @property
    def url_id(self):
        return f'{self.url}{self.create_new_user().json()[0]}'

    def create_new_user(self):
        return requests.post(self.url, data=self.user_data, headers=self.headers)

    def get_users_details(self):
        return requests.get(self.url_id, headers=self.headers)

    def update_user_details(self, changed_data):
        return requests.put(self.url_id, changed_data, headers=self.headers)

    def delete_user(self):
        return requests.delete(self.url_id, headers=self.headers)

r = requests.get(f"{get_base_url()}/public/v2/users/478203", headers=get_headers_with_autorization())
# r = requests.delete(f"{get_base_url()}/public/v2/users/478203", headers=get_headers_with_autorization())
print(r.json())