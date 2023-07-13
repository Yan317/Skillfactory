import pandas as pd

data1 = pd.Series(list(range(10, 1001)))
print(data1.iloc[0])

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)