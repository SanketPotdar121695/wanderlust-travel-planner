from myapp import db
from flask import jsonify, request
from myapp.models import Destination

# Destination Routes
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([
        {'id': dest.id,
         'name': dest.name,
         'location': dest.location,
         'description': dest.description
        } for dest in destinations])

# Get single destination
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)

    if destination:
        return jsonify({
            'id': destination.id,
            'name': destination.name,
            'location': destination.location,
            'description': destination.description
        })
    else:
        return jsonify({'message': 'Destination not found'}), 404

# Create Destination
def create_destination():
    data = request.get_json()
    new_destination = Destination(
        name=data['name'],
        location=data['location'],
        description=data['description']
    )

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
    destination.location = data['location']
    destination.description = data['description']

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