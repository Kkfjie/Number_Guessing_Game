"""
Number Guessing Game
====================
A simple game where the computer picks a random number and the user tries to guess it.
This program demonstrates basic Python programming concepts.

Learning Objectives:
- Variables and data types
- User input
- Random number generation
- Loops (while loops)
- Conditional statements (if/elif/else)
- Functions
- Exception handling
"""

# Import the random module to generate random numbers
# The 'import' statement lets us use code from Python's standard library
import random


def display_welcome_message():
    """
    Display a welcome message to the player.
    
    Functions are reusable blocks of code that perform a specific task.
    They help organize code and make it easier to read and maintain.
    """
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print()


def get_difficulty_level():
    """
    Ask the user to choose a difficulty level.
    
    Returns:
        int: Maximum number of attempts allowed
    """
    print("Choose your difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    print()
    
    # Loop until we get valid input
    while True:
        try:
            # input() function gets text from the user
            # int() converts the text to an integer (whole number)
            choice = int(input("Enter your choice (1-3): "))
            
            # Conditional statements check conditions and execute different code
            if choice == 1:
                return 10  # Easy mode
            elif choice == 2:
                return 7   # Medium mode
            elif choice == 3:
                return 5   # Hard mode
            else:
                # If the number is not 1, 2, or 3, ask again
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            # Exception handling: If user enters non-numeric input, catch the error
            print("Invalid input. Please enter a number (1, 2, or 3).")


def get_user_guess():
    """
    Get a valid guess from the user.
    
    Returns:
        int: The user's guess as an integer
    """
    while True:
        try:
            # Get input and convert to integer
            guess = int(input("Enter your guess (1-100): "))
            
            # Validate that the guess is in the correct range
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a whole number.")


def give_hint(guess, secret_number):
    """
    Provide a hint to the player based on their guess.
    
    Args:
        guess (int): The player's guess
        secret_number (int): The correct number
    """
    # Calculate the difference between guess and secret number
    difference = abs(guess - secret_number)
    
    # Give different hints based on how close the guess is
    if guess < secret_number:
        print("Too low! ", end="")
    else:
        print("Too high! ", end="")
    
    # Provide additional feedback based on how close they are
    if difference > 50:
        print("You're very far away!")
    elif difference > 20:
        print("You're getting warmer...")
    elif difference > 10:
        print("You're close!")
    else:
        print("You're very close!")


def play_game():
    """
    Main game logic - this is where the actual game happens.
    
    Returns:
        bool: True if player wants to play again, False otherwise
    """
    # Display welcome message
    display_welcome_message()
    
    # Get difficulty level (number of attempts)
    max_attempts = get_difficulty_level()
    
    # Generate a random secret number between 1 and 100
    # random.randint(a, b) returns a random integer between a and b (inclusive)
    secret_number = random.randint(1, 100)
    
    # Initialize the attempt counter
    attempts = 0
    
    print(f"\nGreat! You have {max_attempts} attempts to guess the number.")
    print("Let's begin!\n")
    
    # Main game loop - continues until player wins or runs out of attempts
    # while True creates an infinite loop that we'll break out of when needed
    while True:
        # Increment the attempt counter
        attempts += 1
        
        # Show current attempt number
        print(f"\nAttempt {attempts} of {max_attempts}")
        
        # Get the player's guess
        guess = get_user_guess()
        
        # Check if the guess is correct
        if guess == secret_number:
            # Player won!
            print("\n" + "=" * 50)
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            print("=" * 50)
            return ask_play_again()
        else:
            # Wrong guess - give a hint
            give_hint(guess, secret_number)
            
            # Check if player has run out of attempts
            if attempts >= max_attempts:
                # Game over - player lost
                print("\n" + "=" * 50)
                print(f"Game Over! You've used all {max_attempts} attempts.")
                print(f"The number was: {secret_number}")
                print("=" * 50)
                return ask_play_again()


def ask_play_again():
    """
    Ask the player if they want to play again.
    
    Returns:
        bool: True if player wants to play again, False otherwise
    """
    while True:
        # Get user input and convert to lowercase for easier comparison
        response = input("\nWould you like to play again? (yes/no): ").lower()
        
        # Check if response starts with 'y' (yes) or 'n' (no)
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """
    Main function - the entry point of the program.
    This is the first function that runs when you execute the program.
    """
    # Variable to control the game loop
    play_again = True
    
    # Keep playing while player wants to continue
    while play_again:
        play_again = play_game()
    
    # Thank the player for playing
    print("\nThank you for playing! Goodbye! 👋")


# This special condition checks if this file is being run directly
# (not imported as a module). If true, it runs the main() function.
# This is a Python convention for making files that can be both run and imported.
if __name__ == "__main__":
    main()
