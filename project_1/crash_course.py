#!/usr/bin/env python

'''

Course: SSE 691
Project: 1
Students: Thuy-Duong Thi Nguyen, Dmitriy Slipak

Code from Chapter 2 of the "Data science from scratch" 
converted to be compatible with Python 3 

'''

##
## Code from Chapter 2 converted to be compatible with Python 3 

# required for integer division in python 2.x
# from __future__ import division # for integer division

from collections import Counter
from functools import partial

import re as regex
import random

class Set:

  def __init__(self, values=None):
    self.dict = {}

    if values is not None:
      for value in values:
        self.add(value)

  def __repr__(self):
    return "Set: " + str(self.dict.keys())

  def add(self, value):
    self.dict[value] = True

  def contains(self, value):
    return value in self.dict

  def remove(self, value):
    del self.dict[value]

def white_space_formatting():
  for i in [1, 2, 3, 4, 5]:
    print(i) # print i in python 2.x
    
    for j in [1, 2, 3, 4, 5]:
      print(j) # print j in python 2.x
      print(i + j) # print i + j in python 2.x

    print(i) # print i in python 2.x

  print("done looping") # print "done looping" in python 2.x

def my_print(message="my default message"):
  print(message) # print message in python 2.x

def exp(base, power):
  return base ** power

def two_to_the(power):
  return exp(2, power)

def doubler(f):
  def g(x):
    return 2 * f(x)
  return g      

def f1(x):
  return x + 1

def f2(x, y):
  return x + y

def magic(*args, **kwargs):
  print("unnamed args:", args)
  print("keyword args:", kwargs)

def other_way_magic(x, y, z):
  return x + y + z

def doubler_correct(f):
  def g(*args, **kwargs):
    return 2 * f(*args, **kwargs)
  return g

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
  white_space_formatting()
  
  # Calling a function
  my_print("hello")
  my_print()

  # Error handling
  try:
    print(0 / 0) # print 0/0 in python 2.x
  except ZeroDivisionError:
    print("cannot divide by zero")  # print "cannot divide by zero"
                    # in python 2.x

  # Regular expressions
  my_regex = regex.compile("[0-9a-zA-Z]+", regex.I)
  my_string = "Appolo 15"
  match = my_regex.match(my_string)
  print(match) # print match in python 2.x

  print(all([
    not regex.match("a", "cat"),
    regex.search("a", "cat"),
    regex.search("c", "cat"),
    3 == len(regex.split("[ab]", "carbs")),
    "R-D-" == regex.sub("[0-9]", "-", "R2D2")
  ]))

  # Integer division
  print(5 / 2) # print 5/2 in python 2.x

  # Tuples
  my_tuple = (1, 2)

  try:
    my_tuple[1] = 3
  except TypeError:
    print("cannot modify a tuple")

  # Dictionaries
  grades = {"Joel" : 80, "Tim" : 95}

  try:
    kates_grade = grades["Kate"]
  except KeyError:
    print("no grade for Kate!")

  # Counter
  document = ("java", "go", "python", "c++", "go")
  word_counts = Counter(document)

  for word, count in word_counts.most_common(10):
    print(word, count) # print word, count in python 2.x

  # while loop
  x = 0
  while x < 10:
    print(x, "is less than 10") # print x, "is less than 10"
                  # in python 2.x
    x += 1

  # for loop
  for x in range(10):
    print(x, "is less than 10") # print x, "is less than 10"
                  # in python 2.x

  # break/continue statements
  for x in range(10):
    if x == 3:
      continue
    if x == 5:
      break
    print(x) # print x in python 2.x

  # Truthiness
  x = None
  print(x == None) # print x == None in python 2.x
  print(x is None) # print x is None in python 2.x

  # Randomness
  random.seed(10)
  print(random.random()) # print random.random() in python 2.x
  random.seed(10)
  print(random.random()) # print random.random() in python 2.x

  up_to_tem = list(range(10)) # up_to_ten = range(10)
                # in python 2.x
  random.shuffle(up_to_tem)
  print(up_to_tem) # print up_to_ten in python 2.x

  # Classes
  s = Set([1, 2, 3, 4, 5])
  s.add(6)
  print(s.contains(6)) # print s.contains(6) in python 2.x
  s.remove(3)
  print(s.contains(3)) # print s.contains(3) in python 2.x

  # Partials
  two_to_the = partial(exp, 2)
  print(two_to_the(3)) # print two_to_the(3) in python 2.x

  square_of = partial(exp, power=2)
  print(square_of(3)) # print square_of(3) in python 2.x

  # args/kwargs
  g = doubler(f1)
  print(g(3)) # print g(3) in python 2.x
  print(g(-1)) # print g(-1) in python 2.x

  g = doubler(f2)
  #print(g(1, 2)) # print g(1, 2) in python 2.x
  
  magic(1, 2, key="word", key2="word2")

  x_y_list = [1, 2]
  z_dict = {"z" : 3}
  print(other_way_magic(*x_y_list, **z_dict))

  g = doubler_correct(f2)
  print(g(1, 2))
