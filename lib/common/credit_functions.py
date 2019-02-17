# -*- coding:utf-8 -*-
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from lib.common.log import logger
from lib.page_objects.HomePage import HomePage
from lib.common.parse_file import ParseYaml


# open credit system
def open_credit(driver):
    # open data file to get base url
    try:
        file_obj = ParseYaml('project.yml')
        data_dict = file_obj.get_yaml_dict()
        url = data_dict['URL']
        page_obj = HomePage(driver)
        page_obj.open(url)
        if page_obj.default_alert_pops():
            page_obj.close_default_alert()
        return page_obj

    except Exception as e:
        logger.error("Failed to open data file!")
        logger.error(e)


# login credit system
def login_credit_system(page_obj):
    # open data file to get user name and password
    try:
        file_obj = ParseYaml('project.yml')
        data_dict = file_obj.get_yaml_dict()
        username = data_dict['UserName']
        password = data_dict['Password']
        page_obj.click_login()
        page_obj.type_username(username)
        page_obj.type_password(password)
        page_obj.submit_login()
        if page_obj.default_alert_pops():
            page_obj.close_default_alert()
        if page_obj.logout_button_show() and page_obj.update_pwd_button_show():
            logger.info("User: {} login system successfully!".format(username))
        else:
            logger.error("User: {} failed to login system!".format(password))
    except Exception as e:
        logger.error("Failed to open data file!")
        logger.error(e)


# generate dictionary data and then return as a dictionary list
def generate_dict_then_append_as_list(list_key, list_value):
    tmp_list = list()
    i = 0
    try:
        if len(list_key) == len(list_value):
            while i < len(list_key):
                tmp_list += generate_list_with_one_dict(list_key, list_value, i)
                i += 1
        return tmp_list

    except Exception as e:
        logger.error("Fail to generate dictionary list!")
        logger.error(e)


# generate one list which has one dictionary member from two lists
def generate_list_with_one_dict(list_key, list_value, index):
    tmp_list = list()
    tmp_dict = dict()
    tmp_dict['name'] = list_key[index]
    tmp_dict['time'] = list_value[index]
    tmp_list.append(tmp_dict)
    return tmp_list


# cut piece of a string
def generate_partial_query_str(str_value, cut_len):
    tmp_str = str_value[:cut_len]
    return tmp_str


def test_page_links(page_object, *loc_links):
    """
    test whether links in page can be opened correctly, by comparing url
    :param page_object:
    :param loc_links:
    :return: boolean, True or False
    """

    is_tc_pass = True

    try:
        # close additional windows before test
        # get the original page
        original_window = page_object.get_current_window_handle()
        all_handles = page_object.get_window_handles()
        for handle in all_handles:
            if handle != original_window:
                page_object.switch_to_window(handle)
                page_object.close_current_window()
        # switch back to the original page
        page_object.switch_to_window(original_window)

        # find links
        element_links = page_object.find_elements(*loc_links)
        logger.info("The elements have been found: {}".format(len(element_links)))

        if type(element_links) == list and len(element_links) > 0:

            for index in range(0, len(element_links)):

                link_url = element_links[index].get_attribute('href')

                if link_url is not None:
                    link_url = link_url.strip()

                    # check whether to open new page window
                    target_window = element_links[index].get_attribute('target')
                    open_new_window = False
                    if (target_window is not None) and (target_window.strip() == '_blank'):
                        open_new_window = True

                    element_links[index].click()

                    if not open_new_window:
                        if not check_open_in_current_window(page_object, link_url):
                            is_tc_pass = False
                        element_links = page_object.find_elements(*loc_links)
                    else:
                        if not check_open_in_new_window(page_object, link_url, original_window):
                            is_tc_pass = False
            return is_tc_pass

        else:
            logger.error("Fail to locate links")
            return False

    except Exception as e:
        logger.error(e)
        return False


def check_open_in_current_window(page_object, link_url):
    """
    check whether link is opened successfully in current page window
    :param page_object: page object
    :param link_url: target url address
    :return: True or False
    """
    time.sleep(1)
    try:
        if WebDriverWait(page_object.driver, 20).until(ec.url_to_be(link_url)):
            logger.info("Pass to open link: {}".format(link_url))
            return True
        else:
            logger.error("Fail to compare links. \n Actual: {}. \n Expected:{}."
                           .format(page_object.driver.current_url, link_url))
            return False

    except TimeoutException:
        logger.error("Timeout Exception. Fail to open link: {}".format(link_url))
        return False

    except Exception as e:
        logger.error(e)
        return False


def check_open_in_new_window(page_object, link_url, original_window):
    """
    check whether link is opened successfully in new page window
    :param page_object: page object
    :param link_url: target url address
    :param original_window: window where link is clicked
    :return: boolean, True or False
    """

    time.sleep(1)
    try:
        is_tc_pass = True

        all_handles = page_object.get_window_handles()

        for handle in all_handles:
            if handle != original_window:
                page_object.switch_to_window(handle)
                if WebDriverWait(page_object.driver, 20).until(ec.url_to_be(link_url)):
                    logger.info("Pass to open link: {}".format(link_url))
                else:
                    logger.error("Fail to compare links. \n Actual: {}. \n Expected:{}."
                                   .format(page_object.driver.current_url, link_url))
                    is_tc_pass = False
                page_object.close_current_window()
        page_object.switch_to_window(original_window)

        return is_tc_pass

    except TimeoutException:
        logger.error("Timeout Exception. Fail to open link: {}".format(link_url))
        return False

    except Exception as e:
        logger.error(e)
        return False
