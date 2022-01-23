# GOOGLE cannot be used
# You can use documentation:
# https://docs.python.org/3/
# https://docs.djangoproject.com/en/3.1/


# *** TASK 1 ***
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

#Completed this task already in pythonDjangoInterview63-1

# *** TASK 1 END ***


# *** TASK 2 ***
# Let's say we have a dict representing a pair of student name and grade,
# using dict comprehension extract only the student and grade pair that has
# a grade greater than 60:

students = {
    "John": 70,
    "Mark": 55,
    "Ahmad": 81,
    "Sarah": 20,
    "Ivan": 99,
    "Muhammad": 88,
    "Laila": 74,
    "Sven": 45,
}

print({x:y for x,y in students.items() if y>60})

# *** TASK 2 END ***


# *** TASK 3 ***
# Explain the following behavior in Python Interactive shell. (Verbally)
# Use python shell on the right side if needed

"""

Case 1
>>> True, True, True == (True, True, True)
(True, True, False)

Answer: Here, only one comparison is done "True == (True, True, True)" which returns False.
And 1st two True value returns True as usual.

Case 2
>>> False is False in [False]
True

Answer: Here, the command is executed as (False is False) and (False in [False]).
Which becomes True and True. Thus we get True as the return value.

"""

# *** TASK 3 END ***


# *** TASK 4 ***
# Create a function which checks if two strings are anagrams
# (one string can be made from another string by using all the characters of original string exactly once)
# For example: "ship" and "hips", "lovers" and "solver"

def is_anagram(string_one, string_two):
    if(len(string_one)==len(string_two)):
        if(sorted(string_one)==sorted(string_two)):
            return True
        else:
            return False
    else:
        return False

print(is_anagram("ship", "hips")) # returns True
print(is_anagram("lovers", "solver")) # returns True
print(is_anagram("lol", "olo")) # returns False

# *** TASK 4 END ***


# *** TASK 5 ***
# Print out all sundays in current month.

from datetime import date

# weekday == 6 => sunday
daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1,8):
    day = date.today().replace(day=i)
    if day.weekday() == 6:
        while(i<=daysInMonths[date.today().month-1]):
            day = day.replace(day=i)
            print(day)
            i += 7

# *** TASK 5 END ***


# *** TASK 6 ***
# Write a program in Python to check if a sequence is a Palindrome:

"""
def is_palindrome(word: str) -> bool:
    pass

is_palindrome("323") # returns True
is_palindrome("tenet") # returns True
is_palindrome("sequence") # returns False
"""

# Task completed already in pythonDjangoInterview63-1

# *** TASK 6 END ***


# *** TASK 7 ***
# Declare a composite index for fields first_name and last_name

# from django.db import models


# class Customer(models.Model):
# 	first_name = models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)

# Task completed already in pythonDjangoInterview63-1

# *** TASK 7 END ***


# *** TASK 8 ***
# Write Django settings for mysql database

DATABASES = {

}

# Task completed already in pythonDjangoInterview63-1

# *** TASK 8 END ***
