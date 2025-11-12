import random

list1 = ["rock", "paper", "scissors"]
print("Welcome to Rock-Paper-Scissors!")

# Player input
choice = input("Choose rock, paper, or scissors: ")
print(f"You chose: {choice}")

print(f"Computer chose: {random.choice(list1)}")