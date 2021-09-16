import pandas as pd

my_series = pd.Series(["a", "b", "c", "d", "f"])

print(my_series)
print(type(my_series))
print(my_series.index)
print(f'В серии хранятся значения: {my_series.values} \n'
      f'данные хранятся в объекте: {type(my_series.values)}')
