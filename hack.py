import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(20,15))

bs = pd.read_csv('medlog.csv')

b_s_l = plt.scatter(bs['Date'], bs['Blood Glucose Level'], c='b', alpha=0.75)


plt.xlabel('Date')
plt.ylabel('Blood Suagr Level')
plt.title('Blood Sugar Level for March')
plt.show()
