import unittest

import os
import json
import sys
sys.path.append('../src/data_processing')  # Add the path to the 'src' directory

from data_fetcher import get_stock_data, save_stock_data # Import your function from the 'data_fetcher' module

class TestDataFetchingAndSaving(unittest.TestCase):
    def setUp(self):
        self.test_symbol = "AAPL"
        self.file_path = f'../data/{self.test_symbol}_stock_data.json'

    def test_data_fetching_and_saving(self):
        # Define test symbol and API key
        test_symbol = "AAPL"
        api_key = 'sk_61bac6eb481b4c05935309dabc73b65a'

        result = get_stock_data(test_symbol,api_key)

        save_stock_data(result,test_symbol)
        # Check if the data was saved successfully
        self.assertTrue(os.path.exists('../data'))
        self.assertTrue(os.path.exists(f'../data/{test_symbol}_stock_data.json'))

        # Load the saved data and check if it's a valid JSON
        with open(f'../data/{test_symbol}_stock_data.json', 'r') as file:
            saved_data = json.load(file)

        self.assertIsInstance(saved_data, dict)
    def tearDown(self):
        # This method is called after each test to clean up
        if os.path.exists('../data'):
            os.remove(self.file_path)
if __name__ == '__main__':
    unittest.main()
