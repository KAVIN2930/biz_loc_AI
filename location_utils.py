import requests

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key

def get_location_data(location, keyword, radius=5000):
    # 1. Get coordinates
    geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
    geo_params = {"address": location, "key": API_KEY}
    geo_resp = requests.get(geo_url, params=geo_params).json()

    if geo_resp["status"] != "OK":
        return None, None

    coords = geo_resp["results"][0]["geometry"]["location"]
    lat, lng = coords["lat"], coords["lng"]

    # 2. Find nearby places
    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    places_params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "keyword": keyword,
        "key": API_KEY
    }

    places_resp = requests.get(places_url, params=places_params).json()

    if places_resp["status"] != "OK":
        return coords, None

    places = [
        {
            "name": place["name"],
            "lat": place["geometry"]["location"]["lat"],
            "lng": place["geometry"]["location"]["lng"]
        }
        for place in places_resp["results"]
    ]

    return coords, places
