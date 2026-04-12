import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()


# запуск chrome
@pytest.fixture(scope="session")
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


# регистрация
@pytest.fixture(scope="session")
def registration(driver):
    driver.get("https://github.com/login")
    driver.find_element(By.NAME, "login").send_keys(os.getenv("OWNER"))
    driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.NAME, "commit").click()
    yield driver


# раздел с pull requests
@pytest.fixture(scope="session")
def pull_req(registration, owner):
    driver = registration
    driver.get(f"https://github.com/{owner}/HW")
    driver.get(f"https://github.com/{owner}/HW/pulls")
    yield driver


# базовый url для API
@pytest.fixture(scope="session")
def base_url():
    return "https://api.github.com"


# owner
@pytest.fixture(scope="session")
def owner():
    owner = os.getenv("OWNER")
    return owner


# repo_name
@pytest.fixture(scope="session")
def repo_name():
    repo_name = os.getenv("REPO_NAME")
    return repo_name


# headers
@pytest.fixture(scope="session")
def headers():
    token = os.getenv("API_KEY")
    headers = {"accept": "application/vnd.github+json",
               "authorization": f"Bearer {token}"}
    return headers


# тело JSON конструктор
@pytest.fixture(scope="session")
def make_body():
    def make(name="Default", description="Description", private=True):
        return {
            "name": name,
            "description": description,
            "homepage": "https://github.com",
            "private": private,
            "is_template": True
        }
    return make
