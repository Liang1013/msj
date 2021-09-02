from common.base import Base

'''
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''

class WangToolPage(Base):

    title = ("css selector",".header_nav>div:nth-child(2)>span")
    menu_title = ("css selector",".header_nav>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(1)>div>span")

    input_name = ("css selector",".ant-input")
    bth = ("css selector",".ant-btn")

    text_name = ("xpath",
                 "//*[@id='container']/section/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[2]")

    def ls_wang_tool(self,text):
        self.move_to_element(self.title)
        self.is_cilck(self.menu_title)
        self.is_send_keys(self.input_name,text)
        self.is_cilck(self.bth)

    def ls_tool_text(self,text):
        return self.is_text_element(self.text_name,text)
