from main import streets
import pandas as pd, numpy as np

print()
print(streets)
columns = [f'{i}, д. {j}' for i in streets for j in range(1, 101)]
df = pd.DataFrame(np.random.randint (0, 100, size=(300, 300)), index = columns, columns = columns)
for item in columns:
    df.loc[item, item] = 0
for i in columns:
    for j in columns:
        df[i][j] = df[j][i]


print(df)