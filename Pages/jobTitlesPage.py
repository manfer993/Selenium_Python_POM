from Locators.locators import Locators
from selenium.webdriver.common.by import By


class JobTitlesPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.ID, Locators.add_button_id)
        self.job_title_textbox = (By.ID, Locators.job_title_textbox_id)
        self.job_description_textbox = (By.ID, Locators.job_description_textbox_id)
        self.save_job_button = (By.ID, Locators.save_job_button_id)
        self.delete_button = (By.ID, Locators.delete_button_id)
        self.confirm_delete_button = (By.ID, Locators.confirm_delete_button_id)
        self.title_result_text = (By.XPATH, Locators.title_results_xpath)

    def click_add_job(self):
        self.driver.find_element(*self.add_button).click()

    def enter_title(self, title):
        self.driver.find_element(*self.job_title_textbox).clear()
        self.driver.find_element(*self.job_title_textbox).send_keys(title)

    def enter_description(self, description):
        self.driver.find_element(*self.job_description_textbox).clear()
        self.driver.find_element(*self.job_description_textbox).send_keys(description)

    def click_save_job(self):
        self.driver.find_element(*self.save_job_button).click()

    def check_job(self, title):
        for index, element in enumerate(self.driver.find_elements(*self.title_result_text), start=1):
            if element.get_attribute('innerText').strip() == title:
                self.driver.find_element_by_xpath(Locators.checkbox_result(str(index))).click()
                break

    def click_delete_job(self):
        self.driver.find_element(*self.delete_button).click()

    def click_confirmation_delete_job(self):
        self.driver.find_element(*self.confirm_delete_button).click()
