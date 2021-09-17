# Exercise 32: Loops & Lists
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: September 16, 2021

# LISTS in Python are Arrays in Ruby (and many other languages)
# Now we build some LISTS using for-loops to cycle through and print them out
the_count = [1, 2, 3, 4, 5];
fruits = ['apples', 'oranges', 'pears', 'apricots'];
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'];


# For Loop
for number in the_count:
    print(f"This is count {number}")


# Another For Loop
for fruit in fruits:
    print(f"A fruit of type: {fruit}")


# Also we can go through mixed lists too
# Notice we have to use {} since we don't know what's in it.
for i in change:
    print(f"I got {i}")


# We can also build lists, first start with an empty one.
elements = []


# We can use the range function to add numbers to a list
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # Append each new number to the newly created "elements" list
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
