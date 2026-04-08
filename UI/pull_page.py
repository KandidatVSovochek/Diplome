import allure
from selenium.webdriver.common.by import By


class Pull_req:
    def __init__(self, driver):
        self.driver = driver
        self.green_pic = (By.CSS_SELECTOR,
                          "svg.octicon-git-pull-request.color-fg-open")
        self.red_pic = (By.CSS_SELECTOR,
                        "svg.octicon-git-pull-request-closed.color-fg-closed")

    @allure.step("Определить цвет значка открытого pull request")
    def green_element(self):
        """
            Эта функция нужна для опреления цвета определенного элемента.
            :return: None
        """
        element = self.driver.find_element(*self.green_pic)
        return element.value_of_css_property("color")

    @allure.step("Определить цвет значка закрытого pull request")
    def red_element(self):
        """
            Эта функция нужна для опреления цвета определенного
            элемента в разделе закурытых pull request.
            :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 "a[data-ga-click*='Closed']").click()
        element = self.driver.find_element(*self.red_pic)
        return element.value_of_css_property("color")
