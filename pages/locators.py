from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages div.alert div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")