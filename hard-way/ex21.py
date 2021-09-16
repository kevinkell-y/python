# Exercise 21: Functions Can Return Something
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 27, 2021

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b    # Return prints out what the function is doing

def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(105, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway.
print("Here is the puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
