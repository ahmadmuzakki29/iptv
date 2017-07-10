from flask import Flask, render_template, request
from tv import all
from model.tv import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/all')
def allRoute():
	return all.getAll()

@app.route('/create')
def create():
	tipi = Tv(name="Kompas Tv", link="http://kucluks.com")
	tipi.put()
	return "cuks"