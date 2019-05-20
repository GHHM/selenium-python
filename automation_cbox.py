from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.parse
import urllib.request
from datetime import date, timedelta, datetime as dt
import time

# 블로그 url
# https://nid.naver.com/nidlogin.login?mode=form&url=https://blog.naver.com/musicaltalk/221540578065
blog_url = 'https://blog.naver.com/musicaltalk/221540578065'
login_url = 'https://nid.naver.com/nidlogin.login?mode=form'
full_url = login_url + '&url=' + blog_url

# 크롬 드라이버 로딩
options = wd.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = wd.Chrome(executable_path = './chromedriver',chrome_options=options)

# 함수 정의

# 네이버 로그인
def login(id, pw):
    # send_keys 는 네이버 capcha에 의해 반드시 걸리기 때문에.. javascript로 로그인한다.
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(2)

driver.get(login_url)

login('id','pw')

driver.get(blog_url)

# Scroll down
# 아래처럼 로그인 후 바로 블로그로 이동하는 url의 경우 scroll down이 되지 않음
# https://nid.naver.com/nidlogin.login?mode=form&url=https://blog.naver.com/musicaltalk/221540578065
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# TODO
# 댓글 클릭 후 작성

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

driver.close()