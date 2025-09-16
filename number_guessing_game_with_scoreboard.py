import random
import math


# Function to play one round of the game
def play_game():
    secret_number = random.randint(1, 50)  # Computer picks a number
    attempts = 0
    max_attempts = 10

    print("\nI have picked a number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        guess = int(input("\nEnter your guess: "))  # type conversion
        attempts += 1

        # Conditionals to check guess
        if guess == secret_number:
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            score = max_attempts - attempts + 1  # higher score if fewer attempts
            return score
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    # If all attempts used
    print(f"❌ Out of attempts! The number was {secret_number}.")
    return 0


# Main program
def main():
    scores = []  # list to store past scores

    print("🎉 Welcome to the Number Guessing Game 🎉")

    while True:
        score = play_game()  # play one round
        scores.append(score)  # store score in list

        # Show scoreboard
        print("\n🎯 Scoreboard so far:", scores)
        print(f"Best score: {max(scores)}")
        print(f"Average score: {math.floor(sum(scores) / len(scores))}")

        # Ask if player wants to play again
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("\n👋 Thanks for playing! See you next time.")
            break


# Run the program
main()
