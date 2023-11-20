import datetime
from myapp import db
from flask import jsonify, request
from myapp.models import Itinerary

# Itineraries Routes
def get_itineraries():
    itineraries = Itinerary.query.all()
    return jsonify([
        {'id': itinerary.id,
         'date': itinerary.date,
         'activity': itinerary.activity,
         'destination_id': itinerary.destination_id
         } for itinerary in itineraries])

# Create itinerary
def create_itinerary():
    data = request.get_json()
    new_itinerary = Itinerary(
        date=datetime.utcnow(),
        activity=data['activity'],
        destination_id=data['destination_id']
    )

    db.session.add(new_itinerary)
    db.session.commit()
    return jsonify({'message': 'Itinerary created successfully'})

# Update itinerary
def update_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is None:
        return jsonify({'error': 'Itinerary not found'}), 404

    data = request.get_json()
    itinerary.date = datetime.utcnow()
    itinerary.activity = data['activity']

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