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
              pop_weight = int(result['Population'])
              gdp_weight = int(result['GDP'])
              unemp_weight = int(result['GINI'])
              life_exp_weight = int(result['Happiness'])
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


    return render_template("webapp.html", result=result, display_list=display_list, test_list=test_list) #, year_remembered = year, pop_weight_remembered = pop_weight, gdp_weight_remembered = gdp_weight, unemp_weight_remembered = unemp_weight, life_exp_weight_remembered = life_exp_weight



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

        result = {'Year': str(year), 'Population': str(pop_weight), 'GDP': str(gdp_weight), 'GINI': str(unemp_weight), 'Happiness': str(life_exp_weight)}

        country_data = search_country(country_searched, year_dict)

        return render_template("webapp.html", result = result, display_list=display_list, test_list=test_list, country_searched=country_searched, country_data = country_data) #, year_remembered = year, pop_weight_remembered = pop_weight, gdp_weight_remembered = gdp_weight, unemp_weight_remembered = unemp_weight, life_exp_weight_remembered = life_exp_weight


if __name__ == '__main__':
   app.run(debug = True)




# @app.route('/world_map', methods=['GET', 'POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return render_template('index.html', processed_text=processed_text)
#
# @app.route('/world_map', methods=['GET', 'POST'])
# def my_year_post():
#     year = request.form['text']
#     processed_year = year.upper()
#     return render_template('index.html', processed_year=processed_year)
#
#
#
# @app.route('/hello', methods= ['GET', 'POST'])
# def helloTemplate():
#     food = ["Cheese", "Tuna", "Beef"]
#     form = LoginForm()
#     return render_template('hello.html', food=food, form=form)
#
# @app.route('/hello2', methods= ['GET', 'POST'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("home2.html",result = result)

# Break here -- between things I am testing

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name
#
# # @app.route('/login_page')
# # def login_page():
# #     return render_template('login.html')
#
# @app.route('/formsubmit',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       value1 = request.form.getlist('Options')
#       print(value1)
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))



# @app.route('/login_page')
# def my_form():
#     return render_template('login.html')
#
# @app.route('/login_page', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text
