import allure
import requests


@allure.title('Test for user list')
def test_get_users_list(users_url, headers):
    response = requests.get(users_url, headers=headers)
    assert response.status_code == 200


@allure.story('New random user created')
def test_create_new_user(user_with_random_data, new_random_user):
    response = new_random_user.json()
    assert new_random_user.status_code == 201
    with allure.step("Verify that all users field return in response"):
        for item in response.values():
            if type(item) != int:
                assert user_with_random_data.find(item)

@allure.story('New user created with manual input data')
def test_create_new_user(new_user_static_data, user_with_static_data):
    response = new_user_static_data.json()
    print(response)
    assert new_user_static_data.status_code == 201
    assert response["name"] == "Ayiane Sirko"

