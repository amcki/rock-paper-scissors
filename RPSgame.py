import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if beats[player] == computer:
        return "You win!"
    else:
        return "Computer wins!"

def play():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice, try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(get_winner(player_choice, computer_choice))
        print()

if __name__ == "__main__":
    play()