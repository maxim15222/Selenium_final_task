from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        registration_password.send_keys(password)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        registration_password_confirm.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()
