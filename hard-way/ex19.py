# Exercise 19: Functions & Variables
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 27, 2021


# Create a function that takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Format string one parameter, print
    print(f"You have {cheese_count} cheeses!")
    # Format string second parameter, print
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man's that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly: ")
# Call the function w/two numbers as parameters
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# Create new variables, assign them integers
amount_of_cheese = 10
amount_of_crackers = 50

# Use newly created variables as parameters for the original function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside, too:")

# Use math equations as parameters for our function
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
