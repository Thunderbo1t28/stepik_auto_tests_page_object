from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_content(self):
        self.should_be_empty_basket()
        self.should_be_empty_basket_text_true()

    def should_be_empty_basket(self):
        list_items = self.is_element_present(*BasketPageLocators.LIST_ITEMS)
        assert not list_items, "Basket contains items, but should not be"

    def should_be_empty_basket_text_true(self):
        text_basket = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_EMPTY)
        assert text_basket, "Basket page no contains emty text, but should be"