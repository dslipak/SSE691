#!/usr/bin/env python

'''

Course: SSE 691
Project: 2
Students: Dmitriy Slipak

Code from Chapter 4 of the "Data science from scratch".
Functions from chapter converted to use NumPy. 

'''

import numpy as np

# vector_add function
# Adds two vectors componentwise
def vector_add(v, w):
  return np.add(v, w)

# vector_add function
# Subtracts two vectors componentwise
def vector_subtract(v, w):
  return np.subtract(v, w)

# vector_sum function
# Creates sum of vectors
def vector_sum(vectors):
  return np.add.reduce(vectors)

# scalar_multiply function
# Multiplies vector v by number c
def scalar_multiply(c, v) :
  return np.multiply(c, v)

# vector_mean function
# Creates vector from componentwise means of vectors
def vector_mean(vectors):
  return scalar_multiply(1/len(vectors), vector_sum(vectors))

# dot function
# Creats dot product of two vectors
def dot(v, w):
  return np.dot(v, w)

# sum_of_squares_np function
# Creares vector's sum of squares
def sum_of_squares(v):
  return np.sum(np.square(v))

# magnitude function
# Computes magnitude (lenght) of a vector
def magnitude(v):
  return np.sqrt(sum_of_squares(v))

# squared_distance
# Computes squared distance btween vectors
def squared_distance(v, w):
  return sum_of_squares(vector_subtract(v, w))

# distance function
# Computes distance betwen vectors
def distance(v, w):
  return magnitude(vector_subtract(v, w))
  # or
  #return np.sqrt(squared_distance(v, w))

## Functions for working with matrices

# shape function
# Gets shape of a matrix
def shape(A):
  return np.shape(A)

# get_row function
# Retrieves row from a matrix
def get_row(A, i):
  return A[i,:]

# get_column function
# Retrieves column from a matrix
def get_column(A, j):
  return A[:,j]

# make_matrix function
# Creates matrix with shape
def make_matrix(num_rows, num_cols, is_diagonal=False):
  if is_diagonal == True:
    return np.matrix(np.eye(num_rows, num_cols, dtype=np.int))
  return np.zeros((num_rows, num_cols), dtype=np.int)
  # or
  #return np.matrix(np.eye(num_rows, num_cols, dtype=np.int)) if is_diagonal == True else np.zeros((num_rows, num_cols), dtype=np.int)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
	# Test vector_add function
  v = np.array([1, 2, 3], np.int)
  w = np.array([4, 5, 6], np.int)

  # Test vectors addition
  print(vector_add(v, w))
  # Test vectors subtraction
  print(vector_subtract(w, v))
  # Test vectors sum
  print(vector_sum([v, w]))
  # Test scalar multiply
  print(scalar_multiply(3, v))
  # Test vector mean
  print(vector_mean([v, w]))
  # Test dot function
  print(dot(v, w))
  # Test vector's sum of squares
  print(sum_of_squares(v))
  # Test vector's magnitude
  print(magnitude(v))
  # Test squared distance between vectors
  print(squared_distance(v, w))
  # Test distance between vectors
  print(distance(v, w))

  # Test shape of the marix
  mx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # a is 3x3 matrix
  print(shape(mx))
  # Test retrieving a row from the matrix
  print(get_row(mx, 2))
  # Test retrieving a column from the matrix
  print(get_column(mx, 1))
  # Test make matrix
  print(make_matrix(3, 3, True))
