# -*- coding:utf-8 -*-
import unittest
import csv
import os
from lib.common.webdriver import initialize_browser
from selenium.webdriver.common.by import By
from lib.common.log import logger
from lib.common.credit_functions import open_credit, test_page_links

# data structure defined for below test case
loc_links = list()
is_tc_pass = True


class CreditHomeLinksCheck(unittest.TestCase):
    def setUp(self):
        global loc_links
        self.driver = initialize_browser()

        # prepare test data - fetch page links locator
        try:
            data_file = os.path.dirname(os.path.dirname(__file__)) + "/data/credit_home_links_check.csv"
            data_file = os.path.abspath(data_file)
            data = csv.reader(open(data_file, 'r'))
        except:
            logger.error("Failed to open data file!")

        for line in data:
            if line[0] != "section" and line[0] != "":
                loc_links.append(line[1])
        logger.info("The links are {}".format(loc_links))

        # prepare test data - fetch base url
        try:
            file_path = os.path.dirname(os.path.dirname(__file__)) + "/data/Global_Environment.csv"
            data_file = os.path.abspath(file_path)
            data = csv.reader(open(data_file, 'r'))
        except:
            logger.error("Failed to open data file!")

        for item in data:
            if item[0] == "URL":
                self.url = item[1]
        logger.info("The url is {}".format(self.url))

    def testHomeLinksCheck(self):
        '''Check the main links of home page can be opened successfully.'''
        global is_tc_pass
        home_page = open_credit(self.driver)
        for loc_link in loc_links:
            loc_link = eval(loc_link)
            is_tc_pass = test_page_links(home_page, *loc_link)
        if is_tc_pass:
            logger.info("All the links can be opened successfully!")
        else:
            raise AssertionError("Some links can NOT be opened, please refer to the log file for more detail!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()