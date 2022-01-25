# GOOGLE cannot be used
# You can use documentation:
# https://docs.python.org/3/
# https://docs.djangoproject.com/en/3.1/


# *** TASK 1 ***
# Define a property called *prop* on
# class MyClass without using a decorator (with setter, getter and deleter)

# Completed already

# *** TASK 1 END ***


# *** TASK 2 ***
# Using argparse create a command that takes space separated numbers
# and returns it is sum if the argument -s was provided and its multiplication
# if the argument -m was provided

import argparse

parser = argparse.ArgumentParser(description='Sum or Mul')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-s', dest='sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers')
parser.add_argument('-m', dest='mult')

args = parser.parse_args()
if args.mult:
  mult = args.integers[0]
  for i in range(1, len(args.integers)):
    mult *= args.integers[i]
  print(mult)
else:
  print(args.sum(args.integers))

# *** TASK 2 END ***


# *** TASK 3 ***
# Extract Emails from the file in the following directory, please be aware
# that there might be duplicate emails
# Sample from file:
"""
From cwen@iupui.edu Thu Jan  3 16:23:48 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.91])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 16:23:48 -0500
...
Author: ray@media.berkeley.edu
Date: 2008-01-03 17:05:11 -0500 (Thu, 03 Jan 2008)
New Revision: 39745
...
Author: louis@media.berkeley.edu
Date: 2008-01-03 17:16:39 -0500 (Thu, 03 Jan 2008)
New Revision: 39746
...
"""

file = "inbox.txt"

with open(file, 'r') as f:
  for line_str in f.readlines():
    for token in line_str.split():
      clean_token = token.rstrip('>').lstrip('<')
      pos = clean_token.find('@')
      if pos > 0 and pos < len(clean_token):
        print(clean_token)

#print(data.split())

# *** TASK 3 END ***



# *** TASK 4 ***

# Flatten this list of lists:
# output should be: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# nested_list = [[1, [2, 3], 4], [5, 6, 7], [8, 9], 10]


# *** TASK 4 END ***



# *** TASK 5 ***

# Let's say we have this list of elements, remove the duplicate elements:


# elements = ["foo", "bar", "bar", "foo", "tar", "foo", "tar"]


# *** TASK 5 END ***



# *** TASK 6 ***

# Transform uppercase chars to lowercase and vice-versa
# So following will become "AAbbccJJiiAAAmmMMLLlllLIIOIS"


# s = "aaBBCCjjIIaaaMMmmllLLLliiois"

# def transform(input):
#     pass

# print(transform(s) == "AAbbccJJiiAAAmmMMLLlllLIIOIS") # returns True


# *** TASK 6 END ***


# *** TASK 7 ***

# Write a Django view to render an HTML template called index.html
# that will display all the objects from a model called Home.


# def index(
#         # write params here
#         ):
#     pass


# *** TASK 7 END ***



# *** TASK 8 ***

# Declare a composite index for fields first_name and last_name


# from django.db import models


# class Customer(models.Model):
# 	first_name = models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)

# # *** TASK 8 END ***
