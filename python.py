import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import statsmodels.api as sm
import nasdaqdatalink as nasdaq

# WTI Crude Oil price from the US Department of Energy:
df_gdp = nasdaq.get("FRED/GDP")
df_oil = nasdaq.get("EIA/PET_RWTC_D")
df = df_gdp.join(df_oil, lsuffix='GDP', rsuffix='OIL', how="inner")

# Export data to csv-file at specified path
pth = os.getcwd()
pd.DataFrame.to_csv(df, pth + "/Data.csv")

# Import data from csv-file at specified path
files = pd.Series(os.listdir(os.getcwd()))
csv_files = files[files.str.contains('csv')]
df = pd.read_csv(os.getcwd() + "/" + csv_files.to_string(index=False))

# Data manipulation
df.describe()  # Descriptives
df.rename(columns={'ValueGDP': 'GDP', 'ValueOIL': 'OIL'}, inplace=True)  # Renaming
df['pct_GDP'] = df['GDP'].pct_change() * 100
df['pct_OIL'] = df['OIL'].pct_change() * 100
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Plot using matplotlib 3.5.3
plt.title('GDP vs. Oil price growth', fontweight="bold")
plt.ylabel('Percentage')
plt.plot(df['pct_GDP'], color='Blue', label='GDP %')
plt.plot(df['pct_OIL'], color='Red', label='Oil %')
plt.legend()
plt.savefig(pth + '/GDP_Oil_chart.png')

# Linear modelling
y = df['pct_OIL'].dropna()
x = sm.add_constant(df['pct_GDP']).dropna()
lm = sm.OLS(y, x).fit()
print(lm.summary())
fit = lm.fittedvalues

plt.title('Predicted Oil price %-change based on GDP growth', fontweight='bold')
plt.plot(y, color='Black', label='Actual')
plt.plot(fit, '.', color='Blue', label='Predicted')
plt.legend()
plt.savefig('Model.png')

