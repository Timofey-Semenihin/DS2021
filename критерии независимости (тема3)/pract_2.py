# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sn

temp = os.path.abspath("televisions.csv")
data = pd.read_csv( filepath_or_buffer = temp, sep="\s+" )
data = pd.DataFrame(data)

fig1 = plt.subplots(figsize=(18, 18), dpi=170)
heatmap1 = sn.heatmap(data.loc[:, data.columns != 'Country'].pcorr(), center=0, cmap='gist_ncar',square=True)

fig2 = plt.subplots(figsize=(18, 18), dpi=170)
heatmap2 = sn.heatmap(data.loc[:, data.columns != 'Country'].corr(), center=0, cmap='gist_ncar',square=True)