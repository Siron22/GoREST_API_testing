import allure

"""Можно каждый ассерт вынести в отдельный тест. Будет ли от этого смысл?"""



@allure.title('Test for create new post')
def test_make_new_post(make_new_post, post_data):
    response_body = make_new_post.json()
    post_dict = eval(post_data)
    assert make_new_post.status_code == 201
    for item in response_body.values():
        if type(item) != int:
            assert post_data.find(item)
    assert post_dict["title"] == response_body["title"]
    assert post_dict["body"] == response_body["body"]


@allure.title('Test for create new post')
def test_make_new_post(post_request, post_data):
    """Тут я решил поиграться с другой фикстурой которая возвращает
    сам запрос, а не ответ от созданного поста. Это позволило проверить
    id пользователя и поста"""
    response = post_request.create_new_post()
    response_body = response.json()
    post_dict = eval(post_data)
    with allure.step('User id is correct'):
        assert post_request.user_id == response_body["user_id"]
    with allure.step('Post id is correct'):
        assert post_request.post_id == response_body["id"]
    with allure.step('Title is correct'):
        assert post_dict["title"] == response_body["title"]
    with allure.step('Body id is correct'):
        assert post_dict["body"] == response_body["body"]




