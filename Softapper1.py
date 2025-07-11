import random
from datetime import datetime
import os

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def decide_winner(player_choice, computer_choice):
    """Determines the winner based on player and computer choices."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        while True:
    clear_screen()  
    player_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to end the game: ").lower()

        player_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to end the game: ").lower()

        if player_choice == "quit":
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice.Please enter rock, paper, or scissors")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = decide_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            if player_score == 3:
               print("🔥 You're on fire!")

            print("You are the Winner!")
            player_score += 1
        else:
            print("Computer is the Winner!")
            computer_score += 1

     print(f" Round: {rounds}")
        print(f"Score - You: {player_score}, Computer: {computer_score}")

    print("\nGame over!")
    print(f"Final Score after {rounds} rounds - You: {player_score}, Computer: {computer_score}")
    print("Thanks for playing!")
print("🕒 Game ended at:", datetime.now().strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()
