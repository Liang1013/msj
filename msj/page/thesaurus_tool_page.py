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

class ThesaurusToolPage(Base):

     '''进入工具定位'''
     title = ("xpath","//*[@id='container']/section/header/div/div[2]/div[4]/span")
     menu_title = ("xpath","//*[@id='container']/section/header/div/div[2]/div[8]/div[4]/div/div[2]/div/div")

     '''词库下载定位'''
     cl_click = ("css selector",".table-container>div:nth-child(2)>div:nth-child(4)>span:nth-child(3)")
     cl_click_bth = ("css selector",".table-container>div:nth-child(2)>div:nth-child(1)>span")

     '''跳转词库定位'''
     font = ("css selector",".g-flex-dol>div:nth-child(2)>div:nth-child(1)>span")

     '''查询关键词定位'''
     ant_input = ("css selector",".ant-input")
     bth = ("css selector",".search-button")

     '''断言定位'''
     input_text = ("css selector",".list-table>div:nth-child(11)>div>label>span:nth-child(2)>span")

     def ls_tool_thesaurus(self,text):
         self.move_to_element(self.title)
         self.is_cilck(self.menu_title)
         self.is_cilck(self.cl_click)
         self.is_cilck(self.cl_click_bth)
         self.is_scroll_element(self.font)
         self.is_send_keys(self.ant_input,text)
         self.is_cilck(self.bth)

     def ls_thesaurus_text(self,text):
         return self.is_text_element(self.input_text,text)