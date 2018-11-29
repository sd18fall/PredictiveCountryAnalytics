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

def clean_data(x):
    '''Takes a dictionary with countries as keys and a list of indicators as a
    list. Modifies the list to a dictionary with the year as the key and the indicator
    as the value. Eliminates all None values.'''
    for country in x:
        clean_dict = dict()
        for year in range(len(x[country])):
            if x[country][year] != None:
                clean_dict[year + 1960] = x[country][year]
        x[country] = clean_dict
    return x

if __name__ == "__main__":
    gdp_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/gdp.csv'
    gdp_dict = get_data(gdp_file)
    gdp_dict = clean_data(gdp_dict)
    gini_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/gini.csv'
    gini_dict = get_data(gini_file)
    gini_dict = clean_data(gini_dict)
    life_exp_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/life_expectancy.csv'
    life_exp_dict = get_data(life_exp_file)
    life_exp_dict = clean_data(life_exp_dict)
    population_file = '/home/sampeiomichi/PredictiveCountryAnalytics/Machine Learning/Datasets/population.csv'
    population_dict = get_data(population_file)
    population_dict = clean_data(population_dict)
