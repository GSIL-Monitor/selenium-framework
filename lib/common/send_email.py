# -*- coding:utf-8 -*-

# email lib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from bs4 import BeautifulSoup
from conf.global_var import *
from lib.common.log import logger


class SendMail(object):
    def __init__(self, report_file_path, send_mail_always=False):
        """
        Constructor
        :param report_file_path: path of html report file
        :param send_mail_always: if False, send mail only when test case fail; if True, send mail always
        """
        self.report_file_path = report_file_path
        self.send_mail_always = send_mail_always

    def send_email(self):
        """
        parse report file, then send mail
        :return: N/A
        """
        ret_code = self.parse_report_html()
        if self.send_mail_always or ret_code !=0:
            self.set_email(ret_code)

    def set_email(self, ret_code):
        """
        set email service, attachment, etc
        :param ret_code: return code from parse_report_html
        :return: N/A
        """
        try:
            # third party SMTP service
            mail_host = MAIL_HOST
            mail_port = MAIL_PORT
            mail_user = MAIL_USER
            mail_pwd = MAIL_PWD
            sender = MAIL_SENDER
            receivers = MAIL_RECEIVERS

            # email attachment
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = ";".join(receivers)
            if ret_code == 0:
                subject = '全部成功√√√{}'.format(MAIL_SUBJECT)
            elif ret_code == 10010:
                subject = '解析报告失败！！！{}'.format(MAIL_SUBJECT)
            else:
                subject = '失败用例数：{}！！！{}'.format(ret_code, MAIL_SUBJECT)
            message['Subject'] = Header(subject, 'utf-8')

            # email body
            message.attach(MIMEText('附件为{}，请查收'.format(MAIL_SUBJECT), 'plain', 'utf-8'))

            # email attachment
            att1 = MIMEText(open(self.report_file_path, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="automation_test_report.html"'
            message.attach(att1)

            obj_smtp = smtplib.SMTP()
            obj_smtp.connect(mail_host, mail_port)
            obj_smtp.login(mail_user, mail_pwd)
            obj_smtp.sendmail(sender, receivers, message.as_string())
            obj_smtp.quit()
            logger.info("Pass to send email")

        except Exception as e:
            logger.error(e)

    def parse_report_html(self):
        """
        judge whether all test pass or not
        :return: return code, num_fail_case or 10010 - parsing html file fail
        """
        try:

            with open(self.report_file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                ret = soup.select('tr#total_row td')
                # number of cases marked as fail or error
                num_fail_case = int(ret[3].text.strip()) + int(ret[4].text.strip())
                return num_fail_case

        except Exception as e:
            logger.error(e)
            return 10010


if __name__ == '__main__':
    obj_mail = SendMail(PROJECT_PATH + '/report/automation_test_report.html')
    obj_mail.send_email()
