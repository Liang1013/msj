from page.thesaurus_tool_page import ThesaurusToolPage
from page.login_page import LoginPage
from common.route import Route
from selenium import webdriver

import unittest,ddt

toolname = [
    {"input":"连衣裙","text":"0连衣裙"}
]

@ddt.ddt
class TestToolThesaurus(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = LoginPage(cls.driver)
        cls.tur = ThesaurusToolPage(cls.driver)
        cls.log.ls_login()

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
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()