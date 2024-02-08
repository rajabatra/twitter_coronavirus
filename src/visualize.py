#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# get the top 10 keys and sort from low to high
items_10 = items[:10]
keys = [x[0] for x in items_10]
values = [x[1] for x in items_10]
sorted_keys = keys[::-1]
sorted_values = values[::-1]
print(sorted_keys)
print(sorted_values)
#plot the data
plt.bar(range(len(sorted_keys)), sorted_values,)
plt.xticks(range(len(sorted_keys)), sorted_keys)
plt.xlabel(args.input_path[8:])
plt.ylabel('number of tweets')
plt.savefig(args.key[1:] + args.input_path[8:] +'.png')
