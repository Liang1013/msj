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

url = "https://jcrmweb.maimiaotech.com/#/login"

class LoginPage(Base):

    '''登陆定位'''
    user = ("css selector",".content-container-form>form>div:nth-child(1)>div>div>span>input")
    paw = ("css selector",".content-container-form>form>div:nth-child(2)>div>div>span>input")
    btn = ("css selector",".registered-button")

    '''断言定位'''
    text_login = ("xpath","//*[@id='container']/section/header/div/div[3]/div/span[3]")

    def ls_username(self,username):
        self.is_send_keys(self.user,username)

    def ls_password(self,password):
        self.is_send_keys(self.paw,password)

    def ls_btn(self):
        self.is_cilck(self.btn)

    def ls_text_login(self,text):
        return self.is_text_element(self.text_login,text)

    def ls_login(self,user="17774007458",paw="liang971013"):
        self.driver.maximize_window()           #窗口最大化
        self.driver.get(url)                    #打开测试地址
        self.ls_username(user)
        self.ls_password(paw)
        self.ls_btn()