#The goal of this program is to allow a player to play against a computer in a game of hangman.
#Below are some goals on what this program should do
#
# -ask the player for a difficulty
# -have different genres (right now it will be based off animals)
# -have a list of words based off difficulty and chooses at random
# -draws a stick figure whenever a letter is guessed wrong
# -state that there are no more vowels

import random

def AskingForDiff():
    print("Please select a number for the difficulty. Below is the rating.")
    print("1: 3 or 4 letter words")
    print("2: 5 or 6 letter words")
    print("3: 7 or 8 letter words")
    while True:
        try: 
            difficulty = int(input("Select between 1-3: "))
        except ValueError:
            print("Value must be numeric.")
        if difficulty > 3:
            print("Try again.")
        else:
            return difficulty

def WordsByDifficulty(difficulty):
    list1 = ["bear","cat","dog","lion","bird","mole"]
    list2 = ["tiger","badger","crane","eagle","ferret","gerbil"]
    list3 = ["elephant","giraffe","chipmunk","raccoon","ostrich","peacock"]
    if difficulty == 1:
        return random.choice(list1)
    if difficulty == 2:
        return random.choice(list2)
    if difficulty == 3:
        return random.choice(list3)
    

print(WordsByDifficulty(AskingForDiff()))
