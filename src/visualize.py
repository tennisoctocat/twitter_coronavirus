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

# Use this so that we can create graphs without printing them somewhere immediately
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = ['Source Han Sans TW', 'sans-serif', 'Noto Mono']
# /usr/share/fonts/truetype/noto/NotoMono-Regular.ttf
#matplotlib.font_manager.fontManager.addfont('/home/chom/.fonts/NotoSerifKR-Regular.otf')
fonts = matplotlib.font_manager.findSystemFonts(fontpaths='/home/chom/.fonts', fontext='otf')
print(fonts)


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values. Use commented out version if we want descending order.
# items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=False)


# top 10
# top_10_items = items[:10]
top_10_items = items[-10:]

# Create the bar graph
x_arr = [i for i in range(len(top_10_items))]
plt.bar(x_arr, [v for k, v in top_10_items])
xLabel = "Language"
if args.input_path == "reduced.country":
    xLabel = "Country"
plt.xlabel(xLabel)
plt.ylabel("Number of Tweets")
lang = "English"
if args.key != "#coronavirus":
    lang = "Korean"
plt.title("Number of tweets with " + args.key + " by " + xLabel, fontname='Noto Serif KR') 
plt.xticks(x_arr, [k for k, v in top_10_items])
plt.savefig("./graphs/" + args.input_path + args.key + ".png")
