from flask import Flask, jsonify
from flask_restful import Api, Resource
from marshmallow import Schema, fields
from data_utils import DataUtils

app = Flask(__name__)
airbnb_listings = [
    {"id": 1, "name": "Cozy Apartment", "price": 100, "neighborhood": "Downtown", "host_id": 123, "room_type": "Entire home/apt"},
    {"id": 2, "name": "Spacious Condo", "price": 150, "neighborhood": "Suburb", "host_id": 456, "room_type": "Entire home/apt"},
    # Add more listings as needed
]

api = Api(app)
data_utils = DataUtils()

class ListingSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    # ... other listing attributes

class Listings(Resource):
    def get(self):
        # Get all listings
        listings = data_utils.get_listings()
        return jsonify({"listings": listings})

    def post(self):
        # Create a new listing
        new_listing = data_utils.create_listing(request.json)
        return jsonify({"listing": new_listing})

class Listing(Resource):
    def get(self, listing_id):
        # Get a specific listing
        listing = data_utils.get_listing(listing_id)
        return jsonify({"listing": listing})

    def patch(self, listing_id):
        # Update a listing
        updated_listing = data_utils.update_listing(listing_id, request.json)
        return jsonify({"listing": updated_listing})

    def delete(self, listing_id):
        # Delete a listing
        data_utils.delete_listing(listing_id)
        return jsonify({"message": "Listing deleted."})

# Register resources
api.add_resource(Listings, "/listings")
api.add_resource(Listing, "/listing/<int:listing_id>")


@app.route('/listings')
def get_listings():
    return jsonify(airbnb_listings)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
