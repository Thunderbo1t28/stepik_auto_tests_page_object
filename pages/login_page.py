from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_password_repeat = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REPEAT)
        input_password_repeat.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "No correct url, url not contains string login"

    def should_be_login_form(self):
        form_login = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(form_login)>0, "Page not contains login form"

    def should_be_register_form(self):
        form_registration = self.browser.find_elements(*LoginPageLocators.LOGIN_REGISTRATION_FORM)
        assert len(form_registration) > 0, "Page not contains form registration"
