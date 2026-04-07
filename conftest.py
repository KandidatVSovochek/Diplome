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
def pull_req(registration):
    driver = registration
    driver.get("https://github.com/KandidatVSovochek/HW")
    driver.get("https://github.com/KandidatVSovochek/HW/pulls")
    yield driver

# базовый url для API


@pytest.fixture(scope="session")
def base_url():
    return "https://api.github.com"
