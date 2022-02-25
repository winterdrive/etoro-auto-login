import requests as req
import urllib.request as req
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#from time import clock
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
from selenium.webdriver.chrome.options import Options
import pickle
import json

time.perf_counter()

#opts = Options()
#opts.add_argument('--headless')
#opts.add_argument("--incognito")  # 使用無痕模式。用 selenium開瀏覽器已經很乾淨了，但疑心病重的可以用一下
#proxy = "socks5://localhost:9050"
#opts.add_argument('--proxy-server={}'.format(proxy))  # 讓 selenium透過 tor訪問 internet
#opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
# 使用偽造的 user-agent

#opts.add_argument("--disable-blink-features")
#opts.add_argument("--disable-blink-features=AutomationControlled")

url="https://www.etoro.com/zh-tw/login"
PATH="C:/Users/123/Desktop/coding/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get(url)
#底下重頭戲
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"})
#useragnet似乎只能用cdp改才行
#請參考https://ithelp.ithome.com.tw/articles/10248972
#用opts.add_argument("user-agent=......")行不通
#不過貌似只能成功登入一兩次，之後就被擋了

def Login(Username,Password):
    username=driver.find_element_by_xpath('//*[@id="username"]')
    username.click()
    username.send_keys("%s"%Username)
    password=driver.find_element_by_xpath('//*[@id="password"]')
    password.click()
    password.send_keys("%s"%Password)
    login=driver.find_element_by_xpath("/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/button")
    
    login.click()
    time.sleep(5)

Login("XXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXX")

#cookie有效期，不要費時間抓了
#cookie = driver.get_cookies()
#with open('etoro.json', 'w') as f:
#    f.write(json.dumps(cookie))


#virtual=driver.find_element_by_css_selector("div.nav-top")
virtual=driver.find_element_by_xpath("/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[1]/a[2]")
#virtual=driver.find_element_by_xpath("/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[1]")
virtual.click()
time.sleep(2)
#real鈕
virtual_bottum=driver.find_element_by_xpath("/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[3]/div[2]/a")
virtual_bottum.click()
time.sleep(2)
#停在這裡了
#virtual profile鈕
virtual_confirm=driver.find_element_by_link_text('Switch to Virtual Portfolio')
virtual_confirm.click()
time.sleep(5)
#切換至虛擬倉

#切換至My Watchlist
my_watchlist=driver.find_element_by_xpath("/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[2]/nav/ul/li[2]/a/et-layout-sidenav-tooltip/span")
my_watchlist.click()


def Buy(a):#a=order no. in list
    buy=driver.find_element_by_xpath('/html/body/ui-layout/div/et-layout-main/div/div[2]/div[2]/div[3]/div/ng-view/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[%s]/et-instrument-row/et-instrument-trading-row/div/et-buy-sell-buttons/et-buy-sell-button[2]/div/div[1]'%a)
    buy.click()
    time.sleep(2)
    #不停不行啊
    close_button=driver.find_element_by_xpath('//*[@id="open-position-view"]/div[1]/div[2]')
    #print(close_button)
    close_button.click()
    time.sleep(2)
    #1 is spy #2 is tqqq #3 is swn #4 is gold

Buy(1)
Buy(2)
Buy(3)
Buy(4)
#讚 完成

##########################revised###############################

#driver.quit()

        

