import unittest
from util.HTMLTestRunner import HTMLTestRunner
class TestSuit_certificate_query():

    class test_suit():
        suit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover("../scripts","Test_baidu_unittest_001.py")
        print(discover)






        with open('../html/report.html', 'wb')as f:
            HTMLTestRunner(
                stream=f,           # 相当于f.write(报告)
                title='证书查询',
                description='None',
                verbosity=2         # 为每个测试用例生成测试报告
            ).run(suit)