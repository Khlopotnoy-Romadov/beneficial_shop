from data import streets
import pandas as pd, numpy as np, random

print(streets)
columns = [f'{i}, д. {j}' if j>=10 else f'{i}, д. 0{j}' for i in streets for j in range(1, 101)]
df = pd.DataFrame(0, index = columns, columns = columns)
count = 0
for i in columns:
    df[i] = [abs((j-count)*30)+random.randint(-15,15) for j in range(len(columns))]
    df.loc[i, i] = 0
    count+=1

for i in range(len(columns)):
    for j in range(i+1, len(columns)):
        df[columns[i]][columns[j]] = df[columns[j]][columns[i]]


print(df)
#print(df.loc[columns[296:298],columns[10:12]])
#print(df.loc[columns[10:12],columns[296:298]])

df1 = pd.read_csv('address.csv')
print(df1)
