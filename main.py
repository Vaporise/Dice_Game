import random

def main():
    
    print("Roll the dice? (y/n):") # First the choice needs to be made
    choice = input()

    if choice is "Y" or "y": # If the choice yes is chosen then there is a loop or while as long as y is chosen.
        while choice is "Y" or "y":
            pass
    elif choice is "n" or "N": #If no is chosen the game is over so print an message and exit
        print("Thanks for playing!")
        exit
    else: #If the choice is not yes or no then it is an invalid choice.
        print("Invalid Choice!")