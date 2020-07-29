from Utils.locators import *
from Pages.basePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.locator = HomePageLocators

    def validate_welcome(self):
        self.click(*self.locator.welcome_link_id)

    def click_logout(self):
        self.click(*self.locator.logout_button_link_text)

    def click_admin_menu_1level(self):
        self.click(*self.locator.admin_button_id)

    def click_job_menu_2level(self):
        self.click(*self.locator.job_sub_btn_admin_id)

    def click_job_titles_opt(self):
        self.click(*self.locator.menu_job_title_button_id)
