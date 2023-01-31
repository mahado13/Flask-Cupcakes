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
    return render_template("index.html")

@app.route('/api/cupcakes')
def show_cupcakes():
    """Viewing the entire list of cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Route handler for viewing information on a single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """Route handler for adding a new cupcake"""
    new_cupcake = Cupcake(
            flavor=request.json["flavor"],
            size= request.json["size"],
            rating= request.json["rating"],
            image= request.json.get("image")
            )
    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(newcupcake =new_cupcake.serialize())

    return (response_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods =['PATCH'])
def edit_cupcake(cupcake_id):
    """Handles the edting of one of our cupcakes"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor=request.json.get("flavor", cupcake.flavor),
    cupcake.size= request.json.get("size", cupcake.size),
    cupcake.rating= request.json.get("rating", cupcake.rating),
    cupcake.image= request.json.get("image", cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    response_json = jsonify(cupcake = cupcake.serialize())

    return (response_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods =['DELETE'])
def delete_cupcake(cupcake_id):
    """Will delete a cupcake once"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(msg="deleted")
