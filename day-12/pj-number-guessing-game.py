###Number Guessing Game###

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Include an ASCII art logo.
from art import logo
print(logo)

turns = 0
#feedback to user
def check_answer(guess, answer, turns):
    """Check answer agains guess. Return the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#select difficulty
def set_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, {answer}")

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")

game()
