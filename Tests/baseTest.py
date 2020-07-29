from Pages.basePage import *

import unittest


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = chrome_driver_connection()
        cls.base = BasePage(cls.driver)
        cls.base.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.base.close()
        cls.base.quit()
