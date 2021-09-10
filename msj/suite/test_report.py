from common import HTMLTestRunner
from common.route import Route
from common.sendmail import SendMail
import  unittest

def TestReport():

    '''
    :start_dir  获取用例路径
    :pattern  获取路径下的test格式测试用例
    :return:
    '''
    discover = unittest.defaultTestLoader.discover(start_dir=
                                                   Route().is_report("case"),
                                                   pattern="test*.py")

    '''
    :已二进制写入路径下
    '''
    reportpath = Route().is_report("report/")+"report.html"
    fg = open(reportpath, "wb")

    reunner = HTMLTestRunner.HTMLTestRunner(stream=fg,
                                            title="麦商机测试用例",
                                            description="自动化测试")
    '''运行'''
    reunner.run(discover)

    '''发送附件邮件'''
    smtp_receiver = ['123@163.com']
    m = SendMail(
        username='123@163.com', passwd='123456', recv=smtp_receiver,
        title='自动化测试报告', file=reportpath
    )
    m.send_mail()


if __name__ == "__main__":
    reportpath = Route().is_report("report/")+"report.html"
    print(reportpath)
