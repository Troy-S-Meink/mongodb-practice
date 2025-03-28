from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# (for some reason had issues with existing env var names, so changed them)
MONGOUSER = os.getenv('USER')
MONGOPASS = os.getenv('PASS')
MONGOHOST = os.getenv('HOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_restaurants
restaurants = sampler.restaurants

#print("Connection attempt successful")
#print("Restaurants Collection:\n", restaurants, "\n")

# 1.
# Create a new collection called "sports" in the current MongoDB