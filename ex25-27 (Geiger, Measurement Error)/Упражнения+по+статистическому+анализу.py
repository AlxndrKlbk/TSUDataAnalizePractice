import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt
import math


def emp_cdf(sample, x):
    sample = np.sort(sample)  # сортировка выборки по возрастанию
    return np.searchsorted(sample, x, side='right') / sample.size   # определение значения функции по определению


fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 14))

GeigerMassive = np.genfromtxt('Geiger.txt')[1:]
print(GeigerMassive)

sample_counter = np.unique(GeigerMassive, return_counts=True)
print(sample_counter)
value = sample_counter[0]
frequency = sample_counter[1]

#  Полигон частот
axes[0].plot(value, frequency, 'o-')
axes[0].set_title("Полигон частот")
axes[0].set_ylabel('частоты $n_i$')
axes[0].set_xlabel('варианты $value_i$, частиц/сек')

#  Относительные частоты
sample_size = len(GeigerMassive)
rel_frequency = frequency/sample_size  # n(i)/n

axes[1].plot(value, rel_frequency, 'o-')
axes[1].set_title("Полигон относительных частот")
axes[1].set_ylabel('относительные частоты $n_i$')
axes[1].set_xlabel('варианты $value_i$, частиц/сек')

#  Эмпирическая функция распределения
value = np.sort(value)  # сортировка выборки по возрастанию
accumProb = emp_cdf(GeigerMassive, value)  # Накопленная вероятность


axes[2].step(value, accumProb, 'o-', color='purple')
axes[2].set_title("Эмпирическая функция распределения ")
axes[2].set_ylabel('Накопленная вероятность')
axes[2].set_xlabel('Показания счетчика Гейгера')

fig.show()
# ### Задание 26
#  Импортировать из файла Angle_error.txt данные о результатах испытаний, проведенных с целью оценки
#  точности прибора для измерения угла, определяющего высоту наблюдаемого объекта над горизонтом.
#  В файле содержатся значения ошибки, зафиксированной в 500 измерениях (в тысячных долях радиана).
#  Преобразовать столбец значений в массив numpy. Построить гисторамму относительных частот и график
#  эмпирической функции распределения (на разных графиках).


AngleErrorMassive = np.genfromtxt('Angle_error.txt ')[1:]

#  fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 14))

sample_counter = np.unique(AngleErrorMassive, return_counts=True)
value = sample_counter[0]
frequency = sample_counter[1]

# Определение оптимального количества частичных интервалов по правилу Стёрджесса
k = 1+int(math.log2(AngleErrorMassive.size))

#  Гистограмма частот
axes[0].hist(AngleErrorMassive, bins=k)
axes[0].set_title("Гистограмма частот")
axes[0].set_ylabel('Частота')
axes[0].set_xlabel('Диапазон значений')

# Построение гистограммы относительных частот
axes[1].hist(AngleErrorMassive, bins=k, density=True, color='green')
axes[1].set_title("Гистограмма относительных частот")
axes[1].set_ylabel('Относительная частота')
axes[1].set_xlabel('Диапазон значений')

#  Эмпирическая функция распределения
value = np.sort(value)  # сортировка выборки по возрастанию
accumProb = emp_cdf(AngleErrorMassive, value)  # Накопленная вероятность

axes[2].plot(value, accumProb, color='orange')
axes[2].set_title("Эмпирическая функция распределения ")
axes[2].set_ylabel('Накопленная вероятность')
axes[2].set_xlabel('Ошибка при замере угла')

fig.show()

# ### Задание 27
# 1. Для выборок, сформированных при выполнении заданий 25 и 26, найти оценки показателей среднего: выборочные
# средние и медианы. Для выборки из задания 25 найти также моду.
# 2. Для обеих выборок найти выборочную и исправленную дисперсию, выборочное и испраленное среднее
# квадратичное отклонение.
# 3. Для обеих выборок с надежностью $\gamma=0.95$ построить доверительный интервал для среднего значения
# генеральной совокупности. Построение выполнить двумя способами.

