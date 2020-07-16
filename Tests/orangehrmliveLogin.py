from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.jobTitlesPage import JobTitlesPage
from Locators.inputs import Inputs
from time import sleep

import HtmlTestRunner
import unittest


class OrangeHrmLiveLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        option = Options()
        option.add_argument('--window-size=1920,1080')
        # option.add_argument('--start-maximized')
        option.add_argument('incognito')
        # option.add_argument('--headless')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        cls.driver.implicitly_wait(5)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.jobTitles = JobTitlesPage(cls.driver)

    # @unittest.skip('test')
    def test_login_valid(self):
        self.driver.get(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.validate_welcome()
        self.home.click_logout()

    # @unittest.skip('test')
    def test_create_new_job(self):
        self.driver.get(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.click_admin_menu_1level()
        self.home.click_job_menu_2level()
        self.home.click_job_titles_opt()

        self.jobTitles.click_add_job()
        self.jobTitles.enter_title(Inputs.job_title)
        self.jobTitles.enter_description(Inputs.job_description)
        self.jobTitles.click_save_job()

        self.home.validate_welcome()
        self.home.click_logout()

    def test_delete_new_job(self):
        self.driver.get(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.click_admin_menu_1level()
        self.home.click_job_menu_2level()
        self.home.click_job_titles_opt()

        self.jobTitles.check_job(Inputs.job_title)
        self.jobTitles.click_delete_job()
        self.jobTitles.click_confirmation_delete_job()

        self.home.validate_welcome()
        self.home.click_logout()

    # @unittest.skip('test')
    def test_login_invalid_user(self):
        self.driver.get(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.invalid_username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        message = self.login.check_invalid_message()
        self.assertEqual(message, Inputs.assert_invalid_credentials)

    # @unittest.skip('test')
    def test_login_invalid_password(self):
        self.driver.get(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.invalid_password)
        self.login.click_login()

        message = self.login.check_invalid_message()
        self.assertEqual(message, Inputs.assert_invalid_credentials)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
