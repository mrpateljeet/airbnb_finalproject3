from airbnb_api import app
import unittest

class ListingsTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_listings(self):
        response = self.app.get("/listings")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json["listings"]), 1)

    def test_get_specific_listing(self):
        # ... test for successful and failed requests

    # ... tests for POST, PATCH, and DELETE endpoints

if __name__ == "__main__":
    unittest.main()
