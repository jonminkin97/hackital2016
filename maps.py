import googlemaps

class maps:

    def __init__(self):
        key = open('keys.txt', 'r').read()
        if key.endswith('\n'):
            key = key[:-1]

        self.gmaps = googlemaps.Client(key=key)

    def get_lat_long(self, address):
        geocode_result = self.gmaps.geocode(address)
        return geocode_result[0]['geometry']['location']

        print("Address: ", address)
        print("Latitude: ", geocode_result[0]['geometry']['location']['lat'])
        print("Longitude: ",geocode_result[0]['geometry']['location']['lng'])

#sample usage of get_lat_long function
m = maps()
address = '419 7th St NW, Washington, DC'
lat_long = m.get_lat_long(address)
print("Address: ", address)
print("Lat: ", lat_long['lat'])
print("Long: ", lat_long['lng'])


