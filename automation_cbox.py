from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.parse
import urllib.request
from datetime import date, timedelta, datetime as dt
import time

# 블로그 url
blog_url = 'https://blog.naver.com/musicaltalk/221540578065'

#https://nid.naver.com/nidlogin.login?mode=form&url=https://blog.naver.com/musicaltalk/221540578065
login_url = 'https://nid.naver.com/nidlogin.login?mode=form'

full_url = login_url + '&url=' + blog_url

# 크롬 드라이버 로딩
options = wd.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = wd.Chrome(executable_path = './chromedriver',chrome_options=options)

# 네이버 로그인
# send_keys 는 네이버 capcha에 의해서 반드시 걸리기 때문에.. javascript로 로그인한다.
driver.get(full_url)

driver.maximize_window()

id = ""
pw = ""

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.implicitly_wait(3)

# Scroll down
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 이거 안 먹는다.. 왜지 ??

# css selector로 해보기

driver.switch_to_frame("mainFrame")




