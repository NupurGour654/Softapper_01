import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to end the game: ").lower()

        if player_choice == "quit":
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = decide_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        rounds += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}")

    print("\nGame over!")
    print(f"Final Score after {rounds} rounds - You: {player_score}, Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
