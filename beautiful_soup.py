import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin, quote

from IPython.display import Image

# #
# 네이버 웹툰 이미지 다운
# #

# URl 소스 : https://image-comic.pstatic.net/webtoon/718020/33/20190507143410_c1fd5ebb0d38abd9b41d9aba3ac34e13_IMAG01_4.jpg
# 귀곡의 문 : 33화 의문점

image_url = 'https://image-comic.pstatic.net/webtoon/718020/33/20190507143410_c1fd5ebb0d38abd9b41d9aba3ac34e13_IMAG01_4.jpg'

headers = {'Referer' : "https://comic.naver.com/webtoon/detail.nhn?titleId=718020&no=33&weekend=wed" }

response = requests.get(image_url, headers=headers)
print(response) #200 = 성공
image_data = response.content
filename = os.path.basename(image_url)

with open(filename, 'wb') as f :
    print("writing to {} {} bytes" .format(filename, len(image_data)))
    f.write(image_data)


# #
# 
# #