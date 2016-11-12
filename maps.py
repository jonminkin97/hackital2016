import googlemaps

def get_lat_long(address):
    geocode_result = gmaps.geocode(address)
    print("Address: ", address)
    print("Latitude: ", geocode_result[0]['geometry']['location']['lat'])
    print("Longitude: ",geocode_result[0]['geometry']['location']['lng'])
key = open('keys.txt', 'r').read()
if key.endswith('\n'):
    key = key[:-1]

gmaps = googlemaps.Client(key=key)
get_lat_long('419 7th St NW, Washington, DC')
