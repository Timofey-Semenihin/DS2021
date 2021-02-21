# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

temp = os.path.abspath("popcorn.csv")
data = pd.read_csv( filepath_or_buffer = temp, sep="\s+" )
data = pd.DataFrame(data)

#Pot
x = data.loc[data["Pot"]==1]["Count"].tolist()
y = data.loc[data["Pot"]==2]["Count"].tolist()
z = data.loc[data["Pot"]==3]["Count"].tolist()
print( stats.kruskal(x,y,z) )

#Oil
x = data.loc[data["Oil"]==1]["Count"].tolist()
y = data.loc[data["Oil"]==2]["Count"].tolist()
print( stats.kruskal(x,y) )
