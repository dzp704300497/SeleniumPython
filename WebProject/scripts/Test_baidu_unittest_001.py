import sys,os
sys.path.append("/Users/duanzhanpeng/PycharmProjects/WebProject")

import unittest
import time
import ddt
from page.Page import Page_obj
from util.excel_util import ExcelUtil
from log.usr_log import UsrLog


e = ExcelUtil()
excel_data = e.row_data()

@ddt.ddt
class Test_certificate_query(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.page_obj = Page_obj().certificatequery()
        # self.log = UsrLog().get_log()

    def tearDown(self):
        self.page_obj.backo()

    @ddt.data(*excel_data)
    def test_certificate_query(self,excel_data):
        name_text, bianhao_text, yz_text, expect_data = excel_data
        # self.log.debug("11111111111")
        self.page_obj.certificate_query(name_text=name_text,bianhao_text=bianhao_text,yz_text=yz_text)
        data = self.page_obj.alert_data()
        self.assertEqual(data,expect_data)


if __name__ == '__main__':
    unittest.main()