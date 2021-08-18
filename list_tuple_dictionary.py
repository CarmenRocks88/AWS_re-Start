# List, Tuple, Dictionary

# Exercise 1: The List Data Type - Creating a List

"""
To create a list

1) Give the list a meaningful name.
2) Enter all items in the list with [].
3) Strings of data should be in " ".
"""

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Accessing a list by Position

""" 
List position starts at zero.
add brackets to list name [] with the position you are trying to pull.
"""

print(myFruitList[0])
print(myFruitList[2])

# Changing the Values in a List

myFruitList[2] = "orange"
print(myFruitList)

# Exercise 2: The Tuple Data Type

"""
What is a tuple? A tuple is similar to a list but it cannot be changed after creation. It is "immutable".
Tuples are created with () instead of brackets.
"""
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Access a Tuple by Position

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# The Dictionary Data Type

""" A dictionary is a list with named positions (keys). Think of keys as identifiers.

Dictionaries use curly brackets {}. 
Each item pair are linked by colons (:) and separated by commas (,).

"""

myFavoriteFruitDictionary = {
    "Adam": "apple",
    "Ben": "banana",
    "Penny": "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Access a Dictionary by Name
print(myFavoriteFruitDictionary["Adam"])
print(myFavoriteFruitDictionary["Ben"])
print(myFavoriteFruitDictionary["Penny"])
