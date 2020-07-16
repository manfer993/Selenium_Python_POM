from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_button_link_text = Locators.logout_button_link_text
        self.admin_button_id = Locators.admin_button_id
        self.job_sub_btn_admin_id = Locators.job_sub_btn_admin_id
        self.menu_job_title_button_id = Locators.menu_job_title_button_id

    def validate_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_link_text).click()

    def click_admin_menu_1level(self):
        self.driver.find_element_by_id(self.admin_button_id).click()

    def click_job_menu_2level(self):
        self.driver.find_element_by_id(self.job_sub_btn_admin_id).click()

    def click_job_titles_opt(self):
        self.driver.find_element_by_id(self.menu_job_title_button_id).click()
