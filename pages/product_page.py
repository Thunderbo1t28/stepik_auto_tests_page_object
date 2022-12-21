from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def should_be_product_name(self):
        form_login = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert form_login == message_name, "Product name incorected!"

    def should_be_product_price(self):
        form_login = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        assert form_login == message_name, "Product price incorected!"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()