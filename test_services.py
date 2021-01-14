import requests
import unittest

BASE_URL = "http://127.0.0.1:5000"


class TestFlaskApi(unittest.TestCase):

    def test_post_success(self):
        # Given
        data = [31, 12, 15, 99, 3, 102]
        order = "desc"

        # When
        response = requests.post("{}/sorting".format(BASE_URL), json={"data": data, "order": order})

        # Then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["sorted_data"], [102, 99, 31, 15, 12, 3])

    def test_get_fail(self):
        # Given
        data = [31, 12, 15, 99, 3, 102]
        order = "desc"

        # When
        response = requests.get("{}/sorting".format(BASE_URL), json={"data": data, "order": order})

        # Then
        self.assertEqual(response.status_code, 405)

    def test_post_invalid_payload_data(self):
        # Given
        data = [31, 12, 15, 99, 3, 'sss']
        order = "abc"

        # When
        response = requests.post("{}/sorting".format(BASE_URL), json={"data": data, "order": order})

        # Then
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_payload_order(self):
        # Given
        data = [31, 12, 15, 99, 3, 102]
        order = "abc"

        # When
        response = requests.post("{}/sorting".format(BASE_URL), json={"data": data, "order": order})

        # Then
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
