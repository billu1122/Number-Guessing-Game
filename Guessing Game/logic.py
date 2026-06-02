def Guessing_Logic(Computer_number, user_number):
    if user_number == Computer_number:
        return "Correct! Congratulations, you won the game"
    elif user_number > Computer_number:
        return "Wrong! You guessed too high"
    elif user_number < Computer_number:
        return "Wrong! You guessed too low"
    
def continue_logic():
    while True:
        continue_choice = input("Do you want to continue? (y/n): ").lower().strip()
            
        if continue_choice in ["y", "yes"]:
            print("Restarting the game.....\n")
            break
        elif continue_choice in ["n", "no"]:
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid Input! Please enter valid choice (y/n)")

def high_score_logic(attempt, high_score):
    used_attempt = attempt + 1
    if used_attempt < high_score:
        high_score=used_attempt
        print("GG! You created a new high score.")
        print(f"Your High Score is: {high_score}")
        return high_score 
    else:
        high_score=used_attempt
        print(f"Your High Score is still: {high_score}")
        return high_score

def attempt_logic(Computer_number,high_score):

     for attempt in range(5):
        try:
            user_number = int(input("Enter your number between 1-25: "))

        except ValueError:
            print("Invalid Input! Please Enter Integer value")
            print(f"Your Number of attempt left is: {4-attempt}") 
            

        message = Guessing_Logic(Computer_number, user_number)
        print(message)
        if user_number != Computer_number:
                print(f"Your Number of attempt left is: {4-attempt}") 
        else:
                print(f"You Won! at your attempt number: {attempt+1}")
                high_score = high_score_logic(attempt, high_score)
                return True, high_score

     return False , high_score
            