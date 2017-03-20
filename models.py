from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
db = SQLAlchemy()
#ma = Marshmallow()

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    reviews = db.relationship('Review', backref='doctor',
                                lazy='select')

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'reviews': [review.serialize for review in self.reviews]
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    def __init__(self, description, doctor_id):
        self.description = description
        self.doctor_id = doctor_id

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'doctor_id': self.doctor_id,
            'description': self.description,
        }
