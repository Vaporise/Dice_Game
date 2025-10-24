import random

def main():

    roll_counter = 0

    not_number = True #Created a loop to check for How many dice the player wants to roll.

    while not_number == True:
        print("How many dice do you want to roll?")
        num_of_dice = input()
        try: #This try and except block let's the code convert the string input into an int
            num_of_dice = int(num_of_dice)
            not_number = False
        except ValueError: #If the input doesn't match up to the expected input it gives a error.
            print("This is not a valid number. Please enter an integer.")
    
    
    
    looping = True

    while looping == True: #Keeps the options in a loop until exited via n or N choice

        print("Roll the dice? (y/n):") # First the choice needs to be made
        choice = input()
        if choice.lower() == "y": # if the choice of y is taken regardless of upper or lower case.
            roll_counter += 1
            num_of_dice_to_roll= []
            for die in range(num_of_dice):
                num_of_dice_to_roll.append(random.randint(1,6))
            print(f"The rolls dice are: {','.join(str(x) for x in num_of_dice_to_roll)}") #Formatted to comma seperate the results and annouce them nicely.
        
        elif choice.lower() == "n": #If no is chosen regardless of upper or lower case the game is over so print an message and exit
            looping = False #Exit the while loop
            print("Thanks for playing!")
            print(f"You rolled {roll_counter} times!")
            exit
        else: #If the choice is not yes or no then it is an invalid choice.
            print("Invalid Choice!")

if __name__ == "__main__":
    main()