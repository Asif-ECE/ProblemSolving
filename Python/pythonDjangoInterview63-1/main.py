# GOOGLE cannot be used
# You can use documentation:
# https://docs.python.org/3/
# https://docs.djangoproject.com/en/3.1/


# *** TASK 1 ***
# Convert a given string to all uppercase if it contains at least
# 2 uppercase characters in the first 4 characters

def to_uppercase(string: str) -> str:
    count = 0
    ranged = 3
    
    #Find count of upperCased characters
    for j in range(len(string)):
        if(j>ranged):
            break
        if(string[j].isupper()):
            count+=1
            
    #Decision making
    if(count>1):
        return(string.upper())
    else:
        return(string)

print(to_uppercase("PyTHon")) # returns PYTHON
print(to_uppercase("PyThon")) # returns PyThon

# *** TASK 1 END ***


# *** TASK 2 ***
# write code to print the following pattern

def show_pattern(rc:int):
    for i in range(1,rc+1):
        print(" "*(rc-i)+"*"*i)

show_pattern(5) # prints out the pattern given below

"""
    *
   **
  ***
 ****
*****
"""

# *** TASK 2 END ***


# *** TASK 3 ***
# Using argparse create a command that takes space separated numbers
# and returns it is sum if the argument -s was provided and its multiplication
# if the argument -m was provided

import argparse


def multiply(lst:list)->int: #function to multiply numbers in a list
    i = 1
    for j in lst:
        i *= j
    return i

def sum(lst:list)->int: #function to sum numbers in a list
    i = 0
    for j in lst:
        i += j
    return i

parser = argparse.ArgumentParser(description='Processing integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('-s', '--sum', dest='summation', action='store_true')
parser.add_argument('-m', '--mul', dest='multiply', action='store_true')

args = parser.parse_args()

if(args.summation):
    print(sum(args.integers))
elif(args.multiply):
    print(multiply(args.integers))

# *** TASK 3 END ***


# *** TASK 4 ***
# Sample from file:
"""
write a method to get baby names from the files in the following directory,
then print to 3 frequent names

...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
"""

directory = "baby_names/"

# *** TASK 4 END ***

"""
# *** TASK 5 ***
# Write a program in Python to check if a sequence is a Palindrome:

def is_palindrome(word: str) -> bool:
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

print(is_palindrome("323")) # returns True
print(is_palindrome("tenet")) # returns True
print(is_palindrome("sequence")) # returns False

# *** TASK 5 END ***


# *** TASK 6 ***
# Remove duplicate dictionary elements (by name).

student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
}

def removeDup(stdDict:dict)->dict:
    x = list(stdDict)
    uniqueNames = []
    for i in x:
        if stdDict[i]['name'] in uniqueNames:
            del stdDict[i]
        else:
            uniqueNames.append(stdDict[i]['name'])
    print(stdDict)
    return stdDict

removeDup(student_data)

# *** TASK 6 END ***


# *** TASK 7 ***
# Write Django settings for mysql database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbName',
        'USER': 'userName',
        'PASSWORD': 'userPassword',
        'HOST': 'localhost',
        'PORT': ''
    }
}

# *** TASK 7 END ***


# *** TASK 8 ***
# Declare a composite index for fields first_name and last_name

from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]

# *** TASK 8 END ***
"""
