#
    #RAFIQUL ISLAM
#

from googleplaces import GooglePlaces, types
from pymongo import MongoClient
import json

# connect with 27017 port
conn = MongoClient('localhost', 27017)
# create a database
bank = conn.bank
# create a collection
atm_system = bank['atm_system']

# Google place API key
giveYourAPIKey=''
MY_API_KEY = giveYourAPIKey
google_places = GooglePlaces(MY_API_KEY)
# Select parameter, search will be happened based on it
resulted_place = google_places.nearby_search(
    location='Dhaka, Bangladesh',
    radius=1000, types=[types.TYPE_ATM])

for place in resulted_place.places:
    ATM_NAME = place.name
    GEO_LOCATION = place.geo_location
    lat = GEO_LOCATION['lat']
    lng = GEO_LOCATION['lng']
    lat = json.dumps(str(lat))
    lng = json.dumps(str(lng))
    place.get_details()
    PHONE_NO = place.local_phone_number
    WEB_SITE = place.website
    info = {
        'ATM_NAME': ATM_NAME,
        'GEO_LOCATION': {'lat': lat, 'lng': lng},
        'PHONE_NO': PHONE_NO,
        'WEB_SITE': WEB_SITE
    }
    # Insert data into MongoDB database
    objId = atm_system.insert(info)


#Retrieve data from the Database
for doc in atm_system.find()[:]:
    atm = doc['ATM_NAME']
    geo = doc['GEO_LOCATION']
    lat1 = geo['lat']
    lng1 = geo['lng']
    phn = doc['PHONE_NO']
    web = doc['WEB_SITE']
    print("ATM Name: " + str(atm))
    print("Latitude " + str(lat1))
    print("Longitude: " + str(lng1))
    print("Phone Number: " + str(phn))
    print("Website: " + str(web))
    print("\n")

# Delete data from the collection
atm_system.remove()

