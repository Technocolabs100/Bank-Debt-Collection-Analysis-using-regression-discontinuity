from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df=pd.read_csv("bank_data.csv")

plt.scatter(x=df['expected_recovery_amount'], y=df['actual_recovery_amount'], c="g", s=2)
plt.xlim(900, 1100)
plt.ylim(0, 2000)
plt.xlabel("Expected Recovery Amount")
plt.ylabel("Actual Recovery Amount")
plt.legend(loc='upper left')
a1=plt.show()

#print(a1)
#print(a2)

