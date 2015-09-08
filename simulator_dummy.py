import os
import sys
import csv
import datetime
import random
import json

NUM_RECORDS = 10000
NUM_LOCATIONS = 3;
NUM_BINS = 10;

curr_fill = [[0 for x in range(NUM_BINS)] for x in range(NUM_LOCATIONS)]

def check_due(DBFile, timestamp, loc_id, bin_id):
    if curr_fill[loc_id][bin_id] > 70:
        curr_fill[loc_id][bin_id] = 0;
    else:
        curr_fill[loc_id][bin_id] += random.randrange(10,30,4);
    row = [ loc_id, bin_id, timestamp, curr_fill[loc_id][bin_id], random.randrange(25, 50, 1), random.randrange(10,90,1) ]
    with open(DBFile, 'a') as dbFile:
        writer = csv.writer(dbFile, delimiter=',')
        writer.writerow(row)

#str(sys.argv)

csvRows = ['Location ID', 'Bin ID', 'Timestamp', 'Fill Percentage', 'Temperature', 'Humidity']
DBFile = "/Users/bharde/smartBin/SmartBin/SmartBin/simulator/Bins.DB"

timestamp = datetime.datetime.utcnow().timestamp()
i = 0;

while(i < NUM_RECORDS):
    i += 1;
    timestamp = timestamp + 5*60;
    loc_id = random.randrange(0, NUM_LOCATIONS, 1);
    bin_id = random.randrange(0, NUM_BINS, 1);
    check_due(DBFile, timestamp, loc_id, bin_id);

csvfile = open(DBFile, 'r')
jsonfile = open('/Users/bharde/smartBin/SmartBin/SmartBin/simulator/Bins.json', 'w')

reader = csv.DictReader( csvfile, csvRows)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
