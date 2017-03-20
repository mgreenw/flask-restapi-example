from app import db

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

    def __init__(self, description):
        self.description = description
