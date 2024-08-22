import random

def computer_choice():
    game_list = ["rock", "paper", "scissors"]
    return random.choice(game_list)

def player_choice():
    while True:
        player_choice = input("Please enter one of rock, paper or scissors: ").lower().strip()

        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        
        else:
            print("Invalid selection. Please write 'rock', 'paper' or 'scissors'.")

def result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw!"
    
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        return "You won the round!"
    
    else:
        return "You lost the round!"
    
def main():
    print("Welcome To Rock-Paper-Scissors Game")
    players_score = 0
    computers_score = 0

    while True:
        get_player_choice = player_choice()
        get_computer_choice = computer_choice()

        print(f"Your choice: {get_player_choice} - Computer choice: {get_computer_choice}")

        game_result = result(get_player_choice, get_computer_choice)

        print(game_result)

        # for rounds
        if game_result == "You won the round!":
            players_score += 1
            print(f"Your Score: {players_score} | Computer's Score: {computers_score}")
        
        elif game_result == "You lost the round!":
            computers_score += 1
            print(f"Your Score: {players_score} | Computer's Score: {computers_score}")

        else:
            computers_score = computers_score
            players_score = players_score
            print(f"Your Score: {players_score} | Computer's Score: {computers_score}")

        # for the total scores
        if players_score == 3 and players_score > computers_score:
            print("Congratulations! You won the game!")
            playAgain = input("If you want to play again, enter 'YES'. If you want to exit the game, press any key:").upper().strip()

            if playAgain != "YES":
                print("Leaving the game...")
                break
            else:
                computers_score = 0
                players_score = 0

        elif computers_score == 3 and computers_score > players_score:
            print("You lost the game!")
            playAgain = input("If you want to play again, enter 'YES'. If you want to exit the game, press any key:").upper().strip()

            if playAgain != "YES":
                print("Leaving the game...")
                break
            else:
                computers_score = 0
                players_score = 0

if __name__ == "__main__":
    main()