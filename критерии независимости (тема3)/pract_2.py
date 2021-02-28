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

fig1 = plt.subplots(figsize=(18, 12), dpi=400)
heatmap1 = sn.heatmap(data.pcorr(), center=0, cmap='gist_ncar')

fig2 = plt.subplots(figsize=(18, 12), dpi=400)
heatmap2 = sn.heatmap(data.corr(), center=0, cmap='gist_ncar')