from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.parse
import urllib.request
from datetime import date, timedelta, datetime as dt
import time

def getServerTime(form_url):
    serverDate = urllib.request.urlopen(form_url).headers['Date']
    datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
    return datetime_server

def getTimeDeff(form_url):
    serverDate = urllib.request.urlopen(form_url).headers['Date']
    datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
    datetime_local = dt.now()
    return (datetime_local.second-datetime_server.second)

# form.office.naver.com ip address
# 210.89.164.67

login_url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
form_url = 'https://form.office.naver.com/form/responseView.cmd?formkey=MGNjNjIxN2UtZmJiYy00ZmM4LWFlNGUtMTVlMmQ3ZTNkMDVh&sourceId=urlshare'

# open chromedriver
options = wd.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = wd.Chrome(executable_path='./chromedriver',chrome_options=options)

# open browser
driver.get(form_url)

# click button
btn1=driver.find_element_by_xpath('//*[@id="option_1"]/div[1]')

btn2 = driver.find_element_by_xpath('//*[@id="option_2"]/div[1]')

btn3 = driver.find_element_by_xpath('//*[@id="option_5"]/div[1]')

btn4 = driver.find_element_by_xpath('//*[@id="option_7"]/div[1]')

btn_submit = driver.find_element_by_class_name('submitBtn')

btn1.click()
btn2.click()
btn3.click()
btn4.click()


# logic: 현재 서버 시간을 가져와 local 시간과 차이를 계산하여 submit
# result: 
# 해당 시점에서 local과의 차이를 계산 후 실행하면
# 오랜 시간이 지난 후에는 n초 이상 차이가 벌어지기 때문에 좋은 방법이 아님.
#
# time_diff = getTimeDeff(form_url)
# end = False
# while not end : 
#     tim = dt.now()
#     if (tim.second+time_diff)>=59 and tim.microsecond>500000:
#         btn_submit.click()
#         end = True
#         print('local time : ',tim)
#         print('predicted server time : ', tim + timedelta(seconds = time_diff))
#         print('submit complete')
#     else:
#         time.sleep(0.1)

# logic: 0.1s 마다 서버로 request를 보냄
# 
end = False
while not end :
    tim = dt.now()
    datetime_server = getServerTime(form_url)
    if (datetime_server.second)>=59 and tim.microsecond>800000 :
        btn_submit.click()
        end = True
        print('local time : ',tim)
        print('predicted server time : ', datetime_server)
        print('submit complete')
    else:
        time.sleep(0.1)
        print(datetime_server)


# end = False
# while not end : 
#     tim = getServerTime(form_url)
#     if(tim.second>=59 and tim.microsecond>500000):
#          btn_submit.click()
#          end = True
#          print('local time : ',tim)
#          print('predicted server time : ', tim + timedelta(seconds = time_diff))
#          print('submit complete')
#     else :
#         time.sleep(0.1)
#         print(tim)
        


#btn_submit = driver.find_elements_by_name('제출하기')

# current system time

# dt = datetime.datetime.now()
# submit_time = datetime.datetime.fromtimestamp()

# b_1second = submit_time.timedelta(seconds=1)


driver.kill()



