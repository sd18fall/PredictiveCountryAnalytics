import numpy as np
import pandas as pd
import os
import math

from sklearn import linear_model

__author__ = 'Sampei and Sara'
__version__ = '0.0.1'

class Country:
    '''A country with linear regression data for all indicators'''
    def __init__(self, m_gdp, b_gdp, m_unemp, b_unemp, m_life_exp, b_life_exp, m_pop, b_pop):
        self.m_gdp = m_gdp
        self.b_gdp = b_gdp
        self.m_unemp = m_unemp
        self.b_unemp = b_unemp
        self.m_life_exp = m_life_exp
        self.b_life_exp = b_life_exp
        self.m_pop = m_pop
        self.b_pop = b_pop

def get_data(file_path):
    '''Takes a given CSV file and creates a dictionary with country names as keys
    and a list of a given statistic starting from 1960 in a list'''
    country_dict = dict()
    indicator_list = []
    data = pd.read_csv(file_path)
    data = pd.DataFrame(data)
    data = data.astype(object).where(pd.notnull(data),None)
    # Ask Peter how to change None to NA
    for index, row in data.iterrows():
        to_add = []
        for i in row[2:]:
            to_add.append(i)
        indicator_list.append(to_add)
    for index, row in data.iterrows():
        country_dict[row["Country Name"]] = indicator_list[index]
    return country_dict

# Data for Machine Learning
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

def build_lr(indicator_dict):
    lr_dict = dict()
    for country in indicator_dict:
        indicator = indicator_dict[country]
        if indicator != {}:
            year_list = list(indicator.keys())
            year_list_final = []
            for year in year_list:
                year_list_final.append([year])
            indicator_list = list(indicator.values())
            reg = linear_model.LinearRegression()
            reg.fit(year_list_final,indicator_list)
            m = reg.coef_[0]
            b = reg.intercept_
            lr_dict[country] = [m,b]
        else:
            m = None
            b = None
            lr_dict[country] = [m,b]
    return lr_dict

# Data for Output
def populate_data(indicator_dict, lr_dict):
    for country in indicator_dict:
        for year in range(0,len(indicator_dict[country])):
            pred_indicator = None
            if indicator_dict[country][year] == None and lr_dict[country][0] != None and lr_dict[country][0] > 0:
                pred_indicator = lr_dict[country][0]*(year+1960) + lr_dict[country][1]
            if pred_indicator is not None:
                if pred_indicator > 0:
                    indicator_dict[country][year] = pred_indicator
    return indicator_dict

def get_year(year,gdp_dict,unemp_dict,life_exp_dict,population_dict):
    '''Takes in dictionaries for all indicators and returns a dictionary with
    countries as keys and a list of indicators for that year as the value. Also
    populates data using built linear regression model.'''
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
    to_display = []
    for country in year_dict:
        if None not in year_dict[country]:
            weighted_gdp = gdp_weight*(year_dict[country][0]/gdp_max)
            weighted_unemp = unemp_weight*((100-year_dict[country][1])/unemp_max)
            weighted_life_exp = life_exp_weight*(year_dict[country][2]/life_exp_max)
            weighted_pop = population_weight*(year_dict[country][3]/pop_max)
            coef = weighted_gdp + weighted_unemp + weighted_life_exp + weighted_pop
        else:
            coef = 0
        to_display.append([country,coef])
    return to_display


def get_display(year,gdp_dict,unemp_dict,life_exp_dict,population_dict,gdp_weight,unemp_weight,life_exp_weight,population_weight):
    year_dict = get_year(year, gdp_dict, unemp_dict, life_exp_dict, population_dict)
    display = get_output(year_dict, gdp_weight, unemp_weight, life_exp_weight, population_weight)
    return display

def search_country(country, year_dict):
    return year_dict[country]
