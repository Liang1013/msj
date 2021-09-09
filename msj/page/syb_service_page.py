from common.base import Base
from common.window_switching import WindowSwitching

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

class SybServerPage(Base):

    '''定位当前窗口事件'''
    syb_btn = ("css selector",".main_width>div:nth-child(4)>div:nth-child(2)>p:nth-child(1)")

    '''定位页面滑动事件'''
    location = ("css selector",".main_width>div:nth-child(3)>div:nth-child(2)>div:nth-child(2)>p:nth-child(5)")

    '''定位新窗口事件'''
    purchase_bth = ("css selector",".sku-form-info>div>button>span")
    purchase_text = ("css selector",".sku-form-info>div>div:nth-child(9)>div")


    def ls_syb_server(self):
        self.is_scroll_element(self.location)       #定位滑动界面
        self.is_cilck(self.syb_btn)
        WindowSwitching(self.driver)\
            .is_window_handle(-1)                   #切换handle
        self.is_cilck(self.purchase_bth)


    def ls_syb_text(self,text):
        return self.is_text_element(
            self.purchase_text,text)