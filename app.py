from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import (Doctor, Review)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/doctors/<id>')
def show_doctor(id):
    doctor = Doctor.query.filter_by(id=id).first_or_404()
    return jsonify(doctor.serialize)

@app.route('/api/v1/doctors', methods=['POST'])
def create_doctor():
    if not request.is_json or 'name' not in request.get_json():
        abort(400)
    doctor = Doctor(request.get_json()['name'])
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'doctor': doctor.serialize}), 201

@app.route('/api/v1/reviews/<id>')
def show_review(id):
    review = Review.query.filter_by(id=id).first_or_404()
    return jsonify(id=review.id,
                   doctor_id=review.doctor_id,
                   doctor=dict(id=review.doctor.id,
                               name=review.doctor.name))

@app.route('/api/v1/reviews', methods=['POST'])
def create_review():
    request_json = request.get_json()
    if not request.is_json or 'doctor_id' not in request_json or 'description' not in request_json:
        abort(400)
    review = Review(doctor_id=request_json['doctor_id'], description=request_json['description'])
    db.session.add(review)
    db.session.commit()
    return jsonify({'review': review.serialize}), 201
