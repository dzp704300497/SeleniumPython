from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,url=None):
        self.driver = webdriver.Chrome()

        if url == None:
            self.url = "http://www.cnhsis.com.cn/xlcx.html"
        else:
            self.url = url

        self.driver.get(self.url)
    def __del__(self):
        self.driver.close()
        # self.driver.quit()


    def find_element(self,loc):
        try:
            return WebDriverWait(self.driver,10,1).until(
                lambda x:x.find_element(*loc)
            )
        except:
            return None


    def find_elements(self,loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(
                lambda x: x.find_elements(*loc)
            )
        except:
            return None

    def click_element(self,loc):
        el = self.find_element(loc)
        el.click()

    def input_element(self,loc,text):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(text)

    def swtich_alert(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            print(text)
            return text
        except:
            return None

    def back(self):
        try:
            self.driver.back()

        except:
            return None





    # 判断title是否为预期
    def decide_title(self,expect_title):
        title = ES.title_is(expect_title)
        return title(self.driver)



