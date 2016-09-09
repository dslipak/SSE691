#!/usr/bin/env python

'''

Course: SSE 691
Project: 1
Students: Thuy-Duong Thi Nguyen, Dmitriy Slipak

This script contains set of functions to represent
different charts as per chapter 3 from "Data science from scratch".

'''

import argparse, json, sys, random
from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict, Counter

##
# create_args function
# 
# Prepares command line arguments to be
# passed into script.
# 
def create_args():
  argp = argparse.ArgumentParser(description="Creates set of charts")
  argp.add_argument("--source", help="Data source file including path", required=True)
  argp.add_argument("--type", help="Type of the chart: tweets, retweets, etc.", required=True)

  return argp.parse_args()

##
# get_tweets function
# 
# Reads tweets from data file.
# args: src - path to data file
# returns: tweets data
# 
def get_tweets(src):
  tweets = None

  try:
    f = open(args.source, 'r')
  except IOError:
    print("Can't open tweets source file")
  else:
    tweets = f.read()
    f.close()
  
  return tweets

##
# create_tweets_chart function
# 
# Creates simple line chart from provided set of tweets.
# The chart will show number of monthly tweets by @merceryou during 2016.
# 
# args: data - set of tweets
# returns: None
#
def create_tweets_chart(data):
  # List of extracted by criteria tweets.
  tw_list = [datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").date().strftime("%Y-%m-%d") for x in data]
  tc = Counter(tw_list)
  tweets = defaultdict(int)

  # Combine tweets by month into tweets list
  for k, v in tc.items():
    m = datetime.strptime(k, "%Y-%m-%d").date().strftime("%m")
    if m in tweets:
      tweets[m] += v
    else:
      tweets[m] = v

  # Sort new list of tweets
  tweets = sorted(tweets.items())

  x, y = [t[0] for t in tweets], [t[1] for t in tweets]
  print(x)
  print(y)
   
  plt.plot(x, y, color="blue", marker='o', linestyle="solid")
  plt.title("Tweets by @merceryou in 2016")
  plt.xlabel("Month")
  plt.ylabel("# of tweets")
  plt.axis([1, 12, 0, max(y)+5]) # Set additional space above max(y)
  
  plt.show()

##
# create_retweets_chart function
# 
# Creates simple bar chart from provided set of tweets.
# 
# args: data - set of tweets
# returns: None
#
def create_retweets_chart(data):
  # Collect all tweets with retweet_count field
  tw_list = [(datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").date().strftime("%Y-%m-%d"), 
    x["retweet_count"]) for x in data]

  # Get all retweets in July
  tw_july = [x for x in tw_list if datetime.strptime(x[0], 
    "%Y-%m-%d").date().strftime("%m") == "07"]

  re_tweets = defaultdict(int)

  # Combine daily retweets into tw_july list
  for k, v in tw_july:
    day = datetime.strptime(k, 
      "%Y-%m-%d").date().strftime("%d")
    if day in re_tweets:
      re_tweets[day] += v
    else:
      re_tweets[day] = v

  re_tweets = sorted(re_tweets.items())

  x, y = [t[0] for t in re_tweets], [t[1] for t in re_tweets]
  print(x)
  print(y)
  xs = range(len(x))

  plt.bar([x+0.1 for x in xs], y)
  plt.title("retweets by @merceryou in July 2016")
  plt.ylabel("# of retweets")
  plt.xlabel("Day")
  plt.xticks([i+0.5 for i, _ in enumerate(xs)], x)
  
  plt.show()

##
# create_tweets_histogram_chart function
# 
# Creates simple histogram from provided set of tweets.
# 
# Histogram represents number of tweets by @merceryou
# divided into hourly buckets.
# 
# args: data - set of tweets
# returns: None
#
def create_tweets_histogram_chart(data):
  # List of all tweets from data source
  tw_list = [datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").time().strftime("%H") for x in data]

  # Hourly buckets
  buckets = [(0, 6), (6, 12), (12, 18), (18, 24)]
  b_labels = ["00-06", "06-12", "12-18", "18-24"]
  
  # Locate a bucket by hour in the buckets list
  in_bucket = lambda hour: [(b[0], b[1]) for b in buckets if int(hour) >= b[0] and int(hour) <= b[1]][0]
  # Locate index of a bucket in the buckets list
  index = lambda bucket: buckets.index(bucket)
  histogram = Counter(index(in_bucket(h)) for h in tw_list)

  plt.bar([x+0.1 for x in histogram.keys()], histogram.values())
  plt.axis([0, len(buckets), 0, max(histogram.values())+10])
  plt.xticks([i+0.5 for i, _ in enumerate(buckets)], b_labels)
  plt.title("Histogram of tweets by @merceryou in 2016")
  plt.ylabel("# of tweets")
  plt.xlabel("Hours")

  plt.show()

##
# create_user_mentions_chart function
# 
# Creates simple histogram chart from provided set of tweets.
# 
# args: data - set of tweets
#       incorrect - optional args to demonstrate missleading chart
# returns: None
#
def create_user_mentions_chart(data, incorrect=False):
  # List of all tweets from data source
  tw_list = [{datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").date().strftime("%m") : 
    len(x["entities"]["user_mentions"])} for x in data]

  tweets = defaultdict(int)

  for _, li in enumerate(tw_list):
    for k, v in li.items():
      if k in tweets:
        tweets[k] += v
      else:
        tweets[k] = v

  # List of tweets for March, and April
  two_months = [(k, v) for k, v in tweets.items() if k == "03" or k == "04"]
  two_months = sorted(two_months)

  x, y = [t[0] for t in two_months], [t[1] for t in two_months]
  print(x)
  print(y)

  plt.bar([int(x)-0.4 for x in x], y, 0.8)
  plt.xticks([int(x) for x in x])
  plt.ylabel("# of mentions")
  plt.xlabel("Month")

  if incorrect:
    plt.title("Users mentions of @merceryou in March-April 2016 (mislead)")
    plt.axis([1, 6, min(y)-5, max(y)+5])
  else:
    plt.title("Users mentions of @merceryou in March-April 2016")
    plt.axis([1, 6, 0, max(y)+5])

  plt.show()

##
# create_trends_chart function
# 
# Creates simple multiline chart from provided set of tweets.
# 
# args: data - set of tweets
# returns: None
#
def create_trends_chart(data):
  # List of all tweets from data source
  tw_list = [datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").date().strftime("%Y-%m-%d") for x in data]
  tw_total = Counter(tw_list)

  tweets = defaultdict(int)

  # Combine tweets by month into tweets list
  for k, v in tw_total.items():
    m = datetime.strptime(k, "%Y-%m-%d").date().strftime("%m")
    if m in tweets:
      tweets[m] += v
    else:
      tweets[m] = v

  tweets = sorted(tweets.items())

  x, y = [t[0] for t in tweets], [t[1] for t in tweets]
  print(x)
  print(y)

  max_y = max(y)
  plt.plot(x, y, "g-", label="tweets")

  # List of tweets containing a hashtag
  hashtags = [{datetime.strptime(x["created_at"], "%a %b %d %H:%M:%S %z %Y").date().strftime("%m") : 
    len(x["entities"]["hashtags"])} for x in data]

  tweets = defaultdict(int)

  for _, li in enumerate(hashtags):
    for k, v in li.items():
      if v == 0: continue
      if k in tweets:
        tweets[k] += v
      else:
        tweets[k] = v

  tweets = sorted(tweets.items())

  x, y = [t[0] for t in tweets], [t[1] for t in tweets]
  print(x)
  print(y)

  if max(y) > max_y: max_y = y

  plt.axis([1, 12, 0, max_y+5])
  plt.plot(x, y, "b-.", label="tweets with hashtags")
  plt.legend(loc=9)
  plt.title("Trends by @merceryou in 2016")
  plt.xlabel("Month")
  plt.ylabel("# of tweets")

  plt.show()

##
# create_retweets_scatter_plot function
# 
# Creates simple scatter plot from provided set of tweets.
# 
# Chart displays number of retweets in July
# 
# args: data - set of tweets
# returns: None
#
def create_retweets_scatter_plot(data):
  # List of all tweets from data source
  tw_list = [(datetime.strptime(x["created_at"], 
    "%a %b %d %H:%M:%S %z %Y").date().strftime("%Y-%m-%d"), 
    x["retweet_count"]) for x in data]

  # List off all tweets in July
  tw_july = [x for x in tw_list if datetime.strptime(x[0], 
    "%Y-%m-%d").date().strftime("%m") == "07"]
  
  tweets = defaultdict(int)

  # Combine tweets by day into tweets list 
  for k,v in tw_july:
    day = datetime.strptime(k, 
      "%Y-%m-%d").date().strftime("%d")
    if day in tweets:
      tweets[day] += v
    else:
      tweets[day] = v

  tweets = sorted(tweets.items())

  x, y = [t[0] for t in tweets], [t[1] for t in tweets]
  print(x)
  print(y)

  plt.scatter([int(x)+0.5 for x in x], [y+0.5 for y in y])

  labels = [str(x) for x in y]

  for label, day, retweets in zip(labels, x, y):
    plt.annotate(label, xy=(day, retweets), 
      xytext=(4, 10), textcoords="offset points")

  plt.axis([1, 31, 0, max(y)+20])
  plt.xticks([int(x)+0.5 for x in x], x)
  plt.ylabel("# of retweets")
  plt.xlabel("Day")
  plt.title("Number of retweets by @merceryou in July 2016")

  plt.show()

##
# create_user_friends_chart function
# 
# Creates simple scatter plot from provided set of tweets.
# 
# Chart displays number of friends for retweeted tweets 
# by @merceryou in March, July, and September. 
# 
# args: data - set of tweets
#       equal_axes - optional, to show misleaded chart
#       
# returns: None
#
def create_user_friends_chart(data, equal_axis=False):
  # List of all tweets from data source
  tw_list = [(x["retweeted_status"]["user"]["screen_name"],
  x["retweeted_status"]["user"]["friends_count"]) for x in data if x["text"][0:3] == "RT " 
  and datetime.strptime(x["created_at"], 
  "%a %b %d %H:%M:%S %z %Y").date().strftime("%m") in ["03", "07", "09"]]
  
  total_users = [Counter(tw_list)]

  names = [] # For list of screen_names
  friends = []
  total_retweets = []

  for _,v in enumerate(total_users):
    for k, v in v.items():
      names.append(k[0])
      friends.append(k[1])
      total_retweets.append(v)

  # Make total number of retweets close to retweets_count for demonstration purposes
  total_retweets = [x-10 for x in friends]

  plt.scatter([x+0.5 for x in total_retweets], friends)

  for label, retweets_count, friends_count in zip(names, total_retweets, friends):
    plt.annotate(label, xy=(retweets_count, friends_count), 
      xytext=(15, -5), textcoords="offset points")

  if equal_axis == True:
    plt.axis("equal")

  plt.ylabel("# of friends")
  plt.xlabel("# of retweets")
  plt.title("Number of friends for retweets by @merceryou in March, July, and September 2016")

  plt.show()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
  args = create_args()
  # Retrieve tweets from data file
  tweets = get_tweets(args.source)

  if tweets is None:
    print("No tweets")
    sys.exit(1)

  # Decode tweets into Python dictionary
  tweets = json.loads(tweets)

  if args.type == "tweets":
    create_tweets_chart(tweets)
  if args.type == "retweets":
    create_retweets_chart(tweets)
  if args.type == "histogram":
    create_tweets_histogram_chart(tweets)
  if args.type == "user-mentions":
    create_user_mentions_chart(tweets)
  if args.type == "user-mentions-incorrect":
    create_user_mentions_chart(tweets, True)
  if args.type == "trends":
    create_trends_chart(tweets)
  if args.type == "retweets-scatter-plot":
    create_retweets_scatter_plot(tweets)
  if args.type == "friends":
    create_user_friends_chart(tweets)
  if args.type == "friends-equal-axis":
    create_user_friends_chart(tweets, True)
