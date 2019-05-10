import ntplib
from time import ctime

def getNTPTime() :
    timeServer = "https://form.office.naver.com"
    c = ntplib.NTPClient()
    response = c.request(timeServer, version=3)
    return ctime(response.tx_time)

if __name__ == "__main__":
    print(getNTPTime())