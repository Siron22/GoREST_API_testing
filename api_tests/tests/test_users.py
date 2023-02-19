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

    for item in response.values():
        if type(item) != int:
            assert user_with_random_data.find(item)

@allure.story('New user created with manual input data')
def test_create_new_user(new_manual_user, user_with_manual_data):
    response = new_manual_user.json()
    print(response)
    assert new_manual_user.status_code == 201
    assert response["name"] == "Awiane Sirko"

