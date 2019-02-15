# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class PoliceRuleDetailPage(BasePage):
    """detail page of police and rules"""

    # the locators of police and rules page elements
    loc_title = (By.XPATH, "//div[@class='artical_page_detail']//h2")
    loc_publish_time = (By.XPATH, "(//div[@class='artical_page_detail']//span)[1]")

    # fetch data title
    def fetch_data_title(self):
        element = self.find_element(*self.loc_title)
        return element.text.strip()

    # fetch data publish time
    def fetch_data_publish_time(self):
        element = self.find_element(*self.loc_publish_time)
        return element.text.strip()


