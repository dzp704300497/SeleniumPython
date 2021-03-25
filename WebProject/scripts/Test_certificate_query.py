import time
from page.Page import Page_obj
import unittest
import ddt
import logging
from log.loging import Logger
from util.excel_util import ExcelUtil
from log.usr_log import UsrLog
ex = ExcelUtil()
excel_data = ex.row_data()




@ddt.ddt
class Test_certificate_query(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("""""""""""""""""setUpClass""""""""""""""""")
        self.page_obj = Page_obj.certificatequery(self)

    def tearDown(self):
        self.page_obj.backo()
        print("""""""""""""""""teardown""""""""""""""""")


    @ddt.data(*excel_data)
    def test_001(self,excel_data):
        name_text, bianhao_text, yz_text, asser = excel_data

        self.page_obj.certificate_query(name_text=name_text,bianhao_text=bianhao_text,yz_text=yz_text)

        data = self.page_obj.alert_data()
        assert asser == data
if __name__ == '__main__':
    unittest.main()
