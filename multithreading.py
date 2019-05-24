import requests
from bs4 import BeautifulSoup as bs
import time
import os
import threading
import urllib.parse
import urllib.request

from datetime import date, timedelta, datetime as dt
from selenium import webdriver as wd

# global variable
form_url = ''
login_url = 'https://nid.naver.com/nidlogin.login?mode=form'
ID = ''
PW = ''

# Logic
# MultiThreading
# 한번의 request를 통해 서버시간을 가져오고 그 시간을 스레드 끼리 공유하여 동작함

def getServerTime():
    serverDate = urllib.request.urlopen(form_url).headers['Date']
    datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
    return datetime_server

def submit(driver):
    driver.click()

def timeCheck():
    end = False
    while not end :
        tim = dt.now()
        serverTime = getServerTime()
        if serverTime.second>=59 and tim.microsecond>800000 :
            return True

def writeContents(driver):
    end = False;

def loadPage(driver):
    driver.get(form_url)

def login(driver, id, pw):
    driver.get(login_url)
    # send_keys 는 네이버 capcha에 의해 반드시 걸리기 때문에.. javascript로 로그인한다.
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(30)
    
def start_process(id, pw):
    # 크롬 드라이버 로딩
    options = wd.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = wd.Chrome(executable_path = './chromedriver',chrome_options=options)

    # 로직

    # 로그인
    # 폼 접속
    # 내용 작성
    # 시간 체크
    # 제출 버튼 클릭
    login(driver, id, pw)
    loadPage(driver)
    writeContents(driver)
    timeCheck()
    submit(driver)

if __name__=='__main__':
    t = threading.Thread(target=login, args=(ID,PW))
    t2 = threading.Thread(target=login, args=(ID,PW))
    t.start()
    t2.start()

    print("Main Thread")
