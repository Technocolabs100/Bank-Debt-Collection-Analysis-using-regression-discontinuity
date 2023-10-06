from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("bank_data.csv")

a=df.head()
print(a)

plt.scatter(x=df['expected_recovery_amount'], y=df['age'], c="g" , s=2)
plt.xlim(0,2000)
plt.ylim(0.60)
plt.xlabel("Excepted Recovery Amount")
plt.ylabel("Age")
plt.legend(loc=2)
a1=plt.show()
print(a1)
