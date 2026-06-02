# Python Number Guessing Game

This is a terminal-based number guessing game I built in Python. Instead of putting everything into one massive file, I broke it down into separate modules to practice clean code organization and data management.

## How it Works
The project is split into three main files:
* main.py - Runs the main game loop and keeps the game resetting or closing based on user choice.
* logic.py - Handles the actual guessing math, checks if you are too high or too low, and tracks attempts.
* file_logic.py - Opens and writes to a game_data.txt file to save your lowest attempt high score.

## Key Things I Handled
* Multi-file data flow: Handled the challenge of passing variables (like the secret number and high score) safely between different files using function arguments and return statements.
* Error Catching: Wrapped user inputs in a try/except block so if someone types a letter instead of a number, the game explains the mistake instead of crashing.
* No Loop Resets: Fixed scope issues so the game actually remembers your high score across multiple rounds instead of resetting it back to the default value.

## Using AI on this Project
I used AI heavily while building this, but not just to copy-paste code. I used it as a coding partner to debug errors and better understand concepts like local vs global variables, return vehicles, and how files communicate in a multi-module system. 

## How to Run It
Make sure you have Python installed, download the files into the same folder, and run:
python main.py