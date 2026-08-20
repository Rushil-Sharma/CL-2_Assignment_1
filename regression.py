import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("word_statistics.csv")

# Information content predictor
X1 = sm.add_constant(df["information_content"])
y = df["length"]

model_ic = sm.OLS(y, X1).fit()

# Frequency predictor
X2 = sm.add_constant(df["frequency"])

model_freq = sm.OLS(y, X2).fit()

print("===== INFORMATION CONTENT MODEL =====")
print(model_ic.summary())

print("\n===== FREQUENCY MODEL =====")
print(model_freq.summary())

print("\nInformation Content R²:", model_ic.rsquared)
print("Frequency R²:", model_freq.rsquared)
