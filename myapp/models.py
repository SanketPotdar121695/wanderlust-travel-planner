import datetime
from myapp import db


class Destination(db.Model):
    description = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    itineraries = db.relationship(
        'Itinerary',
        backref='destination',
        lazy=True
    )


class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(100), nullable=False)
    date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow
    )
    destination_id = db.Column(
        db.Integer,
        db.ForeignKey('destination.id'),
        nullable=False,
    )


class Expense((db.Model)):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow
    )
    destination_id = db.Column(
        db.Integer,
        db.ForeignKey('destination.id'),
        nullable=False
    )