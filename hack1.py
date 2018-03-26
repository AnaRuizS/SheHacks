import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

plt.figure(figsize=(20,15))

bs = pd.read_csv('meds.csv')


x = np.array([datetime.datetime(2018, 3, 1, i, 0) for i in range(24)])
y = bs['Blood Glucose Level'].values


print(x.shape)
print(y.shape)


plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Blood Sugar Level')
plt.title('Blood Sugar Level for March')
plt.show()
