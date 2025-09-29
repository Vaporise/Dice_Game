import random

def main():

    looping = True

    while looping == True: #Keeps the options in a loop until exited via n or N choice

        print("Roll the dice? (y/n):") # First the choice needs to be made
        choice = input()
        if choice.lower() == "y": # if the choice of y is taken regardless of upper or lower case.
            int1 = random.randint(1, 6)
            int2 = random.randint(1, 6)
            print(f"({int1},{int2})")
        
        elif choice.lower() == "n": #If no is chosen regardless of upper or lower case the game is over so print an message and exit
            looping = False #Exit the while loop
            print("Thanks for playing!")
            exit
        else: #If the choice is not yes or no then it is an invalid choice.
            print("Invalid Choice!")

if __name__ == "__main__":
    main()