# -*- coding:utf-8 -*-

import unittest
# from xvfbwrapper import Xvfb
from HTMLTestRunner import HTMLTestRunner

from lib.common.global_var import PROJECT_PATH
from lib.common.send_email import SendMail
from scripts.credit_login import CreditLogin
from scripts.credit_home_header_article_search import HeaderArticleSearch
from scripts.credit_home_links_check import CreditHomeLinksCheck

if __name__ == "__main__":

    report_file_path = PROJECT_PATH + "/report/automation_test_report.html"
    report = open(report_file_path, "wb")

    total_suite = unittest.TestSuite()
    total_suite.addTest(CreditLogin("testCreditLogin"))
    # total_suite.addTest(HeaderArticleSearch("testHeaderArticleSearch"))
    # total_suite.addTest(CreditHomeLinksCheck("testHomeLinksCheck"))

    '''触发执行'''
    # vdisplay = Xvfb(width=1920, height=1080)
    # vdisplay.start()
    runner = HTMLTestRunner(stream=report, title="Automation Test Report", description="重庆信用信息")
    result = runner.run(total_suite)
    report.close()
    # vdisplay.stop()

    # obj_email = SendMail(report_file_path)
    # obj_email.send_email()



