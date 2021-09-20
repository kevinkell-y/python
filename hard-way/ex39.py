# Exercise 39: Dictionaries, Oh Lovely Dictionaries
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: September 20, 2021


# Create a mapping of State to State's Abbreviation
states = {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# Print out some cities
# ----------
print('-' * 10)

print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


# Print some states
# ----------
print("-" * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['California'])


# Use it by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print("-" * 10 )

# Safely get the abbreviation of a state that might not be There
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
