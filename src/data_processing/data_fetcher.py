import requests
import json
import os
import datetime
from contourpy.util import data



def get_stock_data(symbol,api_key):
    # Endpoint URL
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={api_key}'

    # Make the request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Error fetching data"

# Cleans the stock data so it is easier to read
def clean_stock_data(data):
    return None

def save_stock_data(stock_data,symbol):
    output_directory = '../data'
    output_file_name = f'{symbol}_stock_data.json'
    output_file_path = os.path.join(output_directory, output_file_name)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(output_file_path, 'w') as file:
        json.dump(stock_data,file)

