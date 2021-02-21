import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


X = stats.norm.rvs(0,2,size=1000)
U = stats.norm.rvs(0,2,size=1000)

print('Pearson')
#######Pearson
#a)
F = 2*X+5+U
print( stats.pearsonr(F,X)[1] )
#b)
F = abs(abs(X)-1)+U
print( stats.pearsonr(F,X)[1] )
#c)
F = np.sin(X)+U
print( stats.pearsonr(F,X)[1] )
#######

print('Spearman')
#######Spearman
#a)
F = 2*X+5+U
print( stats.spearmanr(F,X).pvalue )
#b)
F = abs(abs(X)-1)+U
print( stats.spearmanr(F,X).pvalue )
#c)
F = np.sin(X)+U
print( stats.spearmanr(F,X).pvalue )
#######

print('Kendall')
#######Kendall
#a)
F = 2*X+5+U
print( stats.kendalltau(F,X).pvalue )
#b)
F = abs(abs(X)-1)+U
print( stats.kendalltau(F,X).pvalue )
#c)
F = np.sin(X)+U
print( stats.kendalltau(F,X).pvalue )
#######

# print('MGC')
# #######MGC
# #a)
# F = 2*X+5+U
# print( stats.multiscale_graphcorr(F,X).pvalue )
# #b)
# F = abs(abs(X)-1)+U
# print( stats.multiscale_graphcorr(F,X).pvalue )
# #c)
# F = np.sin(X)+U
# print( stats.multiscale_graphcorr(F,X).pvalue )
# #######
