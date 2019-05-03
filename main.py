from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from IPython.display import display
import datetime as dt
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import urllib.parse

twitter_base_url = 'https://twitter.com/'
twitter_reg_url = 'https://twitter.com/signup'
twitter_login_url ='https://twitter.com/login'
default_user_id = ""
default_user_pw = ""

file_path = "./data.csv"

# headless option
options = wd.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = wd.Chrome(executable_path='./chromedriver',chrome_options=options)

# 암시적 대기
driver.implicitly_wait(3)

# 로그인

driver.get(twitter_login_url)
# id_elem = driver.find_element_by_name('session[username_or_email]')
# pw_elem = driver.find_element_by_name('session[password]')
login_btn = driver.find_elements_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button[@type="submit"]')
driver.implicitly_wait(3)
username_field= driver.find_element_by_class_name("js-username-field")
password_field = driver.find_element_by_class_name("js-password-field")

username_field.send_keys(default_user_id)
driver.implicitly_wait(1)

password_field.send_keys(default_user_pw)
driver.implicitly_wait(1)

password_field.submit()

# 기간
startdate = dt.date(year=2019,month=3,day=1)
untildate = dt.date(year=2019,month=3,day=2)
enddate = dt.date(year=2019,month=4, day=29)

# 키워드
# 한국어가 있을경우 urlib.parse 해줘야함
keyword = urllib.parse.quote_plus("한국")

# 검색 url
search_url='https://twitter.com/search?q="+str(keyword)+"%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=ko'

totalfreq = []
tweet_bag = []

while not enddate==startdate:
    url='https://twitter.com/search?q='+keyword+'%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=ko'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        dailyfreq = {'Date':startdate}
        wordfreq=0
        tweets=soup.find_all("p",{"class":"TweetTextSize"})
        wordfreq+=len(tweets)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        newHeight = driver.execute_script("return document.body.scrollHeight")
        print(newHeight)
        if newHeight != lastHeight:
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')
            tweets = soup.find_all("p",{"class":"TweetTextSize"})
            wordfreq = len(tweets)
        else:
            dailyfreq['Frequency']=wordfreq
            wordfreq=0
            totalfreq.append(dailyfreq)
            print(startdate)
            startdate = untildate
            untildate += dt.timedelta(days=1)
            dailyfreq={}
            break
        lastHeight = newHeight

print('end')

df = pd.DataFrame(totalfreq)

df.to_csv(file_path,mode="w")

display(df)
register_matplotlib_converters()
plt.figure(figsize=(20,10))
plt.xticks(rotation=90)
plt.scatter(df.Date ,df.Frequency)
plt.show()