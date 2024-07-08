# "Guess the Number" game using binary search 
#
# Author: Gurnoor Singh Saini

import random

def guess_game():
    
    target_number = random.randint(1, 50)
    
    lower_bound = 1
    upper_bound = 50
    max_attempts = 10
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        
        guess = (lower_bound + upper_bound) // 2
        
        print(f"Attempt {attempts}:")
        user_guess = int(input("Guess the number between 1 to 50: "))

        if user_guess == target_number:
            print("Congratulations! You guessed the number")
            break
        
        elif user_guess < target_number:
            print("Too low! Try again")
            lower_bound = user_guess + 1
        
        else:
            print("Too high! Try again")
            upper_bound = user_guess - 1

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXX GUESS GAME XXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
guess_game()