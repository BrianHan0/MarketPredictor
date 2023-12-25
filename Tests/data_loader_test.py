import unittest
import json
import os
import datetime
import sys
sys.path.append('../src/data_processing')  # Add the path to the 'src' directory

from data_loader import load_dataset, clean_stock_data, save_clean_data  # Replace 'your_script_name' with the name of your script file

class TestStockData(unittest.TestCase):

    def setUp(self):
        # Set up test data and test file
        self.test_data = {
            "latestPrice": 193.6,
            "high": 195.41,
            "low": 192.97,
            "volume": 37149570,
            "closeTime": 1703278800223  # Example timestamp
        }
        self.test_filename = 'test_stock_data.json'
        with open(self.test_filename, 'w') as file:
            json.dump(self.test_data, file)

    def test_load_dataset(self):
        data = load_dataset(self.test_filename)
        self.assertEqual(data, self.test_data)

    def test_clean_stock_data(self):
        data = load_dataset(self.test_filename)
        cleaned_data = clean_stock_data(data)
        self.assertIsNotNone(cleaned_data)
        # Check if timestamp is converted correctly
        expected_time = datetime.datetime.fromtimestamp(1703278800223 / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(cleaned_data['closeTime'], expected_time)
        # Add more specific assertions based on what clean_stock_data does

    def test_save_clean_data(self):
        data = load_dataset(self.test_filename)
        save_clean_data(data, 'clean_' + self.test_filename)
        self.assertTrue(os.path.exists('clean_' + self.test_filename))

    def tearDown(self):
        # Clean up any created files
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists('clean_' + self.test_filename):
            os.remove('clean_' + self.test_filename)

if __name__ == '__main__':
    unittest.main()
