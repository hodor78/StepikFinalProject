from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.email = self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.password = self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRMATION), "you are not registered"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not present in the url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"