import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
import csv

from sklearn.linear_model import LinearRegression

from sklearn.datasets import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

__author__ = 'Sampei and Sara'
__version__ = '0.0.1'

def get_data(file_path):
    '''Takes a given CSV file and creates a dictionary with country names as keys
    and a list of a given statistic starting from 1960 in a list'''
    country_dict = dict()
    indicator_list = []
    data = pd.read_csv(file_path)
    data = pd.DataFrame(data)
    data = data.astype(object).where(pd.notnull(data),None)
    for index, row in data.iterrows():
        to_add = []
        for i in row[1:]:
            to_add.append(i)
        indicator_list.append(to_add)
    for index, row in data.iterrows():
        country_dict[row["Country Name"]] = indicator_list[index]
    return country_dict

if __name__ == "__main__":
    gdp_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/gdp.csv'
    gdp_dict = get_data(gdp_file)
    # gini_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/gini.csv'
    # gini_dict = get_data(gini_file)
    # life_exp_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/life_expectancy.csv'
    # life_exp_dict = get_data(life_exp_file)
    # population_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/population.csv'
    # population_dict = get_data(population_file)
    print(gdp_dict)
