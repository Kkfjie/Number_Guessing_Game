# Number Guessing Game 🎯

A beginner-friendly Python project for learning basic programming concepts!

## 📖 Description

This is a simple number guessing game where the computer randomly selects a number between 1 and 100, and the player tries to guess it. The game includes:

- Three difficulty levels (Easy, Medium, Hard)
- Smart hints to guide you to the answer
- Multiple rounds with replay option
- Input validation and error handling

## 🎮 How to Play

1. The computer thinks of a random number between 1 and 100
2. Choose your difficulty level (affects number of attempts)
3. Try to guess the number
4. Get hints after each guess (too high/too low, distance feedback)
5. Win by guessing correctly, or run out of attempts

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your computer
- No additional libraries needed (uses only Python standard library)

### Running the Game

```bash
# Navigate to the project directory
cd Number_Guessing_Game

# Run the game
python number_guessing_game.py
```

Or on some systems:
```bash
python3 number_guessing_game.py
```

## 📚 Learning Resources

This project is designed to help you learn Python basics. Check out:

- **[TUTORIAL.md](TUTORIAL.md)** - Comprehensive guide explaining every concept used in the code
- **number_guessing_game.py** - Well-commented code with explanations

### Concepts Covered

- ✅ Variables and data types
- ✅ Functions and return values
- ✅ User input handling
- ✅ Loops (while loops)
- ✅ Conditional statements (if/elif/else)
- ✅ Random number generation
- ✅ Exception handling
- ✅ String formatting

## 🎯 Example Game Session

```
==================================================
Welcome to the Number Guessing Game!
==================================================
I'm thinking of a number between 1 and 100.
Can you guess what it is?

Choose your difficulty level:
1. Easy (10 attempts)
2. Medium (7 attempts)
3. Hard (5 attempts)

Enter your choice (1-3): 2

Great! You have 7 attempts to guess the number.
Let's begin!

Attempt 1 of 7
Enter your guess (1-100): 50
Too low! You're getting warmer...

Attempt 2 of 7
Enter your guess (1-100): 75
Too high! You're close!

...
```

## 💡 Ideas for Enhancement

Want to practice more? Try adding these features:

- Keep track of player statistics (games won/lost, average attempts)
- Add a scoring system based on attempts used
- Implement a two-player mode
- Save high scores to a file
- Add hints that cost attempts
- Create a GUI version using tkinter

## 🤝 Contributing

This is a learning project! Feel free to:
- Experiment with the code
- Try the exercises in TUTORIAL.md
- Create your own variations
- Share improvements

## 📝 License

This project is open source and available under the MIT License.

## 🌟 Happy Learning!

Remember: The best way to learn programming is by doing. Don't just read the code—run it, modify it, break it, and fix it! 
