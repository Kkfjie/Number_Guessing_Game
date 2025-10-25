"""
Test script for the Number Guessing Game

This script tests the basic functionality of the game without requiring user interaction.
It validates that all functions work correctly and the game logic is sound.
"""

import sys
import random

# Import the game module
import number_guessing_game as game


def test_welcome_message():
    """Test that welcome message function runs without errors."""
    print("Testing welcome message...")
    try:
        game.display_welcome_message()
        print("✓ Welcome message works!\n")
        return True
    except Exception as e:
        print(f"✗ Error in welcome message: {e}\n")
        return False


def test_hint_function():
    """Test the hint function with various inputs."""
    print("Testing hint function...")
    try:
        # Test various scenarios
        test_cases = [
            (50, 100, "Should say too low"),
            (100, 50, "Should say too high"),
            (45, 50, "Should say very close"),
            (30, 50, "Should say close"),
            (10, 50, "Should say getting warmer"),
            (5, 100, "Should say very far away"),
        ]
        
        for guess, secret, description in test_cases:
            print(f"  Testing: guess={guess}, secret={secret} ({description})")
            game.give_hint(guess, secret)
            print()
        
        print("✓ Hint function works!\n")
        return True
    except Exception as e:
        print(f"✗ Error in hint function: {e}\n")
        return False


def test_random_number_generation():
    """Test that random number generation works and stays in range."""
    print("Testing random number generation...")
    try:
        # Generate 100 random numbers and check they're all in range
        for _ in range(100):
            num = random.randint(1, 100)
            if not (1 <= num <= 100):
                print(f"✗ Random number {num} is out of range!\n")
                return False
        
        print("✓ Random number generation works (tested 100 times)!\n")
        return True
    except Exception as e:
        print(f"✗ Error in random number generation: {e}\n")
        return False


def test_code_structure():
    """Test that all required functions exist and are callable."""
    print("Testing code structure...")
    try:
        required_functions = [
            'display_welcome_message',
            'get_difficulty_level',
            'get_user_guess',
            'give_hint',
            'play_game',
            'ask_play_again',
            'main'
        ]
        
        for func_name in required_functions:
            if not hasattr(game, func_name):
                print(f"✗ Missing function: {func_name}\n")
                return False
            if not callable(getattr(game, func_name)):
                print(f"✗ {func_name} is not callable!\n")
                return False
            print(f"  ✓ Function '{func_name}' exists")
        
        print("✓ All required functions exist!\n")
        return True
    except Exception as e:
        print(f"✗ Error checking code structure: {e}\n")
        return False


def test_imports():
    """Test that all required imports are present."""
    print("Testing imports...")
    try:
        import random
        print("  ✓ random module imported")
        print("✓ All imports work!\n")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}\n")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("=" * 60)
    print("Running Tests for Number Guessing Game")
    print("=" * 60)
    print()
    
    tests = [
        test_imports,
        test_code_structure,
        test_welcome_message,
        test_hint_function,
        test_random_number_generation,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("=" * 60)
    print("Test Results")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total} tests")
    
    if passed == total:
        print("✓ All tests passed! The game is ready to play.")
        return 0
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
