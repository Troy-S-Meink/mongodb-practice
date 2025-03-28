#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *

stats = client.stats
print('stats:\t', stats)

dbs = client.list_database_names()
print('\nDBs:\t', dbs)

thisdb = client.sample_restaurants
cols = thisdb.list_collection_names()
print('\ncols:\t', cols, '\n')

restaurants = thisdb.restaurants
count = restaurants.count_documents({})
print(count, "restaurants")

italian = restaurants.count_documents({'cuisine': 'Italian'})
print(italian, "Italian restaurants")
