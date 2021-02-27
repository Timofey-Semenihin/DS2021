# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform


def distcorr(X, Y):

    X = np.atleast_1d(X)
    Y = np.atleast_1d(Y)
    if np.prod(X.shape) == len(X):
        X = X[:, None]
    if np.prod(Y.shape) == len(Y):
        Y = Y[:, None]
    X = np.atleast_2d(X)
    Y = np.atleast_2d(Y)
    n = X.shape[0]
    if Y.shape[0] != X.shape[0]:
        raise ValueError('Number of samples must match')
    a = squareform(pdist(X))
    b = squareform(pdist(Y))
    A = a - a.mean(axis=0)[None, :] - a.mean(axis=1)[:, None] + a.mean()
    B = b - b.mean(axis=0)[None, :] - b.mean(axis=1)[:, None] + b.mean()
    
    dcov2_xy = (A * B).sum()/float(n * n)
    dcov2_xx = (A * A).sum()/float(n * n)
    dcov2_yy = (B * B).sum()/float(n * n)
    dcor = np.sqrt(dcov2_xy)/np.sqrt(np.sqrt(dcov2_xx) * np.sqrt(dcov2_yy))
    return dcor

#################i
X, Y = [], []
x, y = stats.uniform.rvs(-1,2,100), stats.uniform.rvs(-1,2,100)
for i in range(np.size(x)):
    if ( np.sqrt(x[i]**2 + y[i]**2) <= 1 ) and ( np.sqrt(x[i]**2 + y[i]**2) >= 1/2 ):
        X.append(x[i])
        Y.append(y[i])

X, Y = np.array(X), np.array(Y)
print( stats.pearsonr(X,Y) )
print( stats.multiscale_graphcorr(X,Y).stat,stats.multiscale_graphcorr(X,Y).pvalue )
print( distcorr(X,Y) )

################ii
x, y = stats.uniform.rvs(-1,2,10), stats.uniform.rvs(-1,2,10)
print( stats.pearsonr(x,y) )
print( stats.multiscale_graphcorr(x,y).stat,stats.multiscale_graphcorr(x,y).pvalue )
print( distcorr(x,y) )

#################iii
X, Y = [], []
x, y = stats.uniform.rvs(-3/2,3,100), stats.uniform.rvs(-3/2,3,100)
for i in range(np.size(x)):
    if ( (x[i]+1)**2+(y[i]-1)**2 <= 1/4 ) or ( (x[i]-1)**2+(y[i]-1)**2 <= 1/4 ) or ( (x[i]+1)**2+(y[i]+1)**2 <= 1/4 ) or ( (x[i]-1)**2+(y[i]+1)**2 <= 1/4 ):
        X.append(x[i])
        Y.append(y[i])

X, Y = np.array(X), np.array(Y)
print( stats.pearsonr(X,Y) )
print( stats.multiscale_graphcorr(X,Y).stat,stats.multiscale_graphcorr(X,Y).pvalue )
print( distcorr(X,Y) )