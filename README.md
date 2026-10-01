# Number Guessing Game

A command-line Number Guessing Game built with Python. The player selects a difficulty level, and the program generates a random number within a specific range. The player then tries to guess the number while receiving hints about whether the guess is too high or too low.

The game also keeps track of the number of attempts and provides limited attempts for the Medium and Hard difficulty levels.

## Project Type

**Type:** Command-Line Interface (CLI) Application

**Level:** Level 1 Python Project

**Language:** Python

## Features

- Three difficulty levels:
  - Easy
  - Medium
  - Hard
- Random number generation
- Different number ranges based on difficulty
- User input for guesses
- Attempt counter
- Limited attempts for Medium and Hard levels
- Hints when the guessed number is too high or too low
- Success message when the correct number is guessed
- Error handling for invalid numeric input
- Displays remaining attempts
- Automatically ends the game when the maximum attempts are reached

## Difficulty Levels

### Easy

- Random number range: 1 - 50
- Unlimited attempts
- Provides hints when the guess is too high or too low

### Medium

- Random number range: 1 - 100
- Maximum attempts: 10
- Displays the current attempt number
- Displays the number of remaining attempts

### Hard

- Random number range: 1 - 500
- Maximum attempts: 5
- Displays the current attempt number
- Displays the number of remaining attempts

## How the Game Works

When the program starts, the player is asked to select a difficulty level:



Enter your difficulty level

For Easy press 1
For Medium press 2
For Hard press 3

## Error Handling

The program uses try and except to handle invalid input.

If the player enters something that cannot be converted into an integer, the program displays an error message instead of crashing.

Enter numbers only!!

## Technologies Used
Python
Python random module
Command-Line Interface (CLI)

## Python Concepts Used
Variables
User input using input()
Type conversion using int()
if, elif, and else statements
while loop
try-except exception handling
ValueError
break
continue
Comparison operators
Incrementing variables
Random number generation using random.randint()

## Project Structure

Number-Guessing-Game/
│
├── number_guessing.py
└── README.md