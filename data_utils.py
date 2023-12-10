import json

class DataUtils:

    def __init__(self):
        self.data_file = "data/airbnb.json"

    def get_listings(self):
        with open(self.data_file, "r") as f:
            return json.load(f)

    def get_listing(self, listing_id):
        listings = self.get_listings()
        for listing in listings:
            if listing["id"] == listing_id:
                return listing
        return None

    def create_listing(self, new_listing):
        # Validate and persist new listing
        # ...

        return new_listing

    def update_listing(self, listing_id, updated_data):
        listings = self.get_listings()
        for index, listing in enumerate(listings):
            if listing["id"] == listing_id:
                listings[index] = updated_data
                # Write updated data to file
                # ...
                return listings[index]
        return None

    def delete_listing(self, listing_id):
        listings = self.get_listings()
        for index, listing in enumerate(listings):
            if listing["id"] == listing_id:
                del listings[index]
                # Write updated data to file
                # ...
                return
        return None
