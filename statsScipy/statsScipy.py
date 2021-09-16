import numpy
from scipy import stats as sts
import matplotlib.pyplot as plt
import numpy as np

norm_rv = sts.norm(loc=2, scale=0.5)  # loc - матожидание, scale - среднеквадратичное отклонение
generatedVariates = norm_rv.rvs(size=10)   # rvs - random variates

x = numpy.linspace(0, 4 , 100)
fig, ax = plt.subplots(1, 1)

cdf = norm_rv.cdf(x)  # Cumulative Distribution Function

plt.plot(x, cdf)
plt.show()
print(generatedVariates)
print(norm_rv.cdf(3))
