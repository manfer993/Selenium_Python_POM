from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_button_link_text = Locators.logout_button_link_text

    def validate_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_link_text).click()
