from page.thesaurus_tool_page import ThesaurusToolPage
from page.login_page import LoginPage
from common.route import Route
from selenium import webdriver
from common.logger import Log

import unittest,ddt

toolname = [
    {"input":"连衣裙","text":"0连衣裙"}
]

@ddt.ddt
class TestToolThesaurus(unittest.TestCase):
    logger = Log("TestToolThesaurus").get_log()

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = LoginPage(cls.driver)
        cls.tur = ThesaurusToolPage(cls.driver)
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

    @ddt.data(*toolname)
    def test_thesaurus_A(self,data):
        '''
        TOP20w下载，查询测试用例
        :param data:
        :return:
        '''
        self.tur.ls_tool_thesaurus(data["input"])
        t = self.tur.ls_thesaurus_text(
            data["text"])
        print("TOP20w结果：",t)
        if True == t:
            self.logger.info("TOP20w查询成功")
            self.assertTrue(t)
        else:
            self.logger.info("TOP20w查询失败")

if __name__ == "__main__":
    unittest.main()