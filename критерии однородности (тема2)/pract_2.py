# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

temp = os.path.abspath("taylor.csv")
data = pd.read_csv( filepath_or_buffer = temp, sep="\s+" )
data = pd.DataFrame(data)

x, y, Y = data['First'].tolist(), data['Second'].tolist(), []
for i in y:
    if i!='*':
        Y.append(i)

x, Y = [float(i) for i in x], [float(i) for i in Y]
print( stats.mannwhitneyu(x,Y) )
