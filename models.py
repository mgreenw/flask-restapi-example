from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    reviews = db.relationship('Review', backref='doctor',
                                lazy='select')

    def __init__(self, name):
        self.name = name

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    def __init__(self, description, doctor_id):
        self.description = description
        self.doctor_id = doctor_id

class DoctorSchema(ma.ModelSchema):
    class Meta:
        model = Doctor

class ReviewSchema(ma.ModelSchema):
    class Meta:
        model = Review
