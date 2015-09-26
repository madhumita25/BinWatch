import os
import sys
import csv
import datetime
import random
import json
#from pymongo.objectid import ObjectId
from bson.objectid import ObjectId

NUM_LOCATIONS = 3;
NUM_BINS = 10;

DBFile = "/Users/bharde/smartBin/SmartBin/SmartBin/simulator/MasterBins.DB"
csvRows = ['_id', 'isActive', 'latitude', 'longitude', 'created_timestamp', 'cleared_timestamp', 'last_sensed_timestamp', 'temperature', 'humidity', 'fill']

timestamp = datetime.datetime.utcnow().timestamp()

for loc_id in range(1,NUM_LOCATIONS+1):
    for bin_id in range(1,NUM_BINS+1):
        created_time = datetime.datetime(2014, loc_id+1, bin_id+1)
        object_id = ObjectId.from_datetime(created_time)
        cleared_time = datetime.datetime(2015, loc_id+2, bin_id+2)
        sensed_time = datetime.datetime(2015, loc_id+3, bin_id+3)
        row = [ object_id, "true", random.randrange(120000,130000,1)/10000.0, random.randrange(770000,780000,1)/10000.0, created_time.timestamp(), cleared_time.timestamp(), sensed_time.timestamp(), random.randrange(25, 50, 1), random.randrange(10,90,1), random.randrange(0,100,1)]
        with open(DBFile, 'a') as dbFile:
            writer = csv.writer(dbFile, delimiter=',')
            writer.writerow(row)


csvfile = open(DBFile, 'r')
jsonfile = open('/Users/bharde/smartBin/SmartBin/SmartBin/simulator/MasterBins.json', 'w')

reader = csv.DictReader( csvfile, csvRows)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
