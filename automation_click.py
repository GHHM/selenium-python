import time
import pyautogui
import datetime as dt

endhope=False
while not endhope:
    tim=dt.datetime.now()
    if tim.second>=59 and tim.microsecond>600000:
        pyautogui.click(1301,722)
        endhope=True
        print(tim)
    else:
        time.sleep(0.1)
        print(tim)