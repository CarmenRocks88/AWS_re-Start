# Python Challenge: This script will write all prime numbers between 1 and 250 to a text file.

# Setting up the text file
import os  # imports the operating system
os.system("touch results.txt")  # creates a text file named results

file = open("results.txt", "w")

# Finding all Prime Numbers

for x in range(2, 250):
    if x == 2 or x == 3 or x == 5:
        file.write(str(x))
        file.write("\n")
    elif x % 5 != 0 and x % 3 != 0 and x % 2 != 0:
        file.write(str(x))
        file.write("\n")

# Closing the file
file.close()

os.system("cat results.txt")
