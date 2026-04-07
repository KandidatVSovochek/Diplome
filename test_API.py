import requests
import os
from dotenv import load_dotenv

load_dotenv()


def test_create_repository(base_url):
    repository = {
        "name": "Hello",
        "description": "Discription",
        "homepage": "https://github.com",
        "private": True,
        "is_template": True
    }
    headers = {"accept": "application/vnd.github+json",
               "authorization": os.getenv("API_KEY")}
    resp = requests.post(f"{base_url}/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 201


def test_delete_repository(base_url):
    owner = os.getenv("OWNER")
    repo_name = os.getenv("REPO_NAME")
    headers = {"accept": "application/vnd.github+json",
               "authorization": os.getenv("API_KEY")}
    resp = requests.delete(f"{base_url}/repos/{owner}/{repo_name}",
                           headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 204


def test_create_repository_without_auth(base_url):
    repository = {
        "name": "Hello",
        "description": "Discription",
        "homepage": "https://github.com",
        "private": True,
        "is_template": True
    }
    headers = {"accept": "application/vnd.github+json",
               "authorization": ""}
    resp = requests.post(f"{base_url}/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 401


def test_create_repository_more_then100_sym(base_url):
    repository = {
        "name": ("mpwyyfbtctlpjnfnvfnpzlypxedlmwcrkotnseurvtfdoujal"
                 "mhiqejtwyqagtoozsjjrktjqjdorwjtvi"
                 "oafvmwzgnhhaqdzfrxmbefgjaljb"
                 ),
        "description": "Discription",
        "homepage": "https://github.com",
        "private": True,
        "is_template": True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": ""}
    resp = requests.post(f"{base_url}/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 422


def test_create_repository_without_name(base_url):
    repository = {
        "name": "",
        "description": "Discription",
        "homepage": "https://github.com",
        "private": True,
        "is_template": True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": ""}
    resp = requests.post(f"{base_url}/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 422
