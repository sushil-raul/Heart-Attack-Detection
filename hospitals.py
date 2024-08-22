import requests
from geopy.distance import geodesic
from location import get_location


def get_nearby_hospitals(user_location):
    """Get a list of nearby hospitals using the Overpass API."""
    latitude, longitude = user_location  # Get coordinates from user_location

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:5000, {latitude}, {longitude});
      way["amenity"="hospital"](around:5000, {latitude}, {longitude});
      relation["amenity"="hospital"](around:5000, {latitude}, {longitude});
    );
    out body;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print("Status Code:", response.status_code)
    # print("Response Text:", response.text)

    try:
        data = response.json()
        elements = data.get('elements', [])
        hospitals = []

        for element in elements:
            if 'tags' in element:
                name = element['tags'].get('name', 'No Name')
                latitude = element.get('lat', 'No Latitude')
                longitude = element.get('lon', 'No Longitude')
                address = element['tags'].get('addr:full', 'No Address')

                if name != 'No Name' and latitude != 'No Latitude' and longitude != 'No Longitude':
                    hospitals.append({
                        'name': name,
                        'address': address,
                        'coordinates': (latitude, longitude)
                    })
        
        return hospitals
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON from response.")
        return []

def get_nearest_hospitals(user_location):
    """Get a sorted list of nearby hospitals by distance."""
    hospitals = get_nearby_hospitals(user_location)
    
    if not hospitals:
        return []

    user_lat, user_lon = user_location
    user_coords = (user_lat, user_lon)
    
    sorted_hospitals = sorted(hospitals, key=lambda x: geodesic(user_coords, x['coordinates']).miles)
    
    return sorted_hospitals

if __name__ == "__main__":
    user_location = get_location()
    hospitals = get_nearest_hospitals(user_location)
    if hospitals:
        print("Nearby Hospitals (sorted by distance):")
        for hospital in hospitals:
            print(f"Name: {hospital['name']}")
            print(f"Address: {hospital['address']}")
            print(f"Coordinates: {hospital['coordinates'][0]}, {hospital['coordinates'][1]}")
            print()
    else:
        print("No nearby hospitals found.")
