import random
from logic import *
from file_logic import *

print("Welcome to Our Game\n")

high_score=file_load()

while True:
    Computer_number = random.randint(1, 25)

    game_won, high_score = attempt_logic(Computer_number, high_score)

    
    file_handling(high_score)

    if game_won:
        continue_logic()
    else:
        print(f"You lost the game! The correct number was: {Computer_number}")
        continue_logic()
