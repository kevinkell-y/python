# Exercise 20: Functions & Files
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 27, 2021


from sys import argv

script, input_file = argv

# Create a function that calls a method to read file input
def print_all(f):
    print(f.read())

# Not sure?
def rewind(f):
    f.seek(0)

# Create a function that reads one line at a time
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Get the file from input, store it in the current_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# Call the print function, print out the whole file.
print_all(current_file)

print("Now let's rewind, kind like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Print out a single line
current_line = 1
print_a_line(current_line, current_file)

# Add one to the print-line variable and print it out.
current_line = current_line + 1
print_a_line(current_line, current_file)

# Samsies.
current_line = current_line + 1
print_a_line(current_line, current_file)
