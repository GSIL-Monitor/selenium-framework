# -*- coding:utf-8 -*-
import unittest
from lib.common.webdriver import initialize_browser
from lib.common.log import logger
from lib.page_objects.HomePage import HomePage
from lib.common.parse_file import ParseYaml


class CreditLogin(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_browser()
        # preparing test data
        try:
            file_obj = ParseYaml('project.yml')
            data_dict = file_obj.get_yaml_dict()
            self.URL = data_dict['URL']
            self.UserName = data_dict['UserName']
            self.Password = data_dict['Password']
        except Exception as e:
            logger.error("Failed to open data file!")
            logger.error(e)

    def testCreditLogin(self):
        """Check login/logout credit system"""
        home_page = HomePage(self.driver)
        home_page.open(self.URL)
        if home_page.default_alert_pops():
            home_page.close_default_alert()
        home_page.click_login()
        home_page.type_username(self.UserName)
        home_page.type_password(self.Password)
        home_page.submit_login()
        if home_page.default_alert_pops():
            home_page.close_default_alert()
        if home_page.logout_button_show() and home_page.update_pwd_button_show():
            logger.info("User: {} login system successfully!".format(self.UserName))
        else:
            logger.error("User: {} failed to login system!".format(self.UserName))
            raise AssertionError("Failed to login system!")

        home_page.click_logout()
        if home_page.default_alert_pops():
            home_page.close_default_alert()
        if home_page.login_button_show():
            logger.info("User: {} logout system successfully!".format(self.UserName))
        else:
            logger.error("User: {} failed to logout system!".format(self.UserName))
            raise AssertionError("Failed to logout system!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()