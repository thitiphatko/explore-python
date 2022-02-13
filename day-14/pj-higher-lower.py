from art import logo, vs
from game_data import data
import random
from wiper import wipe


def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display logo
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Generate random accounts from data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"A: {format_data(account_a)}.")
    print(vs)
    print(f"B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower account for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    wipe
    print(logo)

    # Give player a feedback
    if is_correct:
        score += 1
        print(f"You got it right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, you got it wrong. Final score: {score}")
