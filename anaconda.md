# path 설정
* 윈도우 
1. 제어판 > 시스템 > 고급 시스템 설정 > 고급 > 환경변수
2. Path 클릭 후 '편집' 누르기
3. 파이썬 설치 경로 (ex. C:\ProgramData\Anaconda3\) 앞에 세미콜론 붙여서 추가

# Anaconda 
## Anaconda 관리자 권한 실행 
일부 라이브러리는 원한이 필요한 경우가 있다. 설치 안되면 귀찮다..

# Conda 가상환경 구성
`conda create -n 가상환경이름 python=파이썬버젼`
`conda create -n py36 python=3.6`

가상환경의 경로 : Anaconda3\envs\가상환경이름\ (ex. Anaconda3\envs\py36)

# 활성화
activate
`conda activate py36`

deactivate
`conda deactivate`