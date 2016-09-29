#!/usr/bin/env python

'''

Course: SSE 691
Project: 4
Student: Dmitriy Slipak

This script contains set of probabilistic functions
from Chapter 6 using scipy libray. 

'''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from collections import Counter

##
#  Converted code from the chapter

def uniform_pdf(x):
  return stats.uniform.pdf(x)

def uniform_cdf(x):
  return stats.uniform.cdf(x)

def normal_pdf(x, mu=0, sigma=1):
  return stats.norm.pdf(x, mu, sigma)

def normal_cdf(x, mu=0, sigma=1):
  return stats.norm.cdf(x, mu, sigma)

def inverse_normal_cdf(x):
  return stats.norm.ppf(x)

def plot_normal_pdfs(plt):
  xs = [x / 10.0 for x in np.arange(-50, 50)]
  plt.plot(xs,[normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
  plt.plot(xs,[normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
  plt.plot(xs,[normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
  plt.plot(xs,[normal_pdf(x, mu=-1)   for x in xs], '-.', label='mu=-1,sigma=1')
  plt.legend()
  plt.show()

def plot_normal_cdfs(plt):
  xs = [x / 10.0 for x in np.arange(-50, 50)]
  plt.plot(xs,[normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
  plt.plot(xs,[normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
  plt.plot(xs,[normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
  plt.plot(xs,[normal_cdf(x, mu=-1) for x in xs], '-.' , label='mu=-1,sigma=1')
  plt.legend(loc=4) # bottom right
  plt.show()

def binomial(p, n):
  return stats.binom.rvs(n, p)

def make_hist(p, n, num_points):
  data = [binomial(p, n) for _ in np.arange(num_points)]

  # use a bar chart to show the actual binomial samples
  histogram = Counter(data)
  plt.bar([x - 0.4 for x in histogram.keys()],
          [v / num_points for v in histogram.values()],
          0.8,
          color='0.75')

  mu = p * n
  sigma = np.sqrt(n * p * (1 - p))

  # use a line chart to show the normal approximation
  xs = np.arange(min(data), np.max(data) + 1)
  ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
        for i in xs]
  plt.plot(xs, ys)
  plt.show()

##########################################################

def random_kid():
  return np.random.choice(["boy", "girl"])

def family_kids():
  np.random.seed(0)

  both_girls = older_girl = either_girl = 0

  for _ in np.arange(10000):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

  print("P(both | older):", both_girls / older_girl)
  print("P(both | either): ", both_girls / either_girl)

def test_disease():
  samples = 10000
  data = stats.norm.rvs(size=samples)
  res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.99)
  print(res_mean)
  print(res_var)
  print(res_std)

if __name__ == "__main__":
  plot_normal_pdfs(plt)
  plot_normal_cdfs(plt)
  make_hist(0.75, 100, 10000)  
