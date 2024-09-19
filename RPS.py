import random
rps = ["rock", "paper", "scissors"]

gamemode = input("Say duo for local play, say anything else for computer play: " )
best_of = input("Do you want to do best of 3, 5, or infinite? Say 3, 5, or inf.")
score = 0
games = 0


rps = ["rock", "paper", "scissors"]

if gamemode == "duo" or gamemode == "Duo":
    p2wins = 0
    p1wins = 0
    print("You chose local co-op!")
    
    while True:
        player_choice = input("1: What would you like, rock, paper, or scissors? ").lower().strip()
        while player_choice not in rps:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            player_choice = input("1: Please choose rock, paper, or scissors! ").lower().strip()

        player2_choice = input("2: What would you like, rock, paper, or scissors? ").lower().strip()
        while player2_choice not in rps:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            player2_choice = input("2: Please choose rock, paper, or scissors! ").lower().strip()

        if player_choice == rps[0] and player2_choice == rps[2]:
            print("Player one won!")
            p1wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[0] and player2_choice == rps[1]:
            print("Player two won!")
            p2wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[0] and player2_choice == rps[0]:
            print("Tied!")
            if best_of != "inf":
                games += 1
        elif player_choice == rps[1] and player2_choice == rps[0]:
            print("Player one won!")
            p1wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[1] and player2_choice == rps[2]:
            print("Player two won!")
            p2wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[1] and player2_choice == rps[1]:
            print("Tied!")
            if best_of != "inf":
                games += 1

        elif player_choice == rps[2] and player2_choice == rps[1]:
            print("Player one won!")
            p1wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[2] and player2_choice == rps[0]:
            print("Player two won!")
            p2wins += 1
            if best_of != "inf":
                games += 1
        elif player_choice == rps[2] and player2_choice == rps[2]:
            print("Tied!")
            if best_of != "inf":
                games += 1

        if best_of == "inf":
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()
            if play_again != 'yes':
                if p1wins > p2wins:
                    print(f"Well done, Player one. You won and you have {p1wins} wins!")
                elif p2wins > p1wins:
                    print(f"Well done, Player two. You won and you have {p2wins} wins!")
                else:
                    print("You both tied, well played.")
                break

        elif best_of == "3" and games == 3:
                if p1wins > p2wins:
                    print(f"Well done, Player one. You won and you have {p1wins} wins!")
                elif p2wins > p1wins:
                    print(f"Well done, Player two. You won and you have {p2wins} wins!")
                else:
                    print("You both tied, well played.")
                break
        
        elif best_of == "5" and games == 5:
            if p1wins > p2wins:
                print(f"Well done, Player one. You won and you have {p1wins} wins!")
            elif p2wins > p1wins:
                print(f"Well done, Player two. You won and you have {p2wins} wins!")
            else:
                print("You both tied, well played.")
            break


if gamemode != "duo": 
    while True:
        while True:
            player_choice = input("What would you like, rock, paper, or scissors? ").lower().strip()
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

        rematch = input("Want a rematch or no? ").lower()
        player_choice == ""
        if rematch == "no":
            break
            
    if score < 0:
        score = 0

    print(score)