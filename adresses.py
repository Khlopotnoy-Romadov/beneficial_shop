from data import streets
import pandas as pd, numpy as np, random

print()
print(streets)
columns = [f'{i}, д. {j}' if j>=10 else f'{i}, д. 0{j}' for i in streets for j in range(1, 101)]
df = pd.DataFrame(0, index = columns, columns = columns)
count = 0
for i in columns:
    df[i] = [abs((j-count)*30)+random.randint(-15,15) for j in range(len(columns))]
    df.loc[i, i] = 0
    count+=1

print(df)
# print(df.loc[columns[298:300],columns[0:2]])
# print(df.loc[columns[0:2],columns[298:300]])
