from myapp import db
from flask import jsonify, request
from myapp.models import Destination

# Destination Routes
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([{'id': dest.id, 'name': dest.name, 'description': dest.description, 'location': dest.location} for dest in destinations])

# Create Destination
def create_destination():
    data = request.get_json()
    new_destination = Destination(name=data['name'], description=data['description'], location=data['location'])
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Destination created successfully'})

# Update Destination
def update_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination is None:
        return jsonify({'error': 'Destination not found'}), 404

    data = request.get_json()
    destination.name = data['name']
    destination.description = data['description']
    destination.location = data['location']

    db.session.commit()
    return jsonify({'message': 'Destination updated successfully'})

# Delete Destination
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination is None:
        return jsonify({'error': 'Destination not found'}), 404

    db.session.delete(destination)
    db.session.commit()
    return jsonify({'message': 'Destination deleted successfully'})