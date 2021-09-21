# 1. Проанализировать полигон относительных частот (построен при выполнении задания 25).
# Сформулировать предположение о виде закона распределения генеральной совокупности.
# 2. Используя результаты выполнения задания 27, получить оценку параметра предполагаемого
# закона распределения (закона Пуассона) по методу моментов.
# 3. Построить многоугольник предполагаемого теоретического распределения на одном чертеже с
# полигоном относительных частот.
# 4. Выяснить, не противоречит ли имеющимся наблюдениям гипотеза о том, что число
# регистрируемых ежесекундно частиц имеет распределение Пуассона с параметром, подобранным по
# методу моментов; уровень значимости принять равным 0,1.


import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt


def sum_and_del(emp_massive, theory_massive):
    i = 0
    small_freq_index = np.where(emp_massive < 5)
    j = len(small_freq_index)
    while True:
        i = np.take(small_freq_index, 0)
        j = np.take(small_freq_index, -1)
        if np.size(small_freq_index) != 0:
            emp_massive[j-1] = emp_massive[j-1] + emp_massive[j]
            theory_massive[j-1] = theory_massive[j-1] + theory_massive[j]
            emp_massive = np.delete(emp_massive, j)
            theory_massive= np.delete(theory_massive, j)
            small_freq_index = np.delete(small_freq_index, np.where(small_freq_index == j))
        if np.size(small_freq_index) != 0:
            emp_massive[i+1] = emp_massive[i+1] + emp_massive[i]
            theory_massive[i+1] = theory_massive[i+1] + emp_massive[i]
            emp_massive = np.delete(emp_massive, i)
            theory_massive = np.delete(theory_massive, i)
            np.delete(small_freq_index, np.where(small_freq_index == i))

        small_freq_index = np.where(emp_massive < 5)

        if np.size(small_freq_index) == 0:
            break

    result = [emp_massive, theory_massive]
    return result


GeigerMassive = np.genfromtxt('Geiger.txt')[1:]

mean = np.mean(GeigerMassive)  # Среднее (мат.ожидание)
var = np.var(GeigerMassive)  # Выборочная дисперсия
n = len(GeigerMassive)

x_emp = np.unique(GeigerMassive, return_counts=True)
xi = x_emp[0]
ni = x_emp[1]
print(xi)
print(len(xi))

lamda = mean
x_theoretical = np.linspace(int(xi[0]), int(xi[len(xi) - 1]), int(xi[len(xi) - 1]) + 1)

poisson_rv = sts.poisson(lamda)
poissonProbability = poisson_rv.pmf(x_theoretical)

# Пункт 3
plt.plot(xi, ni / len(GeigerMassive), 'o-', color='orange', label='полигон частот')

plt.plot(x_theoretical, poissonProbability, 'o-', color='red', label='Распределение Пуассона')
plt.title('Полигон относительных частот и многоугольник распределения')
plt.ylabel('частоты $\omega_i$ \ вероятность p')
plt.xlabel('$варианты $x_i$ \ x$')
plt.legend()

# Пункт 4
alpha = 0.1  # уровень значимости (вероятность ошибки первого рода)

ni_theoretical = n * poisson_rv.pmf(xi)

print(f'До обработки: ni = {ni}, no_theoretical = {ni_theoretical}')

answer = sum_and_del(ni, ni_theoretical)
ni = answer[0]
ni_theoretical = answer[1]

print(f'После обработки: ni = {ni}, no_theoretical = {ni_theoretical}')

chi2_emp = sum((ni - ni_theoretical) ** 2 / ni_theoretical)  # эмпирическое значение критерия Пирса
print('Наблюдаемое значение', chi2_emp)

chi2_cr = sts.chi2.ppf(1 - alpha, len(ni) - 2)  # критическое значение критерия
print('Критическое значение ', chi2_cr)

print(f"хи2 = {chi2_emp} и хи2кр = {chi2_cr} ")
