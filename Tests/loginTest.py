from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Tests.baseTest import BaseTest
from Utils.inputs import Inputs

import unittest
import HtmlTestRunner


class LoginTest(BaseTest):

    @classmethod
    def setUp(cls) -> None:
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)

    # @unittest.skip('test')
    def test_login_valid(self):
        self.base.open(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        self.home.validate_welcome()
        self.home.click_logout()

    # @unittest.skip('test')
    def test_login_invalid_user(self):
        self.base.open(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.invalid_username)
        self.login.enter_password(Inputs.password)
        self.login.click_login()

        message = self.login.check_invalid_message()
        self.assertEqual(message,
                         Inputs.assert_invalid_credentials,
                         Inputs.assert_invalid_credentials_message)

    # @unittest.skip('test')
    def test_login_invalid_password(self):
        self.base.open(Inputs.orangehrmlive_url)

        self.login.enter_username(Inputs.username)
        self.login.enter_password(Inputs.invalid_password)
        self.login.click_login()

        message = self.login.check_invalid_message()
        self.assertEqual(message,
                         Inputs.assert_invalid_credentials,
                         Inputs.assert_invalid_credentials_message)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
