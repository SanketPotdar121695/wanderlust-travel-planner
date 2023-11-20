from myapp import app
from myapp.controllers.itineraries_controllers import get_itineraries, get_itinerary, create_itinerary, update_itinerary, delete_itinerary

# Itineraries Routes
@app.route('/itineraries', methods=['GET'])
def itineraries_get():
    return get_itineraries()

# Get a single itinerary
@app.route('/itinerary/<int:itinerary_id>', methods=['GET'])
def itinerary_get(itinerary_id):
    return get_itinerary(itinerary_id)

# Create itinerary
@app.route('/itineraries', methods=['POST'])
def itinerary_create():
    return create_itinerary()

# Update itinerary
@app.route('/itineraries/<int:itinerary_id>', methods=['PUT'])
def itinerary_update(itinerary_id):
    return update_itinerary(itinerary_id)

# Delete itinerary
@app.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def itinerary_delete(itinerary_id):
    return delete_itinerary(itinerary_id)