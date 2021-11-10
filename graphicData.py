!pip3 install pandas
!pip3 install matplotlib
!pip3 install scipy
!pip3 install seaborn

import requests
import pandas as pd
import numpy as np
from numpy import sqrt
from pandas import *
from matplotlib import pyplot
from pandas.plotting import *
import scipy.stats as stats
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set(style='whitegrid', palette='colorblind')

response = requests.get('http://192.168.0.2:5000/olympics')
data = pd.read_json(response.text)

data.head(10)

data.groupby('continent')['continent'].count().plot(kind='bar',color='blue',figsize=(10,5))
pyplot.show()

corr = data.corr('spearman')
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = pyplot.subplots(figsize=(8, 6))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, vmax=1,square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax, annot=True)
pyplot.show()
pyplot.close()