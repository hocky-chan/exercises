"""
通过selenium以模拟点击的方式在谷歌浏览器上爬取爬取京东商品评论
并将爬取结果保存至本地
https://github.com/hocky-chan/test
"""

import requests
import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
import csv

def drop_down():
    for x in range(1,12,2):
        sleep(1)
        j = x/9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
    #定义一个自动滚动的函数

try:
    driver.get('https://item.jd.com/100019125569.html#askAnswer')   #获取商品地址
    sleep(7)   #等待一段时间以保证网页加载完毕
    button = driver.find_element(By.XPATH,"//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")
    sleep(3)   #同上
    button.click()    #点击按钮跳转至评论页面

    with open ('京东.txt',mode='a',encoding='utf-8') as f:
        for n in range(99):
            drop_down()
            m = n + 1
            print('第%d页' %m)    #显示当前爬取页数
            sleep(5)
            user = driver.find_elements(By.XPATH,"//div[@class='user-info']")
            comment = driver.find_elements(By.XPATH,"//p[@class='comment-con']")
            other = driver.find_elements(By.XPATH,"//div[@class='order-info']")
            for i in range(len(user)):
                f.write(str(user[i].text))
                f.write(str(comment[i].text))
                f.write(str(other[i].text)\n)    #换行符是爬完之后才加的，感觉加了换行符爬取结果应该更整齐
            button2 =driver.find_element(By.CSS_SELECTOR,"#askAnswer > div.mc > div.askAnswer-list > div.ui-page-wrap.clearfix > div > a.ui-pager-next")
            sleep(1)
            button2.click()    #点击下一页按钮
            sleep(5)      #适当等待以免被京东反爬

finally:
    driver.quit
        #爬取完毕后自动关闭
