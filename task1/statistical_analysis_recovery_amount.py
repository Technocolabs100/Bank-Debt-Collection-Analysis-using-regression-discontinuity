from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("bank_data.csv")
era_900_1100 = df.loc[(df['expected_recovery_amount'] < 1100) & (df['expected_recovery_amount'] >= 900)]
by_recovery_strategy = era_900_1100.groupby(['recovery_strategy'])

print(by_recovery_strategy['actual_recovery_amount'].describe().unstack())

# Perform Kruskal-Wallis test
Level_0_actual = era_900_1100.loc[era_900_1100['recovery_strategy'] == 'Level 0 Recovery']['actual_recovery_amount']
Level_1_actual = era_900_1100.loc[era_900_1100['recovery_strategy'] == 'Level 1 Recovery']['actual_recovery_amount']
kruskal_result = stats.kruskal(Level_0_actual, Level_1_actual)
print("Kruskal-Wallis Test Result (900-1100):", kruskal_result)

# Repeat for a smaller range of $950 to $1050
era_950_1050 = df.loc[(df['expected_recovery_amount'] < 1050) & (df['expected_recovery_amount'] >= 950)]
Level_0_actual = era_950_1050.loc[era_950_1050['recovery_strategy'] == 'Level 0 Recovery']['actual_recovery_amount']
Level_1_actual = era_950_1050.loc[era_950_1050['recovery_strategy'] == 'Level 1 Recovery']['actual_recovery_amount']
kruskal_result_950_1050 = stats.kruskal(Level_0_actual, Level_1_actual)
print("Kruskal-Wallis Test Result (950-1050):", kruskal_result_950_1050)
