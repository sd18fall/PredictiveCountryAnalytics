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
#     def __init__(self, gdp, unemp, life_expectancy, population):
#         self.gdp = gdp
#         self.unemp = unemp
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
    '''Generates a clean dictionary with no None values'''
    indicator_dict = clean_data(get_data(file_path))
    return indicator_dict

def get_year(year,gdp_dict,unemp_dict,life_exp_dict,population_dict):
    '''Takes in dictionaries for all indicators and returns a dictionary with
    countries as keys and a list of indicators for that year as the value.'''
    year_dict = dict()
    for country in gdp_dict:
        year_dict[country] = [gdp_dict[country][year-1960], unemp_dict[country][year-1960], life_exp_dict[country][year-1960], population_dict[country][year-1960]]
    return year_dict

def get_output(year_dict, gdp_weight, unemp_weight, life_exp_weight, population_weight):
    '''Takes in a dictionary with countries as keys and a list of indicators as
    values and returns the same dictionary with a calculated coefficient as the
    first value of the list.'''
    total_weight = gdp_weight + unemp_weight + life_exp_weight + population_weight
    gdp_weight = gdp_weight/total_weight
    unemp_weight = unemp_weight/total_weight
    life_exp_weight = life_exp_weight/total_weight
    population_weight = population_weight/total_weight
    all_gdp = []
    all_unemp = []
    all_life_exp = []
    all_pop = []
    for country in year_dict:
        all_gdp.append(year_dict[country][0])
        all_unemp.append(year_dict[country][1])
        all_life_exp.append(year_dict[country][2])
        all_pop.append(year_dict[country][3])
    while None in all_gdp:
        all_gdp.remove(None)
    while None in all_unemp:
        all_unemp.remove(None)
    while None in all_life_exp:
        all_life_exp.remove(None)
    while None in all_pop:
        all_pop.remove(None)
    gdp_max = max(all_gdp)
    gdp_min = min(all_gdp)
    unemp_max = max(all_unemp)
    unemp_min = min(all_unemp)
    life_exp_max = max(all_life_exp)
    life_exp_min = min(all_life_exp)
    pop_max = max(all_pop)
    pop_min = min(all_pop)
    coef_dict = dict()
    for country in year_dict:
        if None not in year_dict[country]:
            weighted_gdp = gdp_weight*(year_dict[country][0]/gdp_max)
            weighted_unemp = unemp_weight*((100-year_dict[country][1])/unemp_max)
            weighted_life_exp = life_exp_weight*(year_dict[country][2]/life_exp_max)
            weighted_pop = population_weight*(year_dict[country][3]/pop_max)
            coef = weighted_gdp + weighted_unemp + weighted_life_exp + weighted_pop
        else:
            coef = None
        coef_dict[country] = coef
    return coef_dict

if __name__ == "__main__":
    # Data to display and calculate coefficients which contains None values
    gdp_dict = get_data('Datasets/gdp.csv')
    unemp_dict = get_data('Datasets/unemployment.csv')
    life_exp_dict = get_data('Datasets/life_expectancy.csv')
    population_dict = get_data('Datasets/population.csv')
    # Data to run linear regression which contains no None values
    gdp_dict_clean = clean_dict('Datasets/gdp.csv')
    unemp_dict_clean = clean_dict('Datasets/unemployment.csv')
    life_exp_dict_clean = clean_dict('Datasets/life_expectancy.csv')
    population_dict_clean = clean_dict('Datasets/population.csv')
    # Generate a dictionary of display values
    year_2016 = get_year(2016,gdp_dict,unemp_dict,life_exp_dict,population_dict)
    print(get_output(year_2016,100,25,25,25))
