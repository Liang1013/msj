from common import HTMLTestRunner
from common.route import Route
from common.report_email import ReportEmail
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
                                            title="msj测试用例",
                                            description="自动化测试")
    '''运行'''
    reunner.run(discover)

    '''发送邮件'''
    ReportEmail(reportpath)


if __name__ == "__main__":
    reportpath = Route().is_report("report/")+"report.html"
    print(reportpath)
