# Exercise 30: Else and If
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: September 11, 2021

# Type this one and make it work, too
people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")


if trucks > cars:
    print("That's too many many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
