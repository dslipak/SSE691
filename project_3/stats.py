#!/usr/bin/env python

'''

Course: SSE 691
Project: 3
Student: Dmitriy Slipak

This script creates set of satistics from Chapter 5 
using pandas libray. 

'''

import argparse, json
import pandas as pd
from datetime import datetime
from collections import Counter, defaultdict, OrderedDict
from matplotlib import pyplot as plt
import book_stats as bs

##
# create_args function
# 
# Prepares command line arguments to be
# passed into script.
# 
def create_args():
  argp = argparse.ArgumentParser(description="Provides statistics for tweets")
  argp.add_argument("--source", help="Data source file including path", required=True)

  return argp.parse_args()

# Entry point
args = create_args()
tweets = pd.read_json(args.source)

if tweets is None:
  print("No tweets")
  sys.exit(1)

# Data preparation
# 
tw = [x for x in [tweets.created_at, tweets.retweet_count]]
retweets = [x for x in tw[1]]
dates = [x.to_pydatetime().date().strftime("%Y-%m-%d") for x in tw[0]]

i = 0
dd = defaultdict()

for x in dates:
  if x in dd:
    dd[x] += retweets[i]
  else:
    dd[x] = retweets[i]
  i += 1

dd = OrderedDict(sorted(dd.items(), key=lambda x: x[0]))
dates_count = dict(Counter(dates))
dates_count = OrderedDict(sorted(dates_count.items(), key=lambda t: t[0]))
dates_list = [x for x in dates_count.keys()]
tweets_list = [x for x in dates_count.values()]
retweets_list = [x for x in dd.values()]
combined_list = [x for x in zip(dates_list, tweets_list, retweets_list)]

# Main dataframe
# 
df = pd.DataFrame(combined_list, columns=["date", "tweets", "retweets"]).sort_values(by=["tweets"]).reset_index(drop=True)
print("\n", df, "\n")
num_rows = int(df.size//3) # data frame size divided by number of columns

# Tests
# 
print("num_points", num_rows)
print("largest value", df["tweets"].max())
print("smallest value", df["tweets"].min())
print("second smallest value", df.get_value(index=1, col="tweets"))
print("second largest value", df.get_value(index=num_rows-2, col="tweets"), "\n")

print("expected: mean(tweets)", bs.mean(tweets_list))
print("result: mean(tweets)", "%.15f" % df["tweets"].mean(), "\n")

print("expected: median(tweets)", bs.median(tweets_list))
print("result: median(tweets)", df["tweets"].median(), "\n")

print("expected: quantile(tweets, 0.10)", bs.quantile(tweets_list, .10))
print("result: quantile(tweets, 0.10)", int(df["tweets"].quantile(.10)), "\n")

print("expected: quantile(tweets, 0.25)", bs.quantile(tweets_list, .25))
print("result: quantile(tweets, 0.25)", int(df["tweets"].quantile(.25)), "\n")

print("expected: quantile(tweets, 0.10)", bs.quantile(tweets_list, .75))
print("result: quantile(tweets, 0.10)", int(df["tweets"].quantile(.75)), "\n")

print("expected: quantile(tweets, 0.10)", bs.quantile(tweets_list, .90))
print("result: quantile(tweets, 0.10)", int(df["tweets"].quantile(.90)), "\n")

print("expected: mode(tweets)", bs.mode(tweets_list))
print("result: mode(tweets)", [x for x in df["tweets"].mode()], "\n")

print("expected: data_range(tweets)", bs.data_range(tweets_list))
print("result: data_range(tweets)", df["tweets"].max()-df["tweets"].min(), "\n")

print("expected: variance(tweets)", bs.variance(tweets_list))
print("result: variance(tweets)", "%.15f" % df["tweets"].var(), "\n")

print("expected: standard_deviation(tweets)", bs.standard_deviation(tweets_list))
print("result: standard_deviation(tweets)", "%.15f" % df["tweets"].std(), "\n")

print("expected: interquartile_range(tweets)", bs.quantile(tweets_list, .75)-bs.quantile(tweets_list, .25))
print("result: interquartile_range(tweets)", int(df["tweets"].quantile(.75))-int(df["tweets"].quantile(.25)), "\n")

print("expected: covariance(tweets, retweets)", bs.covariance(tweets_list, retweets_list))
print("result: covariance(tweets, retweets)", "%.7f" % df["tweets"].cov(df["retweets"]), "\n")

print("expected: correlation(tweets, retweets)", bs.correlation(tweets_list, retweets_list))
print("result: correlation(tweets, retweets)", "%.12f" % df["tweets"].corr(df["retweets"]), "\n")

print(df.describe(), "\n")

df.plot.scatter(x="retweets", y="tweets", ylim=(0, df["tweets"].max()+(df["tweets"].max()/10)), xlim=(0, df["retweets"].max()+(df["retweets"].max()/10)))

# Remove first outlier
newdf = df.copy()
newdf["x-mean"] = abs(newdf["retweets"] - newdf["retweets"].mean())
newdf["1.96*std"] = 1.96*newdf["retweets"].std()
newdf["outlier"] = abs(newdf["retweets"] - newdf["retweets"].mean()) > 1.96*newdf["retweets"].std()
print(newdf, "\n")

df = newdf[newdf.outlier != True]
#print(df, "\n")

df.plot.scatter(x="retweets", y="tweets", ylim=(0, df["tweets"].max()+(df["tweets"].max()/10)), xlim=(0, df["retweets"].max()+(df["retweets"].max()/10)))

# Remove second outlier
newdf = df.copy()
newdf["x-mean"] = abs(newdf["retweets"] - newdf["retweets"].mean())
newdf["1.96*std"] = 1.96*newdf["retweets"].std()
newdf["outlier"] = abs(newdf["retweets"] - newdf["retweets"].mean()) > 1.96*newdf["retweets"].std()
#print(newdf, "\n")

df = newdf[newdf.outlier != True]
#print(df, "\n")

df.plot.scatter(x="retweets", y="tweets", ylim=(0, df["tweets"].max()+(df["tweets"].max()/10)), xlim=(0, df["retweets"].max()+(df["retweets"].max()/10)))
#plt.show()
