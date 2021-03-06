from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import Log

'''
Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''

class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.logger = Log(logger='Base').get_log()
        self.driver = driver
        self.times = 10
        self.t = 0.5

    def is_find_element(self,locater):
        '''
        封装WebDriverWait定位事件，
        :param locater: 0.5s查找一次，共10s，超过10s抛出异常
        :return:
        '''
        try:
            element = WebDriverWait(self.driver,self.times,self.t).until(lambda x: x.find_element(*locater))
            return element
        except:
            self.logger.error('%s 页面元素未能找到%s 元素' % (self,locater))


    def is_text_element(self,locator,text):
        '''
        封装断言
        :param locator:
        :param text:
        :return: 返回true成功，false失败
        '''
        try:
            element = WebDriverWait(self.driver,self.times,self.t
                                    ).until(EC.text_to_be_present_in_element(locator,text))
            return element
        except:
            self.logger.error('%s 页面元素未能找到%s 元素' % (self, locator))
            return False

    def is_send_keys(self,locater,text):
        '''封装输入框事件'''
        self.is_find_element(locater
                             ).send_keys(text)

    def is_cilck(self,locater):
        '''封装点击事件'''
        self.is_find_element(locater
                            ).click()

    def move_to_element(self,locater):
        '''封装封装鼠标悬浮'''
        ActionChains(self.driver).move_to_element(
            self.is_find_element(locater)).perform()

    def is_scroll_element(self,locater):
        '''通过定位，页面滑动到指定位置'''
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",self.is_find_element(locater))

    def is_scroll_top(self):
        '''页面滑动到顶部'''
        self.driver.execute_script(
            "window.scrollTo(0,0)")