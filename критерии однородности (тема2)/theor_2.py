# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

A = [[5,5,5,5,5],[0,0,0,0,0.5], [(1+i)/10 for i in range(5)]]

#####ANOVA
for a in A:
    x = [stats.norm.rvs(a[i], 1, size=100) for i in range(5)]
    print( stats.f_oneway(x[0],x[1],x[2],x[3],x[4]) )


a = [0,0,0,0,0.5]
x = [stats.norm.rvs(a[i], 1, size=100) for i in range(4)]
x.append( stats.norm.rvs(a[4], 4, size=100) )
print( stats.f_oneway(x[0],x[1],x[2],x[3],x[4]) )
print(' ')

######Kruskal
for a in A:
    x = [stats.norm.rvs(a[i], 1, size=100) for i in range(5)]
    print( stats.kruskal(x[0],x[1],x[2],x[3],x[4]) )


a = [0,0,0,0,0.5]
x = [stats.norm.rvs(a[i], 1, size=100) for i in range(4)]
x.append( stats.norm.rvs(a[4], 4, size=100) )
print( stats.kruskal(x[0],x[1],x[2],x[3],x[4]) )