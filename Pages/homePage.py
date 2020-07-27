from Locators.locators import Locators
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link = (By.ID, Locators.welcome_link_id)
        self.logout_button = (By.LINK_TEXT, Locators.logout_button_link_text)
        self.admin_button = (By.ID, Locators.admin_button_id)
        self.job_sub_btn_admin = (By.ID, Locators.job_sub_btn_admin_id)
        self.menu_job_title_button = (By.ID, Locators.menu_job_title_button_id)

    def validate_welcome(self):
        self.driver.find_element(*self.welcome_link).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()

    def click_admin_menu_1level(self):
        self.driver.find_element(*self.admin_button).click()

    def click_job_menu_2level(self):
        self.driver.find_element(*self.job_sub_btn_admin).click()

    def click_job_titles_opt(self):
        self.driver.find_element(*self.menu_job_title_button).click()
