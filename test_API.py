import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_create_repository():
    repository = {
    "name":"Hello",
    "description":"Discription",
    "homepage":"https://github.com",
    "private":True,
    "is_template":True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": os.getenv("API_KEY")}
    resp = requests.post("https://api.github.com/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)

def test_delete_repository():
    owner = os.getenv("OWNER") 
    repo_name = os.getenv("REPO_NAME")
    headers = {"accept": "application/vnd.github+json", "authorization": os.getenv("API_KEY")}
    resp = requests.delete(f"https://api.github.com/repos/{owner}/{repo_name}",
                           headers=headers)
    print("\nRESPONSE BODY:", resp.text)

def test_create_repository_without_auth():
    repository = {
    "name":"Hello",
    "description":"Discription",
    "homepage":"https://github.com",
    "private":True,
    "is_template":True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": ""}
    resp = requests.post("https://api.github.com/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)

def test_create_repository_more_then100_sym():
    repository = {
    "name":"mpwyyfbtctlpjnfnvfnpzlypxedlmwcrkotnseurvtfdoujalmhiqejtwyqagtoozsjjrktjqjdorwjtvioafvmwzgnhhaqdzfrxmbefgjaljb",
    "description":"Discription",
    "homepage":"https://github.com",
    "private":True,
    "is_template":True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": ""}
    resp = requests.post("https://api.github.com/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)

def test_create_repository_without_name():
    repository = {
    "name":"",
    "description":"Discription",
    "homepage":"https://github.com",
    "private":True,
    "is_template":True
    }
    headers = {"accept": "application/vnd.github+json", "authorization": ""}
    resp = requests.post("https://api.github.com/user/repos",
                         json=repository, headers=headers)
    print("\nRESPONSE BODY:", resp.text)