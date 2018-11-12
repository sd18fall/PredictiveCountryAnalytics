import numpy as np
import pandas as pd
import math
import csv
import matplotlib.pyplot as plt

from sklearn.datasets import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# f = open('/home/sampeiomichi/PredictiveCountryAnalytics/Datasets/gdp.csv')
#
# country_gdp = dict()
#
# csv_f = csv.reader(f)
#
# for row in csv_f:
#     item = row[0]
#     print(item)
#     print(type(item))
#
# f.close()

data = pd.read_csv('/home/sampeiomichi/PredictiveCountryAnalytics/Datasets/gdp_test.csv')
data.head()
data.shape
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='Year', y='US', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='Year', y='Japan', ax=axs[1])
data.plot(kind='scatter', x='Year', y='China', ax=axs[2])
plt.show()
