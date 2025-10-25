# Quick Start Guide

## How to Run the Game

### Method 1: Direct Execution
```bash
python number_guessing_game.py
```

### Method 2: Using Python 3
```bash
python3 number_guessing_game.py
```

### Method 3: Run Tests First
To verify everything works before playing:
```bash
python3 test_game.py
python3 number_guessing_game.py
```

## Understanding the Game Files

| File | Purpose |
|------|---------|
| `number_guessing_game.py` | The main game code with extensive comments |
| `TUTORIAL.md` | Comprehensive learning guide explaining Python concepts |
| `test_game.py` | Automated tests to verify the game works correctly |
| `README.md` | Project overview and quick reference |
| `QUICKSTART.md` | This file - how to get started quickly |

## Game Controls

1. **Choosing Difficulty**: Type `1`, `2`, or `3` and press Enter
   - 1 = Easy (10 attempts)
   - 2 = Medium (7 attempts)
   - 3 = Hard (5 attempts)

2. **Making a Guess**: Type any number from 1-100 and press Enter

3. **Play Again**: Type `yes` or `y` to play again, `no` or `n` to quit

## Example Game Session

Here's what you'll see when you play:

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

Attempt 3 of 7
Enter your guess (1-100): 62
Too low! You're very close!

Attempt 4 of 7
Enter your guess (1-100): 68
Too high! You're very close!

Attempt 5 of 7
Enter your guess (1-100): 65

==================================================
🎉 Congratulations! You guessed it in 5 attempts!
==================================================

Would you like to play again? (yes/no): no

Thank you for playing! Goodbye! 👋
```

## Tips for Playing

1. **Use Binary Search Strategy**: Start with 50, then adjust by half each time
2. **Pay Attention to Hints**: They tell you how close you are
3. **Keep Track**: Remember your previous guesses to narrow down the range
4. **Practice Different Difficulties**: Start with Easy, then challenge yourself

## Learning Path

1. **First**: Just play the game a few times to understand how it works
2. **Second**: Open `number_guessing_game.py` and read through the comments
3. **Third**: Read `TUTORIAL.md` to understand the Python concepts in depth
4. **Fourth**: Try the exercises in the tutorial to modify the game
5. **Fifth**: Create your own variations and improvements

## Troubleshooting

### Problem: "python: command not found"
**Solution**: Try `python3` instead of `python`

### Problem: "No module named 'random'"
**Solution**: The `random` module is part of Python's standard library. This error suggests Python isn't installed correctly. Reinstall Python.

### Problem: Game doesn't accept my input
**Solution**: Make sure you're typing just the number and pressing Enter. Don't include any other characters.

### Problem: "EOFError" when running
**Solution**: This happens when the program runs out of input. This is normal when testing with piped input. Just run it normally: `python3 number_guessing_game.py`

## What to Learn Next

After mastering this game, try:
- Adding a scoring system
- Creating a two-player version
- Building other games (Rock-Paper-Scissors, Hangman)
- Learning about Python lists and dictionaries
- Exploring file I/O to save high scores

## Need Help?

- Check the comments in `number_guessing_game.py`
- Read the detailed explanations in `TUTORIAL.md`
- Look up error messages online (they're very helpful!)
- Experiment! The best way to learn is by trying things

Happy coding! 🐍🎮
