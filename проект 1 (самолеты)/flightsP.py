import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors

data = pd.read_excel("project1.xlsx" )
data = pd.DataFrame(data)


#models
x = data.loc[data["Модель"]==1]["Дальность"].tolist()
y = data.loc[data["Модель"]==2]["Дальность"].tolist()
z = data.loc[data["Модель"]==3]["Дальность"].tolist()
print( stats.kruskal(x,y,z) )
print( stats.f_oneway(x,y,z) )
print( stats.anderson_ksamp([x,y,z]) )

#угол
x = data.loc[(data["Угол запуска"]==0) & (data["Модель"]==1)]["Дальность"].tolist()
y = data.loc[(data["Угол запуска"]==30) & (data["Модель"]==1)]["Дальность"].tolist()
print( stats.kruskal(x,y) )
print( stats.f_oneway(x,y) )
print( stats.anderson_ksamp([x,y]) )

#Высота
x = data.loc[data["Запускающий"]==1]["Дальность"].tolist()
y = data.loc[data["Запускающий"]==2]["Дальность"].tolist()
z = data.loc[data["Запускающий"]==3]["Дальность"].tolist()
j = data.loc[data["Запускающий"]==4]["Дальность"].tolist()
print( stats.kruskal(x,y,z,j) )
print( stats.f_oneway(x,y,z,j) )
print( stats.anderson_ksamp([x,y,z,j]) )

x = data.loc[data["Модель"]==1]["Дальность"].tolist()
print( lilliefors(x, dist='norm') )

