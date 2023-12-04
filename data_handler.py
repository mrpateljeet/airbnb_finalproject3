import json

def read_data():
    with open('airbnb.json', 'r') as file:
        data = json.load(file)
    return data

def write_data(data):
    with open('airbnb.json', 'w') as file:
        json.dump(data, file, indent=2)
