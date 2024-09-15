import random
rps = ["rock", "paper", "scissors"]

player_choice = input("What would you like, rock, paper, or scissors? ").lower().strip()
score = 0

while True:
    while True:
        if player_choice in rps:
            break
        else:
            player_choice = input("Please choose rock, paper, or scissors! ").lower().strip()

    process = random.randint(0,2)
    cpu_choice = rps[process]

    stages = [
    f"You beat me, I threw {cpu_choice}",
    f"You lost to me, I threw {cpu_choice}",
    f"You tied with me, I threw {cpu_choice}"
]
    if player_choice == rps[0] and cpu_choice == rps[2]:
        print(stages[0])
        score += 1
    if player_choice == rps[0] and cpu_choice == rps[1]:
        print(stages[1])
    if player_choice == rps[0] and cpu_choice == rps[0]:
        print(stages[2])

    if player_choice == rps[1] and cpu_choice == rps[0]:
        print(stages[0])
        score += 1
    if player_choice == rps[1] and cpu_choice == rps[2]:
        print(stages[1]) 
    if player_choice == rps[1] and cpu_choice == rps[1]:
        print(stages[2]) 

    if player_choice == rps[2] and cpu_choice == rps[1]:
        print(stages[0])
        score += 1
    if player_choice == rps[2] and cpu_choice == rps[0]:
        print(stages[1])
    if player_choice == rps[2] and cpu_choice == rps[2]:
        print(stages[2])

    print(score)

    rematch = input("Want a rematch or no? ").lower()
    if rematch == "no":
        break
        
if score < 0:
    score = 0

print(score)