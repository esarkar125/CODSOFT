import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize scores
user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game")
    print("Choose: rock, paper, scissors, or quit")

    # User input
    user_choice = input("Your choice: ").lower()
    if user_choice == "quit":
        break

    # Computer choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    # Display the result
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)
    print(f"Your Score: {user_score}, Computer Score: {computer_score}")

# Game over
print("\nGame Over")
print(f"Final Score - You: {user_score}, Computer: {computer_score}")