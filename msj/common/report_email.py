import smtplib # 导入smtplib模块
from email.mime.text import MIMEText
from email.header import Header

def ReportEmail(test_report):

    with open(test_report, 'r', encoding='utf-8') as f:

        mail_body = f.read()                                    # 打开测试报告，读取报告内容作为邮件内容
    sender = '*******************'                              # 发出邮箱
    receiver = ['*******************']                          # 接收邮箱
    mail_server = 'https://mail.163.com/'                       # 邮箱服务地址，这里以139邮箱为例
    subject = '自动化测试报告'                                     # 邮件标题
    username = '*******************'                            # 邮箱登录名
    passwd = '****************'                                 # 密码
    message = MIMEText(mail_body, 'html', 'utf-8')              # 设置邮件格式
    message['Subject'] = Header(subject, charset='utf-8')

    # 邮箱登录
    smtp = smtplib.SMTP()                                       # 实例化smtplib.SMTP()类对象
    smtp.connect("smtp.163.com")                                # 连接163邮件服务器
    smtp.login(username, passwd)                                # 登录

    # 发送邮件
    for i in receiver:
        smtp.sendmail(sender, i, message.as_string())
    smtp.quit()
