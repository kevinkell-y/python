# Exercise 4: Variables and Names
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: August 21, 2021


# Create a variable named cars and give it a value 100
cars = 100

# Create a variable for the seats in the cars
space_in_a_car = 4.0

# Create a variable for the total number of drivers
drivers = 30

# Create a variable for the total number of passengers
passengers = 90

# Find the number of cars not driven by drivers
cars_not_driven = cars - drivers

# Find the number of cars driven by drivers
cars_driven = drivers

# Figure out the carpool sitation
carpool_capacity = cars_driven * space_in_a_car

# Find avg. number per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
