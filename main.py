from location_utils import get_location_data
from clustering import cluster_locations

def main():
    # Example business input
    business_type = "Coffee Shop"
    location = "Chennai, India"
    radius = 5000  # in meters

    print(f"🔍 Searching best zones for: {business_type} in {location}...")

    coords, places = get_location_data(location, business_type, radius)

    if not coords or not places:
        print("❌ Failed to fetch location or places.")
        return

    cluster_locations(places)

if __name__ == "__main__":
    main()
