from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Locators.inputs import Inputs

import HtmlTestRunner
import unittest


class OrangeHrmLiveLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get(Inputs.orangehrmlive_url)

        login = LoginPage(self.driver)
        login.enter_username(Inputs.username)
        login.enter_password(Inputs.password)
        login.click_login()

        home = HomePage(self.driver)
        home.validate_welcome()
        home.click_logout()

    def test_login_invalid_user(self):
        self.driver.get(Inputs.orangehrmlive_url)

        login = LoginPage(self.driver)
        login.enter_username(Inputs.invalid_username)
        login.enter_password(Inputs.password)
        login.click_login()

        message = login.check_invalid_message()
        self.assertEqual(message, Inputs.assert_invalid_credentials)

    def test_login_invalid_password(self):
        self.driver.get(Inputs.orangehrmlive_url)

        login = LoginPage(self.driver)
        login.enter_username(Inputs.username)
        login.enter_password(Inputs.invalid_password)
        login.click_login()

        message = login.check_invalid_message()
        self.assertEqual(message, Inputs.assert_invalid_credentials)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
