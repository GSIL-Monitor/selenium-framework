# -*- coding:utf-8 -*-
import unittest
from lib.common.webdriver import initialize_browser
from lib.common.log import logger
from lib.common.credit_functions import open_credit, login_credit_system, generate_dict_then_append_as_list, \
    generate_partial_query_str

# data structure defined for below test case
actual_article_dict = dict()
result_list = []
partial_result_list = []


class HeaderArticleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_browser()

    def testHeaderArticleSearch(self):
        '''check header article search with full-match-mode and partial-match-mode'''
        global result_list, partial_result_list
        home_page = open_credit(self.driver)
        login_credit_system(home_page)
        current_handle = home_page.get_current_window_handle()
        flag = True
        # fetch the required data which does not contains special characters
        while flag:
            home_page.random_click_any_police_rule()
            police_rule_detail_page = home_page.switch_to_police_rule_detail_page(current_handle)
            article_title = police_rule_detail_page.fetch_data_title()
            article_publish_time = police_rule_detail_page.fetch_data_publish_time()
            police_rule_detail_page.close_current_window()
            police_rule_detail_page.switch_to_window(current_handle)
            actual_article_dict['name'] = article_title
            actual_article_dict['time'] = article_publish_time
            home_page.active_header_article_search()
            home_page.header_search_input(article_title)
            home_page.click_header_search_btn()
            if home_page.search_alert_pops():
                home_page.close_search_alert()
                continue
            else:
                logger.info("The for-searched name and time have been fetched: {},{}".
                              format(article_title, article_publish_time))
                break
        article_list_page = home_page.switch_to_article_list_page(current_handle)
        # load all searched out data
        article_list_page.load_all_data()
        result_list = generate_dict_then_append_as_list(article_list_page.fetch_data_titles(),
                                                        article_list_page.fetch_data_publish_times())
        # existing check
        if actual_article_dict in result_list:
            logger.info("The article: {} has been searched out successfully in full-match-mode!".
                          format(actual_article_dict['name']))
        else:
            raise AssertionError("Fail to searched out article: {} in full-match-mode!".format(actual_article_dict['name']))

        article_list_page.close_current_window()
        article_list_page.switch_to_window(current_handle)
        # generate searching data
        query_string = generate_partial_query_str(actual_article_dict['name'], 5)
        home_page.active_header_article_search()
        home_page.header_search_input(query_string)
        home_page.click_header_search_btn()
        article_list_page = home_page.switch_to_article_list_page(current_handle)
        article_list_page.load_all_data()
        partial_result_list = generate_dict_then_append_as_list(article_list_page.fetch_data_titles(),
                                                                article_list_page.fetch_data_publish_times())
        # existing check
        if actual_article_dict in partial_result_list:
            logger.info("The article: {} has been searched out successfully in partial-match-mode!".
                          format(actual_article_dict['name']))
        else:
            raise AssertionError("Fail to searched out article: {} in partial-match-mode!".format(query_string))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()