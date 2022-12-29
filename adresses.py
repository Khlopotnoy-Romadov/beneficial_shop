import pandas as pd

df = pd.read_csv('C:\\Users\\dafin\\OneDrive\\Рабочий стол\\address.csv')
df.index=df.columns
print(df)
