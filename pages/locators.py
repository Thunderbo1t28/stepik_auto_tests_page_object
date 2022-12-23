from selenium.webdriver.common.by import By

#Gt7-Rks-HMm-cqQ
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")

class BasketPageLocators():
    LIST_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "div.content div#content_inner p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    INPUT_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages div.alert div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")