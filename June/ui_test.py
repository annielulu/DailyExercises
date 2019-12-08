# coding:utf-8
__author__ = 'annie'

from selenium import webdriver
import time

def startBrowser():
    # 打开浏览器
    driver = webdriver.Chrome()
    # 访问百度
    driver.get("http://www.baidu.com")
    # 窗口最大化
    driver.maximize_window()
    time.sleep(5)
    # 点击登录链接
    driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
    time.sleep(5)
    # 点击用户名登录
    # driver.find_element_by_class_name("tang-pass-footerBarULogin pass-link").click()
    # driver.find_elements_by_id("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
    driver.find_elements_by_id("TANGRAM__PSP_10__footerULoginBtn").click()

    # 输入用户名
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("15624958065")
    # 输入密码
    driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("love901226")
    # 点击登录按钮
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
    time.sleep(5)
    driver.close()


startBrowser()


