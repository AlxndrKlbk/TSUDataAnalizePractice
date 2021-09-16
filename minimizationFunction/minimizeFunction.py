from scipy import optimize as opt
import math
import matplotlib

def function_for_minimize(x):
    return math.sin(x/5) * math.exp(x/10) + 5 * math.exp(-x/2)


minVal = opt.minimize(function_for_minimize, 2)
print(f'результат работы функции minimize для начальной точки = 2: \n', minVal, f"\n {'-'*10}")

minVal = opt.minimize(function_for_minimize, 30)
print(f'результат работы функции minimize для начальной точки = 30: \n', minVal, f"\n {'-'*10}")
