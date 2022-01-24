# GOOGLE cannot be used
# You can use documentation:
# https://docs.python.org/3/
# https://docs.djangoproject.com/en/3.1/


# *** TASK 1 ***
# Print out all sundays in current month.

# Completed in pythonDjangoInterview63-1

# *** TASK 1 END ***


# *** TASK 2 ***
# replace each number of the following list of number with it is squared root

from math import sqrt

numbers = [4, 64, 81, 144, 16, 9]

numbers = [int(sqrt(x)) for x in numbers]

print(numbers)

# *** TASK 2 END ***


# *** TASK 3 ***
# Let's say we have the following list of class Foo objects,
# sort it in descending order based on the attribute x:

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

foo_objects = [
    Foo(8, 1),
    Foo(12, 7),
    Foo(11, 19),
    Foo(0, 2),
    Foo(5, 14)
]

foo_objects = sorted(foo_objects, key=lambda a:a.x)

# *** TASK 3 END ***


# *** TASK 4 ***
# Define a property called *prop* on
# class MyClass without using a decorator (with setter, getter and deleter)

class MyClass:
    def __init__(self):
        self._prop = None

    def get_prop(self):
        return self._prop

    def set_prop(self, value):
        self._prop = value

    def del_prop(self):
        del self._prop

# *** TASK 4 END ***


# *** TASK 5 ***
# convert this camel case string to snake case string

text = "TheQuickBrownFoxJumpsOverTheLazyDog"

snakeText = []

for x in text:
    if x.isupper():
        snakeText.append(x.lower())
    else:
        snakeText.append(x.upper())

print(''.join(snakeText))

# *** TASK 5 END ***



# *** TASK 6 ***
# Let's say we have the following list of class Bar objects,
# remove the duplicate objects:

class Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

duplicate_foo_objects = [
    Bar(1, 1),
    Bar(2, 2),
    Bar(1, 1),
    Bar(1, 1),
    Bar(2, 2),
    Bar(2, 2),
    Bar(3, 3),
    Bar(3, 3)
]

no_duplicate_foo_objects = []

for x in duplicate_foo_objects:
    count = 0
    for y in no_duplicate_foo_objects:
        if (x.x == y.x and x.y == y.y):
            count += 1
    if count == 0:
        no_duplicate_foo_objects.append(x)

print(no_duplicate_foo_objects)

# *** TASK 6 END ***


# *** TASK 7 ***
# using Django GenericViews implement a class view for rendering
# an HTML template called index.html that will display all the objects
# from a model called Home.

class ListHomeObjects():
    pass

# *** TASK 7 END ***


# *** TASK 8 ***
# Write Django settings for mysql database

DATABASES = {

}

# Completed in pythonDjangoInterview63-1

# *** TASK 8 END ***
