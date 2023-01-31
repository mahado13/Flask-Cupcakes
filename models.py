"""
Author: Mahad Osman
Date: Jan 31 2021
wodels for Cupcake app.
"""
from traitlets import default
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake Model"""
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.String, nullable = False)
    size = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.String, nullable = False, default = "https://tinyurl.com/demo-cupcake")

    def serialize(self):
        """Used to return JSON Dicts of our objects"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} Flavor={self.flavor} size={self.size} rating={self.rating} image={self.rating}>"
    
