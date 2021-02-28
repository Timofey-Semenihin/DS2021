# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sn

temp = os.path.abspath("babies1.csv")
data = pd.read_csv( filepath_or_buffer = temp, sep="\s+" )
data = pd.DataFrame(data)

fig = plt.subplots(figsize=(18, 12), dpi=400)
heatmap = sn.heatmap(data.pcorr(), center=0, cmap='gist_ncar')