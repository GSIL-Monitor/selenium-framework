# -*- coding:utf-8 -*-

import random
from time import sleep
from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage
from lib.page_objects.PoliceRuleDetailPage import PoliceRuleDetailPage
from lib.page_objects.ArticleListPage import ArticleListPage


class HomePage(BasePage):
    """Home page of credit net"""

    # the locators of home page elements
    loc_login = (By.XPATH, "//a[@id='zh_click_s']")
    loc_update_pwd = (By.XPATH, "//a[@id='update_pwd']")
    loc_logout = (By.XPATH, "//a[@id='exists']")
    loc_feedback = (By.XPATH, "//span[@id='register']/a")
    loc_web_statement = (By.XPATH, "//span[@class='margin_right20']/a[@class='red_h_18out']")
    loc_header_credit_infor_search = (By.XPATH, "//div[@id='nav_list_home']/span[1]")
    loc_header_united_credit_code_search = (By.XPATH, "//div[@id='nav_list_home']/span[2]")
    loc_header_article_search = (By.XPATH, "//div[@id='nav_list_home']/span[3]")
    loc_header_search_input = (By.XPATH, "//input[@id='search_input']")
    loc_header_search_submit = (By.XPATH, "//input[@class='search_btn']")
    loc_navi_home_page = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=0')]")
    loc_navi_credit_status = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=1')]")
    loc_navi_credit_pub = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=2')]")
    loc_navi_punish_reward = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=3')]")
    loc_navi_subject_govern = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=4')]")
    loc_navi_police_rule = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=5')]")
    loc_navi_credit_research = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=6')]")
    loc_navi_other = (By.XPATH, "//li[contains(@class,'nav_item nav_item1')]/a[contains(@href,'navPage=7')]")
    loc_slids_block = (By.XPATH, "//div[@id='slides']")
    loc_pic_united_credit_code_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-1.png')]")
    loc_pic_license_punish_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-2.png')]")
    loc_pic_reb_black_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-3.png')]")
    loc_pic_abnormal_enterprise_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-4.png')]")
    loc_pic_double_random_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-5.png')]")
    loc_pic_police_track_search = (By.XPATH, "//div[@class='swiper-wrapper']//img[contains(@src,'0626-6.png')]")
    loc_credit_status_more = (By.XPATH, "//span[text()='信用动态']/following-sibling::span/a")
    loc_credit_status_contents = (By.XPATH, "//div[@class='body_part_left_top_one']//span[contains(@class,'-icon')]/following-sibling::a")
    loc_police_rule_more = (By.XPATH, "//span[text()='政策法规']/following-sibling::span/a")
    loc_police_rule_contents = (By.XPATH, "//div[@class='body_part_left_top_two']//span[contains(@class,'-icon')]/following-sibling::a")
    loc_punish_reward_more = (By.XPATH, "//span[text()='联合奖惩']/following-sibling::span/a")
    loc_punish_reward_contents = (By.XPATH, "//div[@class='content_five_one_one']//span[contains(@class,'-icon')]/following-sibling::a")
    loc_credit_research_more = (By.XPATH, "//span[text()='信用研究']/following-sibling::span/a")
    loc_credit_research_contents = (By.XPATH, "//div[@class='content_five_one_two']//span[contains(@class,'-icon')]/following-sibling::a")
    loc_advanced_article_search_title = (By.XPATH, "//span[text()='文章高级搜索']")
    loc_advanced_article_search_input = (By.XPATH, "//input[@id='keywords']")
    loc_advanced_article_search_type_select = (By.XPATH, "//select[@id='search-cols']")
    loc_advanced_article_search_start_time = (By.XPATH, "//input[@id='startData']")
    loc_advanced_article_search_end_time = (By.XPATH, "//input[@id='endData']")
    loc_advanced_article_search_submit_button = (By.XPATH, "//button[@id='article-search']")
    loc_direct_credit_status = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'信用动态')]")
    loc_direct_credit_pub = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'信用公示')]")
    loc_direct_punish_reward = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'联合奖惩')]")
    loc_direct_subject_govern = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'专项治理')]")
    loc_direct_police_rule = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'政策法规')]")
    loc_direct_credit_research = (By.XPATH, " //div[@class='special_column_wrap']//li/a[contains(text(),'信用研究')]")
    loc_gathered_data_rolling = (By.XPATH, "//div[@class='content_five_two']")
    loc_third_part_group_member = (By.XPATH, "//ul[@class='conent_six_container']//div[contains(text(),'成员单位')]/following-sibling::div/ul")
    loc_third_part_county_credit_web = (By.XPATH, "//ul[@class='conent_six_container']//div[contains(text(),'区县信用网站')]/following-sibling::div/ul")
    loc_third_part_other_credit_web = (By.XPATH, "//ul[@class='conent_six_container']//div[contains(text(),'其他信用网站')]/following-sibling::div/ul")

    # The locators of login pop-up window
    loc_login_username_input = (By.XPATH, "//input[@id='username']")
    loc_login_password_input = (By.XPATH, "//input[@id='password']")
    loc_login_submit = (By.XPATH, "//input[@id='loginBtn']")

    # The locators of default pop-up alert
    loc_default_alert_window = (By.XPATH, "//div[@id='outsideAlert-zhaopin']")
    loc_default_alert_close = (By.XPATH, "//span[@class='alert-close-zhaopin']")

    # The locators of searching-check pop-up alert
    loc_search_alert_window = (By.XPATH, "//div[contains(@class,'alert-container')]")
    loc_search_alert_close = (By.XPATH, "//div[contains(@class,'alert-btn-close')]")

    '''Page element click functions'''
    # click login button to pop up login window
    def click_login(self):
        self.find_element(*self.loc_login).click()

    # submit login
    def submit_login(self):
        self.find_element(*self.loc_login_submit).click()

    # close the default pop-up window
    def close_default_alert(self):
        element = self.find_element_which_clickable(*self.loc_default_alert_close)
        element.click()
        sleep(1)

    # close the searching-check pop-up window
    def close_search_alert(self):
        element = self.find_element_which_clickable(*self.loc_search_alert_close)
        element.click()
        sleep(1)

    # click the update password button
    def click_update_pwd(self):
        self.find_element(*self.loc_update_pwd).click()

    # click the logout button
    def click_logout(self):
        self.find_element(*self.loc_logout).click()

    # click any one data of police role to check the detail
    def random_click_any_police_rule(self):
        elements = self.find_elements(*self.loc_police_rule_contents)
        random_number = random.randint(0, len(elements) - 1)
        element = elements[random_number]
        element.click()
        sleep(1)

    # click any one data of credit status to check the detail
    def random_click_any_credit_status(self):
        elements = self.find_elements(*self.loc_credit_status_contents)
        random_number = random.randint(0, len(elements) - 1)
        element = elements[random_number]
        element.click()
        sleep(1)

    # switch to header article search
    def active_header_article_search(self):
        self.find_element(*self.loc_header_article_search).click()

    # click header search button
    def click_header_search_btn(self):
        self.find_element(*self.loc_header_search_submit).click()
        sleep(1)

    '''Page element input functions'''
    # input user name
    def type_username(self, username):
        self.find_element(*self.loc_login_username_input).clear()
        self.find_element(*self.loc_login_username_input).send_keys(username)

    # input user password
    def type_password(self, password):
        self.find_element(*self.loc_login_password_input).clear()
        self.find_element(*self.loc_login_password_input).send_keys(password)

    # input content as search criteria
    def header_search_input(self, content):
        self.send_keys(content, True, True, *self.loc_header_search_input)

    '''Page element exists checking'''
    # check whether the default alert window pops up
    def default_alert_pops(self):
        element = self.find_element(*self.loc_default_alert_window)
        if type(element) == bool:
            return False
        else:
            return True

    # check whether the searching-check alert window pops up
    def search_alert_pops(self):
        element = self.find_element_which_displayed_without_error_log(*self.loc_search_alert_window)
        if type(element) == bool:
            return False
        else:
            return True

    # check whether the update password button displays
    def update_pwd_button_show(self):
        element = self.find_element(*self.loc_update_pwd)
        if type(element) == bool:
            return False
        else:
            return True

    # check whether the logout button displays
    def logout_button_show(self):
        element = self.find_element(*self.loc_logout)
        if type(element) == bool:
            return False
        else:
            return True

    # check whether the login button displays
    def login_button_show(self):
        element = self.find_element(*self.loc_login)
        if type(element) == bool:
            return False
        else:
            return True

    '''Page navigation functons'''
    # switch to police rule detail page from home page
    def switch_to_police_rule_detail_page(self, current_handle):
        all_handles = self.get_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.switch_to_window(handle)
        page_object = PoliceRuleDetailPage(self.driver)
        return page_object

    # switch to article list page from home page
    def switch_to_article_list_page(self, current_handle):
        all_handles = self.get_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.switch_to_window(handle)
        page_object = ArticleListPage(self.driver)
        return page_object


