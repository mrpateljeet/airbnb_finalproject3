from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for illustration purposes
airbnb_listings = [
    {"id": 1, "name": "Cozy Apartment", "price": 100, "neighborhood": "Downtown", "host_id": 123, "room_type": "Entire home/apt"},
    {"id": 2, "name": "Spacious Condo", "price": 150, "neighborhood": "Suburb", "host_id": 456, "room_type": "Entire home/apt"},
    # Add more listings as needed
]

@app.route('/listings')
def get_listings():
    return jsonify(airbnb_listings)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
