"""A simple "Hello, World" application using Flask."""

from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField, PasswordField
from machine_learning import *
import numpy as np

year = 0
pop_weight = 0 #This just makes a value exist -- then I can change it later and it will remember it
gdp_weight = 0
unemp_weight = 0
life_exp_weight = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class LoginForm(Form):
    username = StringField('username')

@app.route('/', methods = ['GET']) #This page is our starting point - explains how to use the app
def home():
    return render_template('home.html')

@app.route('/setup_page', methods = ['GET']) #This is the initial setup page for our web app
def setup_page():
      return render_template("setuppage.html")

@app.route('/webapp', methods = ['POST']) #This is the actual world map
def webapp():
    if request.method == 'POST':
         # try:year #Ask if year_remembered exists
         # except NameError: year = None #If it doesn't exist, define it's nonexistence as None
         #
         # if year is None: # If it doesn't exist, you came from the setup page
              global year
              global pop_weight
              global gdp_weight
              global unemp_weight
              global life_exp_weight
              result = request.form.to_dict()
              year = int(result['Year'])
              pop_weight = int(result['GDP'])
              gdp_weight = int(result['Unemployment'])
              unemp_weight = int(result['Life_Exp'])
              life_exp_weight = int(result['Population'])
         #
         #
         # else: #you came from the same page, you need the remembered value
         #      year = year
         #      pop_weight = pop_weight
         #      gdp_weight = gdp_weight
         #      unemp_weight = unemp_weight
         #      life_exp_weight = life_exp_weight

    gdp_dict_clean = clean_dict('Datasets/gdp.csv')
    gdp_lr_dict = build_lr(gdp_dict_clean)
    unemp_dict_clean = clean_dict('Datasets/unemployment.csv')
    unemp_lr_dict = build_lr(unemp_dict_clean)
    life_exp_dict_clean = clean_dict('Datasets/life_expectancy.csv')
    life_exp_lr_dict = build_lr(life_exp_dict_clean)
    population_dict_clean = clean_dict('Datasets/population.csv')
    pop_lr_dict = build_lr(population_dict_clean)
    # Data to display and calculate coefficients which contains None values
    gdp_dict = get_data('Datasets/gdp.csv')
    gdp_dict = populate_data(gdp_dict,gdp_lr_dict)
    unemp_dict = get_data('Datasets/unemployment.csv')
    unemp_dict = populate_data(unemp_dict,unemp_lr_dict)
    life_exp_dict = get_data('Datasets/life_expectancy.csv')
    life_exp_dict = populate_data(life_exp_dict,life_exp_lr_dict)
    population_dict = get_data('Datasets/population.csv')
    population_dict = populate_data(population_dict,pop_lr_dict)

    display_list = get_display(year,gdp_dict,unemp_dict,life_exp_dict,population_dict,gdp_weight, unemp_weight, life_exp_weight, pop_weight)
    test_list = []
    for index in range(0, len(display_list)):
        test_list.append(display_list[index][1])
    x = sorted(test_list)
    for i in test_list:
        test_list[test_list.index(i)] = x.index(i)
    print(test_list)

    Year=int(result['Year'])
    GDP = round(int(result['GDP']),2)
    Unemployment = round(int(result['Unemployment']),2)
    Life_Exp = round(int(result['Life_Exp']),2)
    Population = round(int(result['Population']),2)

    return render_template("webapp.html", result=result, display_list=display_list, test_list=test_list, GDP=GDP, Unemployment=Unemployment, Life_Exp=Life_Exp, Population=Population, Year=Year) #, year_remembered = year, pop_weight_remembered = pop_weight, gdp_weight_remembered = gdp_weight, unemp_weight_remembered = unemp_weight, life_exp_weight_remembered = life_exp_weight



@app.route('/webapp/<country_searched>', methods = ['POST']) #This is the actual world map
def webapp_two(country_searched): #, year, pop_weight, gdp_weight, unemp_weight, life_exp_weights
    if request.method == 'POST':
        #you came from the same page, you need the remembered value
        # year = year
        # pop_weight = pop_weight
        # gdp_weight = gdp_weight
        # unemp_weight = unemp_weight
        # life_exp_weight = life_exp_weight
        global year # means: in this scope, use the global name
        global pop_weight
        global gdp_weight
        global unemp_weight
        global life_exp_weight

        country_searched_dict = request.form.to_dict()
        country_searched = country_searched_dict["country_searched"]

        gdp_dict_clean = clean_dict('Datasets/gdp.csv')
        gdp_lr_dict = build_lr(gdp_dict_clean)
        unemp_dict_clean = clean_dict('Datasets/unemployment.csv')
        unemp_lr_dict = build_lr(unemp_dict_clean)
        life_exp_dict_clean = clean_dict('Datasets/life_expectancy.csv')
        life_exp_lr_dict = build_lr(life_exp_dict_clean)
        population_dict_clean = clean_dict('Datasets/population.csv')
        pop_lr_dict = build_lr(population_dict_clean)
        # Data to display and calculate coefficients which contains None values
        gdp_dict = get_data('Datasets/gdp.csv')
        gdp_dict = populate_data(gdp_dict,gdp_lr_dict)
        unemp_dict = get_data('Datasets/unemployment.csv')
        unemp_dict = populate_data(unemp_dict,unemp_lr_dict)
        life_exp_dict = get_data('Datasets/life_expectancy.csv')
        life_exp_dict = populate_data(life_exp_dict,life_exp_lr_dict)
        population_dict = get_data('Datasets/population.csv')
        population_dict = populate_data(population_dict,pop_lr_dict)

        display_list = get_display(year,gdp_dict,unemp_dict,life_exp_dict,population_dict,gdp_weight, unemp_weight, life_exp_weight, pop_weight)
        year_dict = get_year(year,gdp_dict,unemp_dict,life_exp_dict,population_dict)


        test_list = []
        for index in range(0, len(display_list)):
            test_list.append(display_list[index][1])
        x = sorted(test_list)
        for i in test_list:
            test_list[test_list.index(i)] = x.index(i)
        print(test_list)

        result = {'Year': str(year), 'GDP': str(pop_weight), 'Unemployment': str(gdp_weight), 'Life_Exp': str(unemp_weight), 'Population': str(life_exp_weight)}

        Year=int(result['Year'])
        GDP = round(int(result['GDP']),2)
        Unemployment = round(int(result['Unemployment']),2)
        Life_Exp = round(int(result['Life_Exp']),2)
        Population = round(int(result['Population']),2)


        country_data = search_country(country_searched, year_dict)

        return render_template("webapp.html", result = result, display_list=display_list, test_list=test_list, country_searched=country_searched, country_data = country_data, GDP=GDP, Unemployment=Unemployment, Life_Exp=Life_Exp, Population=Population, Year=Year) #, year_remembered = year, pop_weight_remembered = pop_weight, gdp_weight_remembered = gdp_weight, unemp_weight_remembered = unemp_weight, life_exp_weight_remembered = life_exp_weight


if __name__ == '__main__':
   app.run(debug = True)
