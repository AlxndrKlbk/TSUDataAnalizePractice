import pandas as pd

# Пункт 1
dataFile = open("Ex24.txt", "r", encoding="UTF-8")
frame = pd.read_csv(dataFile, sep='\t', header=0, encoding="UTF-8")

# Пункт 2
print('Пункт 2:', '\n', frame.head(3), '\n')
print(frame.shape, '\n')

# Пункт 3
new_line = [{'ФИО': 'Васильев О.А.', 'Группа': 1, 'Зачетная книжка': 'не известно', 'Sub1': 3},
            {'ФИО': 'Ловцов А.Н', 'Группа': 3, 'Зачетная книжка': 'не известно', 'Sub2': 4, 'Sub3': 5, 'Sub4': 5}]
frame = frame.append(new_line, ignore_index=True)
print('Пункт 3:', '\n', frame, '\n')

# Пункт 4
frame = frame.fillna(2, inplace=False)
print('Пункт 4:', '\n', frame, '\n')

# Пункт 5
columnNames = frame.columns  # возвращает названия столбцов (заголовки)
subList = []  # список только предметов

for column in columnNames:
    if 'Sub' in str(column):
        subList.append(column)  
countLines = frame.shape[0]  # количество строчек

lineNumbers = list()  # массив с номерами строк
i = 0
for i in range(countLines):
    lineNumbers.append(i)

onlySub = frame.loc[lineNumbers, subList]

AverageMark = []
sumMark = 0  # суммарная оценка по ученику

for i in range(countLines):
    line = onlySub.iloc[i]
    for Sub in subList:
        sumMark += int(line[[Sub]])
    AverageMark.append(sumMark/len(subList))
    sumMark = 0
    
frame['Средний бал'] = AverageMark
print('Пункт 5:', '\n', frame, '\n')

# Пункт 6
print('Пункт 6:', '\n', frame.iloc[[0, 1, 2, 3, 4, 5, 6], [0, 7]], '\n')


# Пункт 7
print('Пункт 7:', '\n', frame[frame.Группа == 512], '\n')
print('Пункт 7:', '\n', frame[frame.Группа == 513], '\n')

# Пункт 8
AverageMarkColumn = frame[['Средний бал']]
DeleteFrame = frame

for i in range(countLines):
    line = AverageMarkColumn.iloc[i]
    mark = line[0]
    
    if float(mark) > 2:
        DeleteFrame = DeleteFrame.drop(i)

print('Пункт 8:', '\n', DeleteFrame, '\n')

# Пункт 9
zadolznik = frame

for i in range(countLines):
    line = frame.iloc[i]
    dolg = False
    
    for Sub in subList:
        if float(line[[Sub]]) == 2:
            dolg = True
            break
            
    if not dolg:
        zadolznik = zadolznik.drop(i)

print('Пункт 9:', '\n', zadolznik, '\n')

resultFile = open("result.txt", "w")
frame.to_csv(resultFile, sep="\t")
resultFile.close()
