from page.login_page import LoginPage
from page.wang_tool_page import WangToolPage
from selenium import webdriver
from common.route import Route

import unittest,ddt

toolname = [
    {"name":"淘_旺商务","text":"淘_旺商务"}
]

@ddt.ddt
class TestToolWang(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = LoginPage(cls.driver)
        cls.tool = WangToolPage(cls.driver)
        cls.log.ls_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*toolname)
    def test_tool_A(self,data):
        '''旺旺照妖镜测试用例'''
        self.tool.ls_wang_tool(data["name"])
        t = self.tool.ls_tool_text(
            data["text"])
        print("旺旺照妖镜结果：",t)
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()