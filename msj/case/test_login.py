from selenium import webdriver
from common.route import Route
from page.login_page import LoginPage
from common.logger import Log

import unittest,ddt

ecl = Route().is_excel("log.xlsx")

url = "https://jcrmweb.maimiaotech.com/#/login"

@ddt.ddt
class TestLogin(unittest.TestCase):
    logger = Log('TestCase').get_log()

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.log = LoginPage(cls.driver)

    @classmethod
    def setUp(self) -> None:
        self.logger.info("----------开始执行测试用例----------")

    @classmethod
    def tearDown(self) -> None:
        self.logger.info("---------------pass--------------")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    def add_log(self,user,paw):
        self.log.ls_username(user)
        self.log.ls_password(paw)
        self.log.ls_btn()

    @ddt.data(*ecl)
    def test_login_A(self,data):
        '''msj登陆测试用例'''
        self.add_log(data["user"],data["paw"])
        t = self.log.ls_text_login(
            data["text"])
        print("登陆结果：",t)
        if True == t:
            self.assertTrue(t)
            self.logger.info("msj登陆成功")
        else:
            self.logger.info("msj登陆失败")

if __name__ == "__main__":
    unittest.main()