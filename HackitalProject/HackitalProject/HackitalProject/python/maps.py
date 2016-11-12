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

    def distance_to_location(self):
        origin = self.get_lat_long('419 7th St NW, Washington, DC')
        destination = self.get_lat_long('1900 F St NW, Washington DC')
        matrix = self.gmaps.distance_matrix(origin, destination)
        print(matrix)



"""
TODO
Walking distance to station
Walking distance from loc A to loc B
walking distance from station to loc B
"""
#sample usage of get_lat_long function
m = maps()
address = '1900 F Street NW, Washington, DC'
lat_long = m.get_lat_long(address)
m.distance_to_location()
print("Address: ", address)
print("Lat: ", lat_long['lat'])
print("Long: ", lat_long['lng'])


