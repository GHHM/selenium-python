import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import pandas as pd

file_path = "./data.csv"

df = pd.read_csv(file_path,index_col=0)


print(df)
# df = pd.DataFrame(totalfreq)
register_matplotlib_converters()
plt.figure(figsize=(20,10))
plt.xticks(rotation=90)
# plt.scatter(df.Date ,df.Frequency)
plt.plot(df.Date,df.Frequency)
plt.savefig('result.png')
plt.show()