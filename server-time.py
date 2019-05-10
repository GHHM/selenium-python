import urllib.request
from datetime import date, timedelta, datetime as dt
import time
 
url = "https://form.office.naver.com/form/responseView.cmd?formkey=MGNjNjIxN2UtZmJiYy00ZmM4LWFlNGUtMTVlMmQ3ZTNkMDVh&sourceId=urlshare"

serverDate = urllib.request.urlopen(url).headers['Date']
print('서버시간: ',serverDate)

#타임스탬프 바꾸기
#timestamp = (time.mktime(time.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')))

datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
datetime_local = dt.now()

print((datetime_local.second-datetime_server.second))

while True:
    serverDate = urllib.request.urlopen(url).headers['Date']
    datetime_server = dt.strptime(serverDate, '%a, %d %b %Y %H:%M:%S %Z')
    print('서버시간: ',datetime_server)
    time.sleep(0.1)

print('로컬시간: ',datetime_local)

#print(type(date-serverDate), '초')

