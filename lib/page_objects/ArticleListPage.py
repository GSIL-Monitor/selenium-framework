# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class ArticleListPage(BasePage):
    """
    article list page
    """

    # the locators of police and rules page elements
    loc_titles = (By.XPATH, "//ul[@id='search-result-list']//h4//a")
    loc_publish_times = (By.XPATH, "//ul[@id='search-result-list']//div[@class='column-mesg']//span")
    loc_search_more = (By.XPATH, "//div[contains(text(),'加载更多')]")
    loc_no_more = (By.XPATH, "//div[contains(text(),'没有更多')]")

    # fetch data title
    def fetch_data_titles(self):
        title_list = []
        elements = self.find_elements(*self.loc_titles)
        for element in elements:
            title_list.append(element.text.strip())
        return title_list

    # fetch data publish time
    def fetch_data_publish_times(self):
        time_list = []
        elements = self.find_elements(*self.loc_publish_times)
        for element in elements:
            time_list.append(element.text.strip())
        return time_list

    # load all data
    def load_all_data(self):
        flag = True
        while flag:
            if self.find_element_which_displayed_without_error_log(*self.loc_search_more):
                self.find_element_which_clickable(*self.loc_search_more).click()
                sleep(1)
            elif self.find_element_which_displayed_without_error_log(*self.loc_no_more):
                break



