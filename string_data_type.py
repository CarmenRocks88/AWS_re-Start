# String Data Type

# Exercise 1: The String Data Type

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of data type " + str(type(myString)))

# Exercise 2: String Concatenation (Combining two strings into one)

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Exercise 3: Input String

name = input("What is your name?")
print(name)

# Exercise 4: Format Output String

color = input("What is your favorite color?")
animal = input("What is your favorite animal?")
print("{}, you like a {} {}!".format(color, name, animal))
