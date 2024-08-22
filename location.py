# location.py
import requests

def get_location():
    """Get the user's location using IP-based geolocation."""
    response = requests.get('http://ipinfo.io/json')
    data = response.json()
    coordinates = data.get('loc', '0,0').split(',')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])
    return latitude, longitude

    