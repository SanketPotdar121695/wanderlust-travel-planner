from myapp import app
from myapp.controllers.destinations_controllers import get_destinations, create_destination, update_destination, delete_destination

# Destination Routes
@app.route('/destinations', methods=['GET'])
def destinition_get():
    return get_destinations()

# Create Destination
@app.route('/destinations', methods=['POST'])
def destinition_create():
    return create_destination

# Update Destination
@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def destination_update(destination_id):
    return update_destination(destination_id)

# Delete Destination
@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def destination_delete(destination_id):
    return delete_destination(destination_id)