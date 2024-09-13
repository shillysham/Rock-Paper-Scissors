import random
import re
options = ["rock", "paper", "scissors"]
rps = random.randint(0,2)
score = 0

cpu_choice = options[rps]

while True:
    player_choice = input("Rock, paper or scissors? ").lower()
    if player_choice not in options:
        print("Please input a valid choice: rock, paper, or scissors.")
    else:
        break

if cpu_choice == options[0] and player_choice == options[1]:
    print(f"You won! I picked {cpu_choice}")
    score += 1
elif cpu_choice == options[0] and player_choice == options[0]:
    print(f"We tied! I picked {cpu_choice}")
elif cpu_choice == options[0] and player_choice == options[2]:
    print(f"I won! I picked {cpu_choice}")
    score -= 1

if cpu_choice == options[1] and player_choice == options[2]:
    print(f"You won! I picked {cpu_choice}")
    score += 1
elif cpu_choice == options[1] and player_choice == options[1]:
    print(f"We tied! I picked {cpu_choice}")
elif cpu_choice == options[1] and player_choice == options[0]:
    print(f"I won! I picked {cpu_choice}")
    score -= 1

if cpu_choice == options[2] and player_choice == options[0]:
    print(f"You won! I picked {cpu_choice}")
    score += 1
elif cpu_choice == options[2] and player_choice == options[2]:
    print(f"We tied! I picked {cpu_choice}")
elif cpu_choice == options[2] and player_choice == options[1]:
    print(f"I won! I picked {cpu_choice}")
    score -= 1
    
print(cpu_choice)
print((abs((score))))