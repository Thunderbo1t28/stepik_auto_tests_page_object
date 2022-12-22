from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket_button.click()
