import urllib.request
import datetime as dt
 
url = "https://blog.naver.com/musicaltalk/221533354110"

date = urllib.request.urlopen(url).headers['Date']
print(date)
 
time = int(time.mktime(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))
print(time)
