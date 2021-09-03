from selenium import webdriver

class WindowSwitching():


    def __init__(self,driver:webdriver.Chrome):
        self.drvier = driver

    def is_window_handle(self,name):
        self.pri = self.drvier.window_handles                       # 获取所有handle
        self.drvier.switch_to.window(
            self.pri[name])                                         # 切换到新的窗口 pri会打印出list数据，从0开始到负数）

