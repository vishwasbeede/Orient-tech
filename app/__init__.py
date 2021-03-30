from flask import Flask,render_template,request,redirect,url_for
from flask import jsonify, make_response

app=Flask(__name__)
app.config['SECRET_KEY']='Longasdjkfhkj'

from app import views

