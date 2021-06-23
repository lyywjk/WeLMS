import json
import time

import allure
from selenium.webdriver.common.by import By

from bage.basepage import BasePage


@allure.feature("登录")
class Login(BasePage):
    _base_url = "http://192.168.9.31"
    @allure.step("登录成功")
    def login(self,login_id,password):
        #self.driver.get("http://192.168.9.31")

        with allure.step("老师"):
            # 下拉框
            self.find(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/form/div[1]/div/div/div/input').click()
            # 老师
            self.find(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        with allure.step("用户名"):
            # Login ID
            self.find(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/form/div[2]/div/div/input').send_keys(login_id)
        with allure.step("密码"):
            # password
            self.find(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/form/div[3]/div/div[1]/input').send_keys(
            password)
        # login
        self.find(By.XPATH, '//*[@class="el-button el-button--primary el-button--large"]').click()
        time.sleep(3)

        # # 获取到cookie
        # cookis = self.driver.get_cookies()
        # # 存放cookie
        # with open("/Users/lyy/pyth/WeLMS_PC/filess/cooki.json", "w") as f:
        #     json.dump(cookis, f)
        #
        # cookies = json.load(open("/Users/lyy/pyth/WeLMS_PC/filess/cooki.json", "r"))
        # for cook in cookies:
        #     self.driver.add_cookie(cook)
        # time.sleep(10)
        with allure.step("退出登录"):
            #点击用户名
            self.find_click(By.XPATH,'//*[@class="navOptions"]')
            #return Hom_one(self.driver)
            #点击退出登录
            self.find_click(By.XPATH,'//*[@class="navOptions"]//li[2]')

    # def test_cookie_login(self):
    #     cookies = json.load(open("/Users/lyy/pyth/WeLMS_PC/filess/cooki.json", "r"))
    #     for cook in cookies:
    #         self.driver.add_cookie(cook)
