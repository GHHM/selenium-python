import requests
from bs4 import BeautifulSoup as bs
import time
import os
from multiprocessing import Pool
# Logic
# MultiThreading
# 한번의 request를 통해 서버시간을 가져오고 그 시간을 스레드 끼리 공유하여 동작함

def get_content():
    abs_link = ''
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')

    print(soup.select('h1')[0].text)

def start_process():
    print('start process')
    get_content()

if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=3)
    pool.map(start_process)
    print("---%s seconds ---" %(time.time()-start_time))