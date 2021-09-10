from selenium import webdriver
from page.syb_service_page import SybServerPage
from page.login_page import LoginPage
from common.route import Route
from common.window_switching import WindowSwitching
from common.logger import Log

import unittest,ddt

sybname = [
    {"text":"请选择规格和周期"}
]

@ddt.ddt
class TestSybServer(unittest.TestCase):
    logger = Log("TestSybServer").get_log()

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = LoginPage(cls.driver)
        cls.syb = SybServerPage(cls.driver)
        cls.log.ls_login()

    @classmethod
    def setUp(self) -> None:
        self.logger.info("----------开始执行测试用例----------")

    @classmethod
    def tearDown(self) -> None:
        self.logger.info("---------------pass--------------")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*sybname)
    def test_syb_A(self,data):
        '''syb打开新窗口定位测试用例'''
        self.syb.ls_syb_server()
        t = self.syb.ls_syb_text(
            data["text"])
        print("syb结果：",t)
        if True == t:
            self.logger.info("syb执行成功")
            self.assertTrue(t)
        else:
            self.logger.info("syb执行失败")
        WindowSwitching(self.driver).is_window_handle(0)            #切换到当初界面
        self.syb.is_scroll_top()                                    #界面滑动到顶部

if __name__ == "__main__":
    unittest.main()