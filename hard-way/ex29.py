# Exercise 29: What if
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: September 1, 2021



# Introduction to the If statement
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("Better world ahead!")

if people > dogs:
    print("The world could be better!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
