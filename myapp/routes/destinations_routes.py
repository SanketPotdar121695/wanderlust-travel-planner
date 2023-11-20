from myapp import app
from myapp.controllers.destinations_controllers import get_destinations, get_destination, create_destination, update_destination, delete_destination

# Destination Routes
@app.route('/destination', methods=['GET'])
def destinitions_get():
    return get_destinations()

# Get a single destination
@app.route('/destination/<int:destination_id>', methods=['GET'])
def destination_get(destination_id):
    return get_destination(destination_id)

# Create Destination
@app.route('/destinations', methods=['POST'])
def destinition_create():
    return create_destination

# Update Destination
@app.route('/destination/<int:destination_id>', methods=['PUT'])
def destination_update(destination_id):
    return update_destination(destination_id)

# Delete Destination
@app.route('/destination/<int:destination_id>', methods=['DELETE'])
def destination_delete(destination_id):
    return delete_destination(destination_id)