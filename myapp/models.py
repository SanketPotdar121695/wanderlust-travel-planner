from myapp.config import db

class Destination(db.Model):
    id: db.Column(db.Integer, primary_key=True)
    name: db.Column(db.String(length=30), nullable=False, unique=True)
    description: db.Column(db.String, nullable=False)

class Itinerary:
    id: db.Column(db.Integer, primary_key=True)
    destination_id: db.Column(db.Integer)
    destination: db.relationship('Destination', backref='owned_user', lazy=True)
    meal: db.Column(db.String, nullable=False)
    accomodation: db.Column(db.String, nullable=False)
    luggage: db.Column(db.String, nullable=False)
    local_tourism: db.Column(db.List, nullable=False)

class Expense:
    id: db.Column(db.Integer, primary_key=True)
    destination_id: db.Column(db.Integer, db.foreignKey('destination_id'))