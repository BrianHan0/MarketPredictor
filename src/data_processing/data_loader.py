import json
import datetime

from contourpy.util import data


#Function to load the file
def load_dataset(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_clean_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, default=str)