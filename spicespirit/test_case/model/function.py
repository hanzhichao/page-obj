# -*- coding: utf-8 -*-
from selenium import webdriver
import os

#截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    #print(base_dir)
    base_dir = str(base_dir)
    #print(base_dir)
    base_dir = base_dir.replace('\\','/')
    #print(base_dir)
    base = base_dir.split('/mail')[0]
    #print(base)
    file_path = base + '/mail/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)


#用于验证该脚本是否有效
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()

