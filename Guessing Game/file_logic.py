import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "game_data.txt")


def file_load():
    with open("Game_data.txt", "w") as file:
        try:
            with open(FILE_PATH, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            pass

def file_handling(high_score):
    with open(FILE_PATH, "w") as file:
        file.write(f"Your High Score is: {high_score}\n")
    print(f"High Score Stored In: {FILE_PATH}")
    