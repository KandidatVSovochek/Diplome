import allure
import requests


@allure.title("Создание репозитория")
@allure.story("Создание репозитория на GitHub")
@allure.description("Создание репозитория на GitHub")
@allure.feature("API")
@allure.severity("critical")
def test_create_repository(base_url, headers, repo_name, make_body):
    with allure.step("Отправить post запрос на сервер"
                     "на создание репозитрия"):
        body = make_body(name=repo_name, private=True)
    resp = requests.post(f"{base_url}/user/repos",
                         json=body, headers=headers)
    response = resp.json()
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 201
    assert response["name"] == body["name"]


@allure.title("Удаление репозитория")
@allure.story("Удаление репозитория на GitHub")
@allure.description("удаление репозитория на GitHub, который был ранее создан")
@allure.feature("API")
@allure.severity("critical")
def test_delete_repository(base_url, headers, owner, repo_name):
    with allure.step("Отправить delete запрос на сервер"
                     "на удаление репозитрия"):
        resp = requests.delete(f"{base_url}/repos/{owner}/{repo_name}",
                               headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 204


@allure.title("Создание репозитория без авторизации")
@allure.story("Создание репозитория на GitHub")
@allure.description("Создание репозитория без авторизации")
@allure.feature("API")
@allure.severity("critical")
def test_create_repository_without_auth(base_url, repo_name, make_body):
    with allure.step("Отправить post запрос на сервер"
                     "на создание репозитрия без авторизации"):
        body = make_body(name=repo_name, private=True)
        headers = {"accept": "application/vnd.github+json",
                   "authorization": ""}
        resp = requests.post(f"{base_url}/user/repos",
                             json=body, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 401


@allure.title("Создание репозитория c названием > 100 символов")
@allure.story("Создание репозитория на GitHub")
@allure.description("Создание репозитория c названием > 100 символов")
@allure.feature("API")
@allure.severity("critical")
def test_create_repository_more_then100_sym(base_url, headers, make_body):
    with allure.step("Отправить post запрос на сервер"
                     "на создание репозитрия с названием > 100 символов"):
        body = make_body(name="mpwyyfbtctlpjnfnvfnpzlypxedlmwcr"
                         "kotnseurvtfdoujalmhiqejtwyqagtoozsjjrktjqjdorwjtvi"
                         "oafvmwzgnhhaqdzfrxmbefgjaljb", private=True)
        resp = requests.post(f"{base_url}/user/repos",
                             json=body, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 422


@allure.title("Создание репозитория без названия")
@allure.story("Создание репозитория на GitHub")
@allure.description("Создание репозитория без названия")
@allure.feature("API")
@allure.severity("critical")
def test_create_repository_without_name(base_url, headers, make_body):
    with allure.step("Отправить post запрос на сервер"
                     "на создание репозитрия без названия"):
        body = make_body(name="", private=True)
        resp = requests.post(f"{base_url}/user/repos",
                             json=body, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 422
