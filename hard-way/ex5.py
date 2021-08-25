# Exercise 5: More Variables and Printing
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 21, 2021

# Introduction to format Variables'
name = 'Kevin Kelly'
age = 38 # not a lie
weight = 210 # lbs
height = 72 # inches
eyes = 'Brown'
belt = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His belt in Jiu Jitsu is {belt}... forever {belt}")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
