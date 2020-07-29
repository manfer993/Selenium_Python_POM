from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.jobTitlesPage import JobTitlesPage
from Tests.baseTest import BaseTest
from Utils.inputs import Inputs

import unittest
import HtmlTestRunner


class JobsTest(BaseTest):

    @classmethod
    def setUp(cls) -> None:
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.job_titles = JobTitlesPage(cls.driver)

    @unittest.skip('test')
    def test_create_new_job(self):
        self.base.open(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.click_admin_menu_1level()
        self.home.click_job_menu_2level()
        self.home.click_job_titles_opt()

        self.job_titles.click_add_job()
        self.job_titles.enter_title(Inputs.job_title)
        self.job_titles.enter_description(Inputs.job_description)
        self.job_titles.click_save_job()

        self.home.validate_welcome()
        self.home.click_logout()

    @unittest.skip('test')
    def test_delete_new_job(self):
        self.base.open(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.click_admin_menu_1level()
        self.home.click_job_menu_2level()
        self.home.click_job_titles_opt()

        self.job_titles.check_job(Inputs.job_title)
        self.job_titles.click_delete_job()
        self.job_titles.click_confirmation_delete_job()

        self.home.validate_welcome()
        self.home.click_logout()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
