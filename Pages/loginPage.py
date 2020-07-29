from Utils.locators import *
from Pages.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.locator = LoginPageLocators

    def enter_username(self, username):
        self.clear_text(*self.locator.username_textbox_id)
        self.send_text(username, *self.locator.username_textbox_id)

    def enter_password(self, password):
        self.clear_text(*self.locator.password_textbox_id)
        self.send_text(password, *self.locator.password_textbox_id)

    def click_login(self):
        self.click(*self.locator.login_button_id)

    def check_invalid_message(self):
        return self.get_text(*self.locator.invalidUsername_message_id)
