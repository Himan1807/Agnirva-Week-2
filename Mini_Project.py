import random
import time

def number_guessing_game():
    print("<----------------Welcome to the Number Guessing Game!----------------->")
    
    # let the player choose the difficulty level
    print("Choose a difficulty level")
    print("1) Easy (1 - 50)")
    print("2) Medium (1 - 100)")
    print("3) Hard (1 - 500)")
    level = int(input("Enter your choice: "))
    if(level == 1):
        rand = random.randint(1, 50)
    elif(level == 2):
        rand = random.randint(1, 100)
    elif(level == 3):
        rand = random.randint(1, 500)
    else:
        print("Medium Level(1-100) by default")
        rand = random.randint(1, 100) # default to Medium level in case of invalid input
    
    attempts = 0
    max_attempts = 10
    while(attempts < max_attempts):
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if(guess == rand):
                print(f"Congrats! You've guessed it in {attempts} attempts")
                return
            elif(guess < rand):
                print("Too low! Try Again")
            else:
                print("Too High! Try Again")
        except ValueError:
            print("Invalid input! Kindly enter a valid choice")
    print(f"You've used all {max_attempts} attempts. The number was {rand}")
            
number_guessing_game()
while(True):
    play_again = input("Do you wish to play again? (yes/no):").lower()
    if(play_again == "yes"):
        number_guessing_game()
    else:
        print("Thank you for playing. Goodbye!")
        break