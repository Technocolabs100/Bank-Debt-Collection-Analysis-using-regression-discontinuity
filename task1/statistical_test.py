from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df=pd.read_csv("bank_data.csv")

#age vs expected recovery amount

era_900_1100 = df.loc[(df['expected_recovery_amount']<1100) & (df['excepted_recovery_amount']>=900)]

by_recovery_strategy=era_900_1100.groupby(['recovery_stratgey'])
'''
by_recovery_strategy['age'].describe().unstack()

level_0_age = era_900_1100.loc[df['recovery_stratgey']=="Level 0 Recovery"]['age']
level_1_age = era_900_1100.loc[df['recovery_stratgey']=="Level 1 Recovery"]['age']
a=stats.kruskal(level_0_age,level_1_age)
print(a)
from scipy import stats

# Compute average age just below and above the threshold
era_900_1100 = df.loc[(df['expected_recovery_amount']<1100) & 
                      (df['expected_recovery_amount']>=900)]
by_recovery_strategy = era_900_1100.groupby(['recovery_strategy'])
by_recovery_strategy['age'].describe().unstack()

# Perform Kruskal-Wallis test 
Level_0_age = era_900_1100.loc[df['recovery_strategy']=="Level 0 Recovery"]['age']
Level_1_age = era_900_1100.loc[df['recovery_strategy']=="Level 1 Recovery"]['age']
res=stats.kruskal(Level_0_age,Level_1_age)
print(res)
'''
#sex vs expected recovery amount
'''
crosstab = pd.crosstab(df.loc[(df['expected_recovery_amount']<1100) & (df['expected_recovery_amount']>=900)]['recovery_strategy'], df['sex'])
print(crosstab)

# Chi-square test
chi2_stat, p_val, dof, ex = stats.chi2_contingency(crosstab)
print(p_val)
'''
