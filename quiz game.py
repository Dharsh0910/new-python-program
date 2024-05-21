import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to the Guessing Game!")
    print("I've selected a number between 1 and 100. You have 10 attempts to guess it.")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        guess = int(input("Enter your guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        
        attempts -= 1
    
    if attempts == 0:
        print("\nGame over! You've run out of attempts. The correct number was:", secret_number)

guessing_game()
