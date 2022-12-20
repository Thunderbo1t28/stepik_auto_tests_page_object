from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "No correct url, url not contains string login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        form_login = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(form_login)>0, "Page not contains login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        form_registration = self.browser.find_elements(*LoginPageLocators.LOGIN_REGISTRATION_FORM)
        assert len(form_registration) > 0, "Page not contains form registration"
