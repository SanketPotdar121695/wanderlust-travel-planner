from myapp import app
from myapp.controllers.itineraries_controllers import get_itineraries, create_itinerary, update_itinerary, delete_itinerary

# Itineraries Routes
@app.route('/itineraries', methods=['GET'])
def itineraries_get():
    return get_itineraries()

# Create itinerary
@app.route('/itinerary', methods=['POST'])
def itinerary_create():
    return create_itinerary()

# Update itinerary
@app.route('/itinerary/<int:itinerary_id>', methods=['PUT'])
def itinerary_update(itinerary_id):
    return update_itinerary(itinerary_id)

# Delete itinerary
@app.route('/itinerary/<int:itinerary_id>', methods=['DELETE'])
def itinerary_delete(itinerary_id):
    return delete_itinerary(itinerary_id)