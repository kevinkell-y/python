# Exercise 16: Study Drills - Use read to read the file you made in 16.py
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 25, 2021

from sys import argv

script, filename  = argv

print("Opening the file now...\n")
txt = open(filename)

print("Passed checkpoint.\n")

print("Reading the file now...\n")
contents = txt.read() # read is a method, needs attaching to something.

print("Passed checkpoint. \n")

print("Printing the file now...\n")

print(contents)
print("\n")
print("Passed final checkpoint! Hooray!")

# Close opened file
txt.close()
