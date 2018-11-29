"""A simple "Hello, World" application using Flask."""

from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/world_map')
def hello():
    return render_template('index.html')

@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# @app.route('/login_page')
# def login_page():
#     return render_template('login.html')

@app.route('/formsubmit',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      value1 = request.form.getlist('Options')
      print(value1)
      return redirect(url_for('success',name = value1))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
