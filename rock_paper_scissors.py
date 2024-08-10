import random

def play():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

print(play())