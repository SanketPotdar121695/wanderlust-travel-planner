import datetime
from myapp import db
from flask import jsonify, request
from myapp.models import Itinerary

# Itineraries Routes
def get_itineraries():
    itineraries = Itinerary.query.all()
    return jsonify([{'id': itin.id, 'activity': itin.activity, 'date': itin.date, 'destination_id': itin.destination_id} for itin in itineraries])

# Create itinerary
def create_itinerary():
    data = request.get_json()
    new_itinerary = Itinerary(activity=data['activity'], date=datetime.utcnow(), destination_id=data['destination_id'])
    db.session.add(new_itinerary)
    db.session.commit()
    return jsonify({'message': 'Itinerary created successfully'})

# Update itinerary
def update_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is None:
        return jsonify({'error': 'Itinerary not found'}), 404

    data = request.get_json()
    itinerary.activity = data['activity']
    itinerary.date = datetime.utcnow()

    db.session.commit()
    return jsonify({'message': 'Itinerary updated successfully'})

# Delete itinerary
def delete_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is None:
        return jsonify({'error': 'Itinerary not found'}), 404

    db.session.delete(itinerary)
    db.session.commit()
    return jsonify({'message': 'Itinerary deleted successfully'})