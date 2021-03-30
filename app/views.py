from app import app,render_template,request,redirect,url_for
from app import jsonify, make_response
from test import *
from lucky_number import *
from datetime import datetime

import json
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

@app.route("/")
def root_fun():
    return render_template('public/templates/index.html')

# @app.route("/blog/")
@app.route("/blog/")
def return_fun():
    return render_template("new.html",names="Blog")

@app.route("/new.html")
def return_fun1_1_1():
    return render_template("new.html",names="Ganesh")

@app.route("/lucky_number.html",methods=['GET'])
def display_page_lucky_number():
    output_data=("val1","val2")
    return render_template("lucky_number.html",output_data=output_data)

@app.route("/lucky_number.html",methods=['POST'])
def return_cal_lucky():
    input_data=request.form['input_dob']
    output_data=cal_lucky_num(request.form['input_dob'])
    f = open("luckuy_number.log", "a")
    f.write("{0} -- {1}\n".format(input_data,output_data))
    f.close()
    return render_template("lucky_number.html",output_data=output_data)

@app.route("/animals")
def return_fun2():
    return render_template("aniamls.html",z=packed)

# @app.route("/animals1")
# def GreetUserForm():
#     username = StringField(label=("Enter your name"))
#     submit = SubmitField(label=("submit"))
#     return ""

@app.route("/Products/")
def products_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Blog/")
def Blog_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Email/")
def Contact_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Careers/")
def Careers_page():
    return render_template("aniamls.html",z=packed)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      data_log=json.dumps(dict(request.form))
      f = open("filename.log", "a")
      f.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), data_log))
      f.close()
      requset_data = request.form['reqdesc']
      print(requset_data)
    #   return "We will contact you soon on this queires"
      return render_template('public/templates/index.html')
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))