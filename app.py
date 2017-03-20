from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import (Doctor, Review)

# Initialize Flask app with SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Doctor Routes
@app.route('/api/v1/doctors/<id>')
def show_doctor(id):
    doctor = Doctor.query.filter_by(id=id).first_or_404()
    return jsonify(doctor.serialize)

@app.route('/api/v1/doctors', methods=['POST'])
def create_doctor():
    if not request.is_json or 'name' not in request.get_json():
        return bad_request('Missing data. Required fields: name')
    doctor = Doctor(request.get_json()['name'])
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'doctor': doctor.serialize}), 201

#Review Routes
@app.route('/api/v1/reviews/<id>')
def show_review(id):
    review = Review.query.filter_by(id=id).first_or_404()
    return jsonify(id=review.id,
                   doctor_id=review.doctor_id,
                   description=review.description,
                   doctor=dict(id=review.doctor.id,
                               name=review.doctor.name))

@app.route('/api/v1/reviews', methods=['POST'])
def create_review():
    request_json = request.get_json()
    if not request.is_json or 'doctor_id' not in request_json or 'description' not in request_json:
        return bad_request('Missing data. Required fields: doctor_id and description')
    doctor_id = request_json['doctor_id']
    try:
        review = Review(doctor_id=doctor_id, description=request_json['description'])
        db.session.add(review)
        db.session.commit()
    except:
        return bad_request('Given doctor_id does not exist')
    return jsonify({'review': review.serialize}), 201

# Helper Functions

def bad_request(message):
    response = jsonify({'error-message': message})
    response.status_code = 400
    return response
