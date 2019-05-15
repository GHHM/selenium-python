import requests
from bs4 import BeautifulSoup as bs
import time
import os
import threading

# Logic
# MultiThreading
# 한번의 request를 통해 서버시간을 가져오고 그 시간을 스레드 끼리 공유하여 동작함

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread" , total)


def start_process():


if __name__=='__main__':
    t = threading.Thread(target=sum, args=(1,600000))
    t2 = threading.Thread(target=sum, args=(2,40000))
    t.start()
    t2.start()

    print("Main Thread")
