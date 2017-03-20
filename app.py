from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from models import (Doctor, Review)

# start the flask app
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
#ma = Marshmallow(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/doctors')
def hello_doc():
    return 'Hello, Doctors!'

@app.route('/doctors/<id>')
def show_doctor(id):
    doctor = Doctor.query.filter_by(id=id).first_or_404()
    return jsonify(id=doctor.id,
                   name=doctor.name)

@app.route('/doctors/', methods = ['POST'])
def create_doctor():
    if not request.json or not 'name' in request.json:
        abort(400)
    doctor = Doctor(request.json.name)
    db.session.add(doctor)
    db.session.commit()
    return jsonify( { 'doctor': doctor } ), 201
