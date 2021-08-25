# Exercise 13: Parameters, Unpacking, Variables
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 23, 2021


from sys import argv    # argv stands for "argument variable", is a module or library
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
