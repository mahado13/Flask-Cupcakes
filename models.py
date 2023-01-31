"""
Author: Mahad Osman
Date: Jan 31 2021
wodels for Cupcake app.
"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake Model"""