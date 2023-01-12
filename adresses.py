import pandas as pd

df = pd.read_csv('address.csv')
df.index=df.columns
print(df)
