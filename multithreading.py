import requests
import time
import os
import threading
import urllib.parse
import urllib.request

from datetime import date, timedelta, datetime as dt
from selenium import webdriver as wd

SUBMIT_SECOND = 59
MICRO_SECOND = 500000

# global variable
form_url = 'http://naver.me/G73wgGaT'
login_url = 'https://nid.naver.com/nidlogin.login?mode=form'
ID = '1111'
PW = '2222'

isSubmit = False
serverTime = ''

# Logic
# MultiThreading
# 한번의 request를 통해 서버시간을 가져오고 그 시간을 스레드 끼리 공유하여 동작함

def getServerTime():
    while not isSubmit: 
        serverDate = urllib.request.urlopen(form_url).headers['Date']
        datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
        global serverTime
        serverTime = datetime_server
        print(serverTime)
        time.sleep(0.1)
    #return datetime_server

def submit(driver,btnSubmit):
    btnSubmit.click()
    print("submit complete!")
    global isSubmit
    isSubmit = True

def timeCheck():
    end = False
    while not end :
        tim = dt.now()
        #serverTime = getServerTime()
        # 문제점 : 반을 SUBMIT_SECOND의 답을 못 받았을 경우 그냥 넘어감
        if serverTime.second>=SUBMIT_SECOND and tim.microsecond>MICRO_SECOND :
            print("Server Time : ", serverTime, "   Local Time: ",tim.microsecond)
            return True

def writeContents(driver):
    btn1=driver.find_element_by_xpath('//*[@id="option_1"]/div[1]')
    btn1.click()
    print("write contents complete!")

def loadPage(driver):
    driver.get(form_url)

# def login(driver, id, pw):
#     driver.get(login_url)
#     # send_keys 는 네이버 capcha에 의해 반드시 걸리기 때문에.. javascript로 로그인한다.
#     driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
#     driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
#     driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
#     time.sleep(30)
    
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

    #login(driver, id, pw)
    loadPage(driver)
    writeContents(driver)
    btnSubmit = driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]')
    timeCheck()
    submit(driver,btnSubmit)

if __name__=='__main__':
    t6 = threading.Thread(target=start_process, args=(ID,PW))
    t5 = threading.Thread(target=start_process, args=(ID,PW))
    t4 = threading.Thread(target=start_process, args=(ID,PW))
    t3 = threading.Thread(target=start_process, args=(ID,PW))
    t2 = threading.Thread(target=start_process, args=(ID,PW))
    t = threading.Thread(target=getServerTime,args=())

    t.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()