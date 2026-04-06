from selenium.webdriver.common.by import By


class RepoPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://github.com/new")
        self.input_text = (By.ID, "repository-name-input")
        self.error_message = (By.ID, "RepoNameInput-message")
        self.not_error_message = (By.ID, "RepoNameInput-is-available")

#  ввод в поле названия рапозитория
    def new_text(self, name):
        self.driver.find_element(*self.input_text).send_keys(name)

# проверка для неправильного названия
    def text_red(self):
        element = self.driver.find_element(*self.error_message)
        return element.value_of_css_property("color")


# проверка для правильного названия
    def text_green(self):
        element = self.driver.find_element(*self.not_error_message)
        return element.value_of_css_property("color")
