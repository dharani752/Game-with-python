import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if player_choice in valid_choices:
            break
        else:
            print("Invalid choice. Try again.")

    computer_choice = random.choice(valid_choices)
    print(f"The computer chose: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))

play_game()
