import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sn

temp = os.path.abspath("planes1.csv")
data = pd.read_csv( filepath_or_buffer = temp)
data = pd.DataFrame(data)
data = data.drop('i', 1)
                 
#models
x = data.loc[data["модель"]==1]["дальность"].tolist()
# y = data.loc[data["модель"]==2]["дальность"].tolist()
z = data.loc[data["модель"]==3]["дальность"].tolist()
print( stats.kruskal(x,z) )

d1 = pd.read_excel("project1_1.xlsx" )
d1 = pd.DataFrame(d1)
p = d1.loc[d1["Модель"]==3].loc[d1["Угол запуска"]==30]['Отклонение'] 
w = stats.norm.rvs(0, 0.3, size = 12)
w = [round(w[i],2) for i in range(12)]
pw = (p + w).tolist()
data.loc[ (data["Модель"]==3) & (data["Угол запуска"]==30 ), 'Отклонение'] = pw
data.to_excel('project1_2.xlsx')