# Python Concepts Cheat Sheet

Quick reference for the Python concepts used in the Number Guessing Game.

## 📦 Imports

```python
import random  # Import a module
from random import randint  # Import specific function
```

**In our game**: We use `import random` to access random number generation.

---

## 📝 Variables

```python
# Assignment
name = "Player"
age = 25
is_playing = True

# Multiple assignment
x, y, z = 1, 2, 3

# Swap values
a, b = b, a
```

**In our game**: `attempts = 0`, `secret_number = random.randint(1, 100)`, `play_again = True`

---

## 🔢 Data Types

```python
# Integer (whole numbers)
count = 10

# Float (decimal numbers)
price = 19.99

# String (text)
message = "Hello"

# Boolean (True/False)
is_valid = True

# Check type
type(count)  # <class 'int'>
```

**In our game**: We use integers for guesses and attempts, strings for user input, booleans for game control.

---

## 🎯 Functions

```python
# Basic function
def greet():
    print("Hello!")

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Call a function
greet("Alice")
result = add(5, 3)
```

**In our game**: Functions like `display_welcome_message()`, `get_user_guess()`, `play_game()`

---

## 🔄 Loops

### While Loop
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    answer = input("Continue? ")
    if answer == "no":
        break
```

**In our game**: Main game loop uses `while True` and breaks when game ends.

### For Loop
```python
# Loop through range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## ⚖️ Conditional Statements

```python
# If statement
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator (one-liner)
status = "Adult" if age >= 18 else "Minor"
```

**In our game**: We use if-elif-else to check guesses and provide feedback.

---

## 📥 User Input

```python
# Get string input
name = input("Enter your name: ")

# Get integer input
age = int(input("Enter your age: "))

# Get float input
price = float(input("Enter price: "))
```

**In our game**: `guess = int(input("Enter your guess (1-100): "))`

---

## 🎲 Random Numbers

```python
import random

# Random integer in range (inclusive)
num = random.randint(1, 100)

# Random float between 0 and 1
num = random.random()

# Random choice from list
color = random.choice(["red", "green", "blue"])

# Shuffle list
random.shuffle(my_list)
```

**In our game**: `secret_number = random.randint(1, 100)`

---

## 🧮 Operators

### Arithmetic
```python
x + y   # Addition
x - y   # Subtraction
x * y   # Multiplication
x / y   # Division
x // y  # Floor division
x % y   # Modulus (remainder)
x ** y  # Exponentiation
```

### Comparison
```python
x == y  # Equal
x != y  # Not equal
x > y   # Greater than
x < y   # Less than
x >= y  # Greater than or equal
x <= y  # Less than or equal
```

### Logical
```python
x and y  # Logical AND
x or y   # Logical OR
not x    # Logical NOT
```

**In our game**: We use `==` to check if guess equals secret number, `<` and `>` for hints.

---

## 📊 String Formatting

```python
name = "Alice"
age = 25

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# format() method
print("Name: {}, Age: {}".format(name, age))

# % operator (old style)
print("Name: %s, Age: %d" % (name, age))

# String concatenation
print("Name: " + name + ", Age: " + str(age))
```

**In our game**: `print(f"You have {max_attempts} attempts")`

---

## 🛡️ Exception Handling

```python
# Basic try-except
try:
    number = int(input("Enter number: "))
except ValueError:
    print("That's not a number!")

# Multiple exceptions
try:
    result = 10 / x
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Invalid value!")

# Try-except-else-finally
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid!")
else:
    print("Success!")
finally:
    print("This always runs")
```

**In our game**: We use try-except to handle invalid numeric input gracefully.

---

## 📏 String Methods

```python
text = "Hello World"

text.lower()        # "hello world"
text.upper()        # "HELLO WORLD"
text.strip()        # Remove whitespace
text.replace("H", "J")  # "Jello World"
text.split()        # ["Hello", "World"]
text.startswith("H")    # True
text.endswith("d")      # True
"Hello" in text     # True
len(text)           # 11
```

**In our game**: `response.lower()` to normalize yes/no answers.

---

## 🔢 Math Operations

```python
# Absolute value
abs(-5)  # 5

# Power
pow(2, 3)  # 8

# Min/Max
min(1, 2, 3)  # 1
max(1, 2, 3)  # 3

# Round
round(3.7)  # 4
round(3.14159, 2)  # 3.14
```

**In our game**: `difference = abs(guess - secret_number)`

---

## 💡 Common Patterns

### Input Validation Loop
```python
while True:
    try:
        value = int(input("Enter number: "))
        if 1 <= value <= 100:
            break
        print("Out of range!")
    except ValueError:
        print("Invalid input!")
```

### Menu Selection
```python
while True:
    print("1. Option A")
    print("2. Option B")
    choice = input("Choose: ")
    
    if choice == "1":
        # Do A
        break
    elif choice == "2":
        # Do B
        break
    else:
        print("Invalid choice")
```

### Play Again Loop
```python
play_again = True
while play_again:
    # Play game
    response = input("Play again? (y/n): ")
    play_again = response.lower() in ['y', 'yes']
```

---

## 🎯 Best Practices

1. **Use descriptive variable names**: `max_attempts` not `ma`
2. **Add comments for clarity**: Explain WHY, not just WHAT
3. **Keep functions small**: One function = one purpose
4. **Handle errors gracefully**: Use try-except for user input
5. **Use constants for magic numbers**: `MAX_NUMBER = 100` instead of hardcoded 100
6. **Follow PEP 8**: Python's style guide
7. **Test your code**: Run it with different inputs
8. **Use meaningful function names**: `get_user_guess()` is clear

---

## 🐛 Common Mistakes

### 1. Indentation Errors
```python
# Wrong
def my_function():
print("Hello")

# Correct
def my_function():
    print("Hello")
```

### 2. Forgetting to Convert Types
```python
# Wrong
age = input("Age: ")  # age is a string!
if age > 18:  # Error!

# Correct
age = int(input("Age: "))
if age > 18:
```

### 3. Using = Instead of ==
```python
# Wrong (assignment)
if x = 5:

# Correct (comparison)
if x == 5:
```

### 4. Infinite Loops
```python
# Wrong (infinite loop)
while True:
    print("Forever!")

# Correct
count = 0
while count < 10:
    print("Limited")
    count += 1
```

---

## 📚 Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| Variable | `name = value` | `count = 0` |
| Function | `def name():` | `def greet():` |
| If statement | `if condition:` | `if x > 5:` |
| While loop | `while condition:` | `while True:` |
| For loop | `for i in range(n):` | `for i in range(10):` |
| Input | `input("prompt")` | `name = input("Name: ")` |
| Print | `print(value)` | `print("Hello")` |
| Comment | `# comment` | `# This is a comment` |
| Import | `import module` | `import random` |

---

## 🚀 Next Steps

After mastering these concepts:
1. Learn about **lists** and **dictionaries**
2. Explore **file I/O** (reading/writing files)
3. Study **classes** and Object-Oriented Programming
4. Try **list comprehensions** for concise code
5. Learn about **modules** and **packages**

---

**Remember**: The best way to learn is by doing. Write code, break it, fix it, and learn from mistakes! 🐍✨
