from UI.repo_page import RepoPage
from UI.pull_page import Pull_req
from selenium.webdriver.common.by import By
import re
from dotenv import load_dotenv

load_dotenv()


def test_text_under_input_field_green(registration):
    driver = registration
    repo_page = RepoPage(driver)
    driver.get("https://github.com/new")
    repo_page.new_text("Diplomee")
    color_text = repo_page.text_green()
    rgb_values = re.findall(r'\d+', color_text)
    r, g, b = map(int, rgb_values[:3])
    assert g > r and g > b and g > 120, f"Цвет {color_text} не похож на зеленый"


def test_text_under_input_field_red(registration):
    driver = registration
    repo_page = RepoPage(driver)
    driver.get("https://github.com/new")
    repo_page.new_text("Diplome")
    color_text = repo_page.text_red()
    rgb_values = re.findall(r'\d+', color_text)
    r, g, b = map(int, rgb_values[:3])
    assert r > g and r > b and r > 140, f"Цвет {color_text} не похож на красный"


def test_russian_text(registration):
    driver = registration
    repo_page = RepoPage(driver)
    driver.get("https://github.com/new")
    repo_page.new_text("Текст")
    text = driver.find_element(By.CSS_SELECTOR, "span[class*='ValidationText']").text
    assert "Your new repository will be created as " in text


def test_open_pullreqest(pull_req):
    driver = pull_req
    pull_page = Pull_req(driver)
    color_element = pull_page.green_element()
    rgb_values = re.findall(r'\d+', color_element)
    r, g, b = map(int, rgb_values[:3])
    assert g > r and g > b and g > 120, f"Цвет {color_element} не похож на зеленый"


def test_close_pullreqest(pull_req):
    driver = pull_req
    pull_page = Pull_req(driver)
    color_element = pull_page.red_element()
    rgb_values = re.findall(r'\d+', color_element)
    r, g, b = map(int, rgb_values[:3])
    assert r > g and r > b and r > 120, f"Цвет {color_element} не похож на красный"
