# -*- coding:utf-8 -*-
import unittest
from lib.common.webdriver import initialize_browser
from lib.common.credit_functions import open_credit, login_credit_system

# data structure defined for below test case


class CaseClassName(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_browser()

    def testCaseName(self):
        """enter some description about the test case"""
        home_page = open_credit(self.driver)
        login_credit_system(home_page)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()