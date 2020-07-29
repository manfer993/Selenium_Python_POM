from Utils.locators import *
from Pages.basePage import BasePage


class JobTitlesPage(BasePage):

    def __init__(self, driver):
        super(JobTitlesPage, self).__init__(driver)
        self.locator = JobTitlePageLocators

    def click_add_job(self):
        self.click(*self.locator.add_button_id)

    def enter_title(self, title):
        self.clear_text(*self.locator.job_title_textbox_id)
        self.send_text(title, *self.locator.job_title_textbox_id)

    def enter_description(self, description):
        self.clear_text(*self.locator.job_description_textbox_id)
        self.send_text(description, *self.locator.job_description_textbox_id)

    def click_save_job(self):
        self.click(*self.locator.save_job_button_id)

    def check_job(self, title):
        for index, element in enumerate(self.find_elements(*self.locator.title_results_xpath), start=1):
            if element.get_attribute('innerText').strip() == title:
                self.click(self.locator.checkbox_result(str(index)))
                break

    def click_delete_job(self):
        self.click(*self.locator.delete_button_id)

    def click_confirmation_delete_job(self):
        self.click(*self.locator.confirm_delete_button_id)
