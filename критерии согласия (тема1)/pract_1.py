import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from math import log

p = [log(1+1/k , 10) for k in range(1,10) ]
N = 9
f = []
fib1 = fib2 = 1
n = 100
if n < 2:
    quit()

f.append(fib1)
f.append(fib2)
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    f.append(fib2)

nu = np.zeros(10)
ff = [int(str(abs(f[i]))[0]) for i in range(n)]
for k in range(1,10):
    for i in range(n):
        if ff[i]==k:
            nu[k] = nu[k] + 1
nu = nu.tolist()
del nu[0]
t = sum( [ (nu[i]-N*p[i])**2/N/p[i] for i in range(9)] )

print(stats.chi2.ppf(0.6,t))