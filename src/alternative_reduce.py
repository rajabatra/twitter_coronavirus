#!/usr/bin/env python3

# Arguments
import argparse

def list_of_strings(arg):
    return arg.split(',')

parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+', type=list_of_strings)
args = parser.parse_args()

import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import glob

paths = glob.glob('outputs/geoTwitter*.lang')
total = {hashtag: [] for hashtag in args.keys[0]}
for path in paths:
    date = os.path.splitext(os.path.basename(path))[0][10:18]
    with open(path) as f:
        tmp = json.load(f)
        
        for k in tmp:
            if k in args.keys[0]:
                count = 0
                for hashtag in tmp[k]:
                    count += tmp[k][hashtag]
                total[k].append((date, count))

#print(total)
#plot
for hashtag, date_count in total.items():
    dates, count = zip(*[(datetime.strptime(date, '%y-%m-%d'), count) for date, count in date_count])

    
    sorted_days = sorted(range(len(dates)), key=lambda k: dates[k])
    dates = [dates[i] for i in sorted_days]
    count = [count[i] for i in sorted_days]

    # Plotting
    plt.plot(dates, count, label=hashtag)

# Formatting the plot
plt.xlabel('Date')
plt.ylabel('Number Of Tweets')
plt.title('Hashtag Count Over Time')
plt.legend()
name = []
for hashtag in args.keys[0]:
    name.append(hashtag[1:])
final_name = '_'.join(name)
plt.savefig(final_name + '.png')
