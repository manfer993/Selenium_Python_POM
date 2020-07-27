from Locators.locators import Locators
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, Locators.username_textbox_id)
        self.password_textbox = (By.ID, Locators.password_textbox_id)
        self.login_button = (By.ID, Locators.login_button_id)
        self.invalidUsername_message = (By.ID, Locators.invalidUsername_message_id)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).clear()
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).clear()
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def check_invalid_message(self):
        return self.driver.find_element(*self.invalidUsername_message).text
