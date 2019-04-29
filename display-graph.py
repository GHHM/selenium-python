import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import pandas as pd

file_path = "./data.csv"

df = pd.read_csv(file_path,index_col=0)


print(df)
# df = pd.DataFrame(totalfreq)
register_matplotlib_converters()
plt.figure(figsize=(15,10))
plt.xticks(rotation=90)
# plt.scatter(df.Date ,df.Frequency)
plt.bar(df.Date,df.Frequency) # 막대 그래프
plt.scatter(df.Date,df.Frequency) # 산점도 그래프
plt.plot(df.Date,df.Frequency, color='green') # 선그래프
plt.title('Crawling Result') # 제목 추가
plt.savefig('result.png') # 이미지로 저장
plt.show()