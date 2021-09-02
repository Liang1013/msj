from common.excelutil import ExcelUtil

import os

class Route():

    '''封装查找路径方法'''

    def is_route(self):
        garderpath = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件父级目录
        garder = os.path.dirname(garderpath)  # 获取父目录的父目录
        paths = "/data/chromedriver"

        return garder+paths

    def is_excel(self,file):
        # 调取excel表数据
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath,"data",file)
        data = ExcelUtil(filepath)

        return data.dict_data()


    def is_report(self,locater):
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath,locater)

        return filepath