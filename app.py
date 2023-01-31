"""
Author: Mahad Osman
Date: Jan 31 2021
Assignment: Flask app for Cupcakes
"""
import re
from flask import Flask, redirect, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret-1-2-3"

connect_db(app)
@app.route('/')
def index():
    return render_template()