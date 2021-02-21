import numpy as np
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors
import matplotlib.pyplot as plt

x = stats.norm.rvs(0, 10, size = 100)
print( stats.kstest( x, 'norm', args=(np.mean(x),np.sqrt(np.var(x))) ) )
print( lilliefors(x, dist='norm') )

p_ks, p_l = [], []
for i in range(1000):
    x = stats.norm.rvs(0, 10, size = 100)
    p_ks.append(stats.kstest( x, 'norm', args=(np.mean(x),np.sqrt(np.var(x))) )[1])
    p_l.append(lilliefors(x, dist='norm')[1])

X = np.linspace(0,1,1000)
p_ks, p_l = sorted(p_ks), sorted(p_l)
lab = ['ks','lilliefors']
fig = plt.subplots(figsize=(18, 12), dpi=400)
plt.plot(X, p_ks)
plt.plot(X, p_l)
plt.legend(lab)