# Exercise 15: Reading Files
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 25, 2021

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
