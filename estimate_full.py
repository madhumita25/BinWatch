import os
import sys
import csv
import datetime
import random
import json
#from pymongo.objectid import ObjectId
#from bson.objectid import ObjectId

#DBFile = "/Users/bharde/BinWatch/BinWatch/52f573800000000000000000.csv"
DBFile = sys.argv[1]

rate = 0;
sum_weight = 0;
i = 0;

#stores fill levels for 5 recent records
fill = [0] * 10;

#stores timestamps for 5 recent records
timestamp = [0] * 10;

#Weight matrix
weight = [1,2,3,4]

# To calculate estimated time when the bin will be full:
#------------------------------------------------------
# 1. Calculate fill rate for consecutive records
#      rate_i = (diff between fill levels)/(diff between timestamp)
#
# 2. Calculate effective fill rate: Take weighted sum of fill rates by giving more importance to recent records:
#      rate = sum( weight_i * rate_i)/ sum(weight_i)
#
# 3. With this rate, find out when bin will be 100% full.
#
# 4. If this timestamp is lesser than now(), Give now() as output

with open(DBFile, newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        fill[i] = int(row[4])
        timestamp[i] = float(row[5])
        if i != 0 and (fill[i] > fill[i-1]):
            rate += weight[i-1]*(fill[i] - fill[i-1])/ (timestamp[i] - timestamp[i-1]);
            sum_weight += weight[i-1];
        i += 1;

rate = rate/ sum_weight;

time = (100 - fill[i-1])/rate;

predicted_timestamp = timestamp[i-1] + time;

print ("Bin will be full at:", predicted_timestamp)

#current_timestamp = timestamp = datetime.datetime.utcnow().timestamp();
#if predicted_timestamp <  current_timestamp:
#    predicted_timestamp = current_timestamp;
#print (predicted_timestamp)
