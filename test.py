# test_app.py

import unittest

import app


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.payload = {
            "geometry": {
                "type": "Point",
                "latitude": 43.2849777,
                "longitude": -123.1189405
            },
            "address": "10d95 W Pender St, Vancouver, BC V6E 2M6",
            "bed": 2,
            "bath": 1
        }

    def test_get_response(self):
        response = self.client.get('/house')
        self.assertEqual(response.status_code, 200)

    def test_post_response(self):
        response = self.client.post('/house', json=self.payload)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()