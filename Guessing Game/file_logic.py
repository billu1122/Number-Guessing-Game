import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "game_data.txt")


def file_load():
    try:
        with open(FILE_PATH, "r") as file:
            content = file.read()
            if content:
                score = int(content.split(":")[-1].strip())
                return score
    except (FileNotFoundError, ValueError):
        pass
    return 6

def file_handling(high_score):
    with open(FILE_PATH, "w") as file:
        file.write(f"Your High Score is: {high_score}\n")
    print(f"High Score Stored In: {FILE_PATH}")
    
