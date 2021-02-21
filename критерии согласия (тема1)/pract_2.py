import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from math import log

data = np.loadtxt("Rainfall.txt", delimiter='\t', dtype=np.float)
logdata = [log(i) for i in data]

stats.kstest(data, 'expon', args = ([1/np.mean(data)]) )
stats.kstest(logdata, 'norm', args=(np.mean(logdata),np.sqrt(np.var(logdata))))



#graphical
fig1,ax1 = plt.subplots(figsize=(18, 12), dpi=400)
fig1 = qqplot(data, stats.expon(1/np.mean(data)), line='r',ax=ax1)

fig2,ax2 = plt.subplots(figsize=(18, 12), dpi=400)
fig2 = qqplot(np.array(logdata), stats.norm(np.mean(logdata),np.sqrt(np.var(logdata))), line='r',ax=ax2)