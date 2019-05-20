import requests
from bs4 import BeautifulSoup as bs
import time
import os
import threading

from selenium import webdriver as wd

# global variable
login_url = 'https://nid.naver.com/nidlogin.login?mode=form'
ID = ''
PW = ''

# Logic
# MultiThreading
# 한번의 request를 통해 서버시간을 가져오고 그 시간을 스레드 끼리 공유하여 동작함

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread" , total)

def login(id, pw):
    # 크롬 드라이버 로딩
    options = wd.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = wd.Chrome(executable_path = './chromedriver',chrome_options=options)

    driver.get(login_url)

    # send_keys 는 네이버 capcha에 의해 반드시 걸리기 때문에.. javascript로 로그인한다.
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(30)

def start_process():
    login('','')

if __name__=='__main__':
    t = threading.Thread(target=login, args=(ID,PW))
    t2 = threading.Thread(target=login, args=(ID,PW))
    t.start()
    t2.start()

    print("Main Thread")