#  Пункт 1
#  Счетчик Гейгера
print('Пункт 1', '\n')
print('Счетчик Гейгера:')
print('Выборочная средняя показаний счетчика Гейгера равна: ', np.mean(GeigerMassive))
print('Медиана показаний счетчика Гейгера равна: ', np.median(GeigerMassive))
print('Значение моды: ', sts.mode(GeigerMassive)[0])
print('Модальная частота: ', sts.mode(GeigerMassive)[1])
print('\n')


#  Ошибки при измерении угла
print('Ошибки при измерении угла:')
print('Выборочная средняя показаний ошибок при измерении угла равна: ', np.mean(AngleErrorMassive))
print('Медиана показаний ошибок при измерении угла равна: ', np.median(AngleErrorMassive))
print('\n')

#  Пункт 2
#  Счетчик Гейгера
print('Пункт 2', '\n')
print('Счетчик Гейгера:')
print('Выборочная дисперсия показаний счетчика Гейгера равна: ', np.var(GeigerMassive))
print('Исправленная дисперсия показаний счетчика Гейгера равна: ', np.var(GeigerMassive, ddof=1))
print('Выборочное среднее квадратическое отклонение показаний счетчика Гейгера равно: ', np.std(GeigerMassive))
print('Исправленное среднее квадратическое отклонение показаний счетчика Гейгера равно:', np.std(GeigerMassive, ddof=1))

print('\n')

#  Ошибки при измерении угла
print('Ошибки при измерении угла:')
print('Выборочная дисперсия показаний ошибок при измерении угла равна: ', np.var(AngleErrorMassive))
print('Исправленная дисперсия показаний ошибок при измерении угла равна: ', np.var(AngleErrorMassive, ddof=1))
print('Выборочное среднее квадратическое отклонение показаний ошибок при измерении угла равно: ',
      np.std(AngleErrorMassive))
print('Исправленное среднее квадратическое отклонение показаний ошибок при измерении угла равно:',
      np.std(AngleErrorMassive, ddof=1))

#  Пункт 3
gamma = 0.95  # надежность(доверительная вероятность)

#  Счетчик Гейгера
print('Пункт 3', '\n')
print('Счетчик Гейгера')
loc = np.mean(GeigerMassive)  # Сохранение выборочной средней
scale = np.std(GeigerMassive, ddof=1)/(GeigerMassive.size**0.5)  # Оценка среднего квадратичного отклонения распределения Стьюдента
t_rv = sts.t(df=GeigerMassive.size-1)  # создание случайной величины, имеющей распределение Стьюдента с n-1 степенью свободы
delta = t_rv.ppf((gamma+1)/2)*scale  # определение точности оценки
left = loc - delta   # левый конец доверительного интервала
right = loc + delta   # правый конец доверительного интервала
print('Левый конец ', left)
print('Правый конец ', right)

# Определение границ доверительного интервала вторым способом
inter = sts.t.interval(gamma, df = GeigerMassive.size-1, loc=loc, scale=scale)
print('Доверительный интервал вторым способом: ')
print('Левый конец ', inter[0])
print('Правый конец ', inter[1], '\n')

#Ошибки при измерении угла
print('Ошибки при измерении угла')
loc = np.mean(AngleErrorMassive) # Сохранение выборочной средней
scale = np.std(AngleErrorMassive, ddof=1)/(AngleErrorMassive.size**0.5)  # Оценка среднего квадратичного отклонения распределения Стьюдента
t_rv = sts.t(df=AngleErrorMassive.size-1)  # создание случайной величины, имеющей распределение Стьюдента с n-1 степенью свободы
delta = t_rv.ppf((gamma+1)/2)*scale  # определение точности оценки
left = loc - delta   # левый конец доверительного интервала
right = loc + delta   # правый конец доверительного интервала
print('Левый конец ', left)
print('Правый конец ', right)

# Определение границ доверительного интервала вторым способом
inter = sts.t.interval(gamma, df = AngleErrorMassive.size-1, loc=loc, scale=scale)
print('Доверительный интервал вторым способом: ')
print('Левый конец ', inter[0])
print('Правый конец ', inter[1])
