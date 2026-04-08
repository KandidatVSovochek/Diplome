import allure
from selenium.webdriver.common.by import By


class RepoPage:

    @allure.step("api.Перейти на страницу сайта по ссылке: {url}")
    def __init__(self, driver, url: str = "https://github.com/new"):
        """
            Эта функция нужна чтобы перейти на страницу
            создания нового репозитория.
            Функция берет значение url и отправляет запрос на указанный адрес.
            :url: str
            :return: None
        """
        self.driver = driver
        self.driver.get(url)
        self.input_text = (By.CSS_SELECTOR, "#repository-name-input")
        self.error_message = (By.ID, "RepoNameInput-message")
        self.not_error_message = (By.ID, "RepoNameInput-is-available")

#  ввод в поле названия рапозитория
    @allure.step("Ввести в поле Repository name название нового репозитория")
    def new_text(self, name):
        """
            Эта функция берет значение name и
            подставляет в указанное поле.
            :name: str | int
            :return: None
        """
        self.driver.find_element(*self.input_text).send_keys(name)

# проверка для неправильного названия
    @allure.step("Определить цвет текста, при вводе имени,"
                 "которое уже используется в аакаунте"
                 "как название репозитория")
    def text_red(self):
        """
            Эта функция определяет цвет надписи при вводе
            названия репозитория которое уже занято.
            :return: None
        """
        element = self.driver.find_element(*self.error_message)
        return element.value_of_css_property("color")

# проверка для правильного названия
    @allure.step("Определить цвет текста, при вводе имени,"
                 "которое ренее не использовалось")
    def text_green(self):
        """
            Эта функция определяет цвет надписи при вводе названия
            репозитория которое ренее не использовалось.
            :return: None
        """
        element = self.driver.find_element(*self.not_error_message)
        return element.value_of_css_property("color")
