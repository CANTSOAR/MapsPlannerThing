from googleplaces import GooglePlaces, types, lang
import sys
import time

API_KEY = "key"

google_places = GooglePlaces(API_KEY)

with open("restaurantdata.txt", "a", encoding='utf-8') as txt:
    for lat in range(-90,90):
        for long in range(-180,180):
            time.sleep(.1)
            sys.stdout.write("\rLocation: " + str(lat * -1) + " " + str(long * -1))
            sys.stdout.flush()
            query_result = google_places.nearby_search(
                lat_lng = {"lat": lat * -1, "lng": long * -1},
                radius=1000, types=[types.TYPE_RESTAURANT])
            
            if query_result.has_attributions:
                print(query_result.html_attributions)

            if query_result.places:
                print(" ")
            
            for place in query_result.places:
                place.get_details()
                txt.write(str(lat) + " " + str(long) + ": " + place.name + "\n") #, "\n Description: ", place.details