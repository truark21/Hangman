#The goal of this program is to allow a player to play against a computer in a game of hangman.
#Below are some goals on what this program should do
#
# -ask the player for a difficulty
# -have a list of words based off difficulty and chooses at random
# -draws a stick figure whenever a letter is guessed wrong
# -state that there are no more vowels

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
            break
    

AskingForDiff()