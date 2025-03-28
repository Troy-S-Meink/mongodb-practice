from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# (for some reason had issues with existing env var names, so changed them)
MONGOUSER = os.getenv('USER')
MONGOPASS = os.getenv('PASS')
MONGOHOST = os.getenv('HOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
sampler = client.ked6na
ked6na = sampler.ked6na

print("Connection attempt successful")
print("Current DB:\t", ked6na)

# 1.
# Create a new collection called "sports" in the current MongoDB
sports = sampler.sports
print('\nCollection Created:\t', sports)

# 2.
# Add five documents into the new collection
sports.delete_many({})  # Deleting all previous documents beforehand

sport_1 = {
    "name": "Swimming",
"equipment": "goggles",
    "indoor": True
}
sport_2 = {
    "name": "Running",
    "equipment": "shoes",
    "indoor": False
}
sport_3 = {
    "name": "Hiking",
    "equipment": "backpack",
    "indoor": False
}
sport_4 = {
    "name": "Weightlifting",
    "equipment": "barbell",
    "indoor": True
}
sport_5 = {
    "name": "Polo",
    "equipment": "horse",
    "indoor": False
}

# Insert each document individually
sports.insert_one(sport_1)
sports.insert_one(sport_2)
sports.insert_one(sport_3)
sports.insert_one(sport_4)
sports.insert_one(sport_5)

print('\n5 new documents created')

# 3.
# Display 3 out of 5 documents by filtering only for outdoor sports
outdoor_sports = sports.find({"indoor": False})

print('\nOutdoor Sports:')
for sport in outdoor_sports:
    print(dumps(sport, indent=2))

print('\nNumber of Documents:', sports.count_documents({"indoor": False}))