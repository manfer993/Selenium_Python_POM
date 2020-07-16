from Locators.locators import Locators
from time import sleep


class JobTitlesPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_button_id = Locators.add_button_id
        self.job_title_textbox_id = Locators.job_title_textbox_id
        self.job_description_textbox_id = Locators.job_description_textbox_id
        self.save_job_button_id = Locators.save_job_button_id
        self.delete_button_id = Locators.delete_button_id
        self.confirm_delete_button_id = Locators.confirm_delete_button_id

    def click_add_job(self):
        self.driver.find_element_by_id(self.add_button_id).click()

    def enter_title(self, title):
        self.driver.find_element_by_id(self.job_title_textbox_id).clear()
        self.driver.find_element_by_id(self.job_title_textbox_id).send_keys(title)

    def enter_description(self, description):
        self.driver.find_element_by_id(self.job_description_textbox_id).clear()
        self.driver.find_element_by_id(self.job_description_textbox_id).send_keys(description)

    def click_save_job(self):
        self.driver.find_element_by_id(self.save_job_button_id).click()

    def check_job(self, title):
        for index, element in enumerate(self.driver.find_elements_by_xpath(Locators.tittle_results_xpath), start=1):
            if element.get_attribute('innerText').strip() == title:
                self.driver.find_element_by_xpath(Locators.checkbox_result(str(index))).click()
                break

    def click_delete_job(self):
        self.driver.find_element_by_id(self.delete_button_id).click()

    def click_confirmation_delete_job(self):
        self.driver.find_element_by_id(self.confirm_delete_button_id).click()
