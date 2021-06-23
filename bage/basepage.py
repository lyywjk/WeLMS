from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage():
    _base_url=""
    def __init__(self,driver_basepage:WebDriver=None):
        if driver_basepage==None:
            #复用浏览器，减少重复多余的步骤
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()
        else:
            self.driver=driver_basepage

        if self._base_url !="":
            #self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)
    #优化self.driver.find_element(by=by,value=value)
    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)

    def find_click(self,by,value):
        return self.driver.find_element(by=by,value=value).click()








