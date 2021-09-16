import pandas as pd
# from sys import path

dataFile = open("csv_data.txt", "r", encoding="UTF-8")

print(dataFile)
frame = pd.read_csv(dataFile, sep="\t", header=0, encoding="UTF-8")

print(frame)
print("Имена столбцов: ", frame.columns)

new_line = {"фио": "person5", "курс": 1, "группа": 2, "анализ данных": 4, "статистика": 5}
# frame.append(new_line, ignore_index=True)
frame = frame.append(new_line, ignore_index=True)

print(frame)
