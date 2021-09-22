# Exercise 40: Modules, Classes, and Objects
# From Python3 The Hard Way by Zed Shaw
# Programmer: Kevin Kelly
# Date: September 21, 2021


# Python is an object-oriented programming language.
# This means there is a construct called a "class" that lets you strucutre your software in a particular Way
# Instantiate just means "create a class"

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally round tha family",
                        "With a pocket full of shells"])

impossible_dream = Song(['To dream the impossible dream',
                    'To fight the unbeatable foe',
                    'To bear with unbearable sorrow',
                    'To run where the brave not go.'])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

impossible_dream.sing_me_a_song()
