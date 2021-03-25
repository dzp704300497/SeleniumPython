from base.Base import Base
import page
class CertificateQuery(Base):

    def __init__(self):
        url = "http://www.cnhsis.com.cn/xlcx.html"
        Base.__init__(self,url=url)


    def send_name(self,name_text):
        self.input_element(page.txtRealName,text=name_text)

    def send_bianhao(self,bianhao_text):
        self.input_element(page.txtBianHao,text=bianhao_text)

    def send_yz(self,yz_text):
        self.input_element(page.yz,text=yz_text)

    def click_bt(self):
        self.click_element(page.button)

    def alert_data(self):
        return self.swtich_alert()

    def backo(self):
        self.back()



    def certificate_query(self,name_text,bianhao_text,yz_text):
        # 输入姓名
        self.send_name(name_text)
        # 输入证书编号
        self.send_bianhao(bianhao_text)
        # 输入验证码
        self.send_yz(yz_text)
        # 点击查询按钮
        self.click_bt()
