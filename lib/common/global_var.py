# -*- coding:utf-8 -*-

import os

# project absolute path
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# system account path
SYSTEM_ACCOUNT_PATH = PROJECT_PATH + u"/conf/system_account.ini"

# mail config
MAIL_HOST = "smtp.exmail.qq.com"
MAIL_PORT = 25
MAIL_USER = "yu.li@hualongdata.com"
MAIL_PWD = "Liyu12345"
MAIL_SENDER = 'yu.li@hualongdata.com'

# string list
MAIL_RECEIVERS = ["yu.li@hualongdata.com"]
# MAIL_RECEIVERS = ["xxx@hualongdata.com",
#                   "xxx@hualongdata.com"]
MAIL_SUBJECT = "自动化测试结果 - 信用重庆"
