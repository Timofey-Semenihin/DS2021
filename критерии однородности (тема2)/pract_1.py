# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

temp = os.path.abspath("kidsfeet.csv")
data = pd.read_csv( filepath_or_buffer = temp, sep="\s+" )
data = pd.DataFrame(data)

#a)
print( stats.mannwhitneyu(data.loc[data["gender"]=='B']["length"],
                          data.loc[data["gender"]=='G']["length"]) )
#b)
print( stats.mannwhitneyu(data.loc[data["gender"]=='B']["width"],
                          data.loc[data["gender"]=='G']["width"]) )
#c)
print( stats.mannwhitneyu(data.loc[data["who"]=='L']["width"],
                          data.loc[data["who"]=='R']["width"]) )