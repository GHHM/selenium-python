from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.parse
import datetime as dt
import time

# form.office.naver.com ip address
# 210.89.164.67

form_url = 'https://form.office.naver.com/form/responseView.cmd?formkey=MGNjNjIxN2UtZmJiYy00ZmM4LWFlNGUtMTVlMmQ3ZTNkMDVh&sourceId=urlshare'

options = wd.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = wd.Chrome(executable_path='./chromedriver',chrome_options=options)

driver.get(form_url)

btn1=driver.find_element_by_xpath('//*[@id="option_1"]/div[1]')

btn2 = driver.find_element_by_xpath('//*[@id="option_2"]/div[1]')

btn3 = driver.find_element_by_xpath('//*[@id="option_5"]/div[1]')

btn4 = driver.find_element_by_xpath('//*[@id="option_7"]/div[1]')

btn_submit = driver.find_element_by_class_name('submitBtn')

btn1.click()
btn2.click()
btn3.click()
btn4.click()

end = False
while not end : 
    tim = dt.datetime.now()
    if tim.second>=59 and tim.microsecond>500000:
        btn_submit.click()
        end = True
        print(tim)
        print('submit complete')
    else:
        time.sleep(0.1)
        print(tim)


#btn_submit = driver.find_elements_by_name('제출하기')

# current system time

# dt = datetime.datetime.now()
# submit_time = datetime.datetime.fromtimestamp()

# b_1second = submit_time.timedelta(seconds=1)


driver.kill()