# -*- coding: utf-8 -*-
from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chrome():
    options = Options()
    options.add_argument('disable-infobars')
    chromedriver = '../../driver/chromedriver'
    driver = webdriver.Chrome(chromedriver, chrome_options=options)
    return driver


def headless():
        options = Options()
        options.add_argument('disable-infobars')
        options.add_argument('--headless')  # 无界面模式
        options.add_argument('--disable-gpu')
        chromedriver = '../../driver/chromedriver'
        return webdriver.Chrome(chromedriver, chrome_options=options)


def remote():
    host = '127.0.0.1:4444'  # 运行主机：端口号（本机默认：127.0.0.1:4444）
    dc = {'browserName': 'chrome'}  # 指定浏览器
    driver = Remote(command_execute='http://' + host + '/wd/hub', desired_capabilities=dc)
    return driver


# 用于测试该脚本是否有效
if __name__ == '__main__':
    dr = headless()
    dr.get('http://www.baidu.com')
    print dr.title
    dr.quit()
