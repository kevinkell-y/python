# Exercise 18: Names, Variables, Code, Functions
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 26, 2021

# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# This one takes no arguments
def print_none():
    print("I got nothin'.")



print_two("Kevin", "Kelly")
print_two_again("Kevin", "Kelly")
print_one("First!")
print_none()
