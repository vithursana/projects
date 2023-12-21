
import unittest
from unittest.mock import patch, Mock
from Assignment_2 import fetch_random_dog_facts

class TestFetchRandomDogFacts(unittest.TestCase):

    @patch('requests.get')
    @patch('json.loads')
    def test_fetch_random_dog_facts(self, mock_json_loads, mock_requests_get):
        # Mock the response from the API
        mock_response = Mock()
        mock_response.text = '{"facts": ["Fact 1", "Fact 2"]}'  # Mocked JSON response
        mock_requests_get.return_value = mock_response

        # Mock the json.loads function
        mock_json_loads.return_value = {"facts": ["Fact 1", "Fact 2"]}

        # Call the function
        facts = fetch_random_dog_facts()

        # Assertions
        self.assertEqual(facts, ["Fact 1", "Fact 2"])
        mock_requests_get.assert_called_once_with("http://dog-api.kinduff.com/api/facts")
        mock_json_loads.assert_called_once_with(mock_response.text)

if __name__ == '__main__':
    unittest.main()
