import random

list = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ")

computer = random.choice(list)

print("Computer:", computer)

if user == computer:
    print("Match Draw")

elif user == "rock" and computer == "scissors":
    print("You Win")

elif user == "paper" and computer == "rock":
    print("You Win")

elif user == "scissors" and computer == "paper":
    print("You Win")

else:
    print("Computer Wins")