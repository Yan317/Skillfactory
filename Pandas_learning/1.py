import pandas as pd

data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
                 index=['Первый', "Второй", "Третий", "Четвёртый"])
print(data)

# print(data.loc[["Первый", "Третий"]])

data1 = pd.Series(list(range(10, 1001)))
print(data1.iloc[0])
