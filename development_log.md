# 1. 개발 계기
ㄴㅇㅂ 폼으로 하는건 항상 실패해서.. 다계정으로 다른 시간에 제출할 수 있는 프로그램을 만들어보았다. 업무 시간을 제외하고 비는 시간에 틈틈히 만들고 있다.

# 2. 개발 과정

## 2.1 패키지 선정

많이 알려진 웹 크롤링 패키지로 beutifulsoup 이나 selenium이 있다.

Javascript link를 사용하는 웹사이트의 경우 높은 복잡도를 가지고 있고, 이 때 beautiful soup를 이용하기에 적합하지 않다. Selenium은 드라이버를 통해 웹 브라우저 위에서 동작하기 때문에 동적 상호작용을 할 수 있고 JavaScript link 또한 편리하게 접근할 수 있다. 속도는 selenium이 좀 느리다.

확장성을 생각해 selenium을 선택하였다.

## 2.2 개발 흐름

대략 생각해둔 개발 흐름은 다음과 같다.

1. 자동 로그인 (reqeust)
2. 폼 자동 작성 (selenium)
3. 서버 시간에 맞추어 제출 (time)

(+)
추가적으로 고려해야할 사항

- ㄴㅇㅂ의 경우 캡차 들의 자동화 로그인 방지 코드가 짜여져있다.
- 한 번에 여러 개 프로세스 실행.
- 폼에 따라 제약이 있는 경우가 있다. (아이디 별 1폼, ip별 1폼)
- web element를 동적으로 생성할 수 있을까? (해당 폼의 web element를 감지해 자동으로 생성할 수 있나)
- 클라우드

## 2.3 개발 진행

비교적 쉬운 작업부터 시작해 점차 심화하는 방식으로 개발하였다. 쉽다고 생각했던 부분도 잘 안되는 경우가 많아 시간을 많이 뺏겼다.

각 과정에서 발생한 문제와 원인, 해결방법에 대해서 기록하겠다.

### 로그인

먼저, 많이 알려져 있는 beautifulsoup 이나 selenium으로 xpath로 web element 가져와 입력하는 방법이 통하지 않았다.
delay를 주어도 캡차로 막히는걸 보면 아마 헤더에 python이 있어서 서버쪽에서 걷어내는 것 같다.

그래서 찾아낸 방법은 javascript로 실행하는 것이다.

```python
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
```

그리고 아래와 같이 로그인 후 바로 블로그에 이동하는 url을 이용하면 이동 후 어떤 동작도 먹히지 않는다.

`https://nid.naver.com/nidlogin.login?mode=form&url=https://blog.naver.com/example`

해결 방법은 간단했다.. 따로따로 페이지를 불러오면 된다.

`driver.get(https://nid.naver.com/nidlogin.login?mode=form)`

`driver.get(https://blog.naver.com/example)`

첫 번째 url로 이동한 블로그 페이지는 사용자 입장에서는 똑같이 동작하기 때문에 url이 문제일거라고는 생각도 못했었다. (xpath를 잘못 딴줄 알고 계속 고치고..)

### 지정된 시간에 submit 버튼 누르기

가장 핵심으로 생각한 부분은 로컬 컴퓨터와 서버 시간의 동기화였다.

검색해보니 여러 방법이 있었다.

1. 도메인 서버와 로컬 컴퓨터의 시간 동기화

도메인의 ip 주소를 알아내어 net 명령어를 이용해 windows time을 동기화 시켜주는 것이다.

2. 일정 시간 마다 서버 시간 받아오기

생각할 수 있는 가장 간단한 방법이다. 통신 cost가 크다는 것이 단점이다.


### 한 번에 여러 개의 프로세스 돌리기

멀티 프로세싱 vs 멀티 스레딩

통신을 최소화 하기 위해 리소스를 공유할 수 있는 멀티 스레딩을 선택하였다.


### 아이디/ip 변경

폼 제출에 아이디 당 하나, 혹은 ip당 하나 라는 제한이 걸려있어 다계정 제출을 위해서는 처리가 필요하다

아이디의 경우 간단하게 프로세스 별로 다른 인자값을 주면 되지만 ip 변경이 꽤 까다로운 문제였다.


1. 익명 브라우저 사용

https://wkdtjsgur100.github.io/selenium-change-ip/

2. fake user agent를 이용한 IP 변경


https://brunch.co.kr/@ueber/28

https://pymon.tistory.com/11