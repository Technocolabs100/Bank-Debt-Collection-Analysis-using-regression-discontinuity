import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv("bank_data.csv")
'''
#no threshold
era_900_1100 = df[(df['expected_recovery_amount'] < 1100) & (df['expected_recovery_amount'] >= 900)]
X = era_900_1100['expected_recovery_amount']
y = era_900_1100['actual_recovery_amount']
X = sm.add_constant(X) 

# Build linear regression model
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print(model.summary())
'''
#adding true threshold
df['indicator_1000'] = np.where(df['expected_recovery_amount']<1000, 0, 1)
era_900_1100 = df.loc[(df['expected_recovery_amount']<1100) & 
                      (df['expected_recovery_amount']>=900)]

X = era_900_1100[['expected_recovery_amount','indicator_1000']]
y = era_900_1100['actual_recovery_amount']
X = sm.add_constant(X)

model = sm.OLS(y,X).fit()
print(model.summary())

#adjusting the window
# Redefine era_950_1050 so the indicator variable is included

era_950_1050 = df.loc[(df['expected_recovery_amount']<1050) & 
                      (df['expected_recovery_amount']>=950)]

X = era_950_1050[['expected_recovery_amount','indicator_1000']]
y = era_950_1050['actual_recovery_amount']
X = sm.add_constant(X)

model = sm.OLS(y,X).fit()

model.summary()

