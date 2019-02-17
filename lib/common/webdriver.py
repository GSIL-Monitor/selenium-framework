# -*- coding:utf-8 -*-
from selenium import webdriver


def browser_chrome():
    #load google chrome browser and initiate testing environment
    #prefs = {'profile.default_content_settings.popups': 0}
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option('prefs', prefs)
    #options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def browser_firefox():
    #load firefox browser and initiate testing environment
    #options = webdriver.FirefoxOptions()
    #options.add_argument('-headless')
    #driver = webdriver.Firefox(executable_path='geckodriver', firefox_options=options)
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


def initialize_browser():
    return browser_chrome()
