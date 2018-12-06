"""A simple "Hello, World" application using Flask."""

from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField, PasswordField


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
      result = request.form
      return render_template("webapp.html", result=result)

# This route beneath here will be removed eventually, using it as reference currently
@app.route('/world_map')
def hello():
    return render_template('index.html')


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
