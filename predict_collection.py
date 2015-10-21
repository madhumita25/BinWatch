import os
import sys
import csv
import datetime
import random
import json
import re
#from pymongo.objectid import ObjectId
#from bson.objectid import ObjectId

weight = [1,2,3,4]

def estimate_fill1(binId, threshold):
    binFile = "/Users/bharde/BinWatch/BinWatch/" + binId + ".csv";
    sum_weight = 0;
    fill = [0] * 10
    timestamp = [0] * 10
    i = 0;
    rate = 0;
    with open(binFile, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            fill[i] = int(row[4])
            timestamp[i] = float(row[5])
            if i != 0 and (fill[i] > fill[i-1]):
                rate += weight[i-1]*(fill[i] - fill[i-1])/ (timestamp[i] - timestamp[i-1]);
                sum_weight += weight[i-1];
            i += 1;

    rate = rate/ sum_weight;

    time = (threshold - fill[i-1])/rate;

    predicted_timestamp = timestamp[i-1] + time;

    #current_timestamp = timestamp = datetime.datetime.utcnow().timestamp();
    #if predicted_timestamp <  current_timestamp:
        #predicted_timestamp = current_timestamp;
    #print (predicted_timestamp)

    return predicted_timestamp

#listFile = "/Users/bharde/BinWatch/BinWatch/bin_list.csv"
listFile = sys.argv[1];

min_time = 1443493164;
#min_time = now;

threshold = 90;

with open(listFile, 'r') as dbFile:
    lines = dbFile.readlines()
    for row in lines:
        #print(row);
        time = estimate_fill1(row.rstrip(), threshold)
        if time < min_time:
            min_time = time;
print ("Next Collect at", min_time);

