import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyAmNVtLfQ00M033j3-YWaEX5ZX2d703R4I')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#print(geocode_result)

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#print(reverse_geocode_result)
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


#print(directions_result)