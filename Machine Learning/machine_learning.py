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

# class Country:
#     '''A country with lists of indictors and years'''
#     def __init__(self, gdp, gini, life_expectancy, population):
#         self.gdp = gdp
#         self.gini = gini
#         self.life_exp = life_expectancy
#         self.population = population

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
        for i in row[2:]:
            to_add.append(i)
        indicator_list.append(to_add)
    for index, row in data.iterrows():
        country_dict[row["Country Code"]] = indicator_list[index]
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

def clean_dict(file_path):
    indicator_dict = clean_data(get_data(file_path))
    return indicator_dict

def get_year(year,gdp_dict,gini_dict,life_exp_dict,population_dict):
    year_dict = dict()
    for country in gdp_dict:
        year_dict[country] = [gdp_dict[country][year-1960], gini_dict[country][year-1960], life_exp_dict[country][year-1960], population_dict[country][year-1960]]
    return year_dict

if __name__ == "__main__":
    # Data to display and calculate coefficients which contains None values
    gdp_dict = get_data('Datasets/gdp.csv')
    gini_dict = get_data('Datasets/gini.csv')
    life_exp_dict = get_data('Datasets/life_expectancy.csv')
    population_dict = get_data('Datasets/population.csv')
    # Data to run linear regression which contains no None values
    gdp_dict_clean = clean_dict('Datasets/gdp.csv')
    gini_dict_clean = clean_dict('Datasets/gini.csv')
    life_exp_dict_clean = clean_dict('Datasets/life_expectancy.csv')
    population_dict_clean = clean_dict('Datasets/population.csv')
