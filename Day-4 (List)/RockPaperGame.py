import random
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '✊'
paper = '🤚'
scissors = '👉'
Win = '😃'
Loose = '🥲'
draw = '😑'
game_images = [rock, paper, scissors]
choice1 = int(input("What do you want to choose? Type 0 for 'rock', 1 for 'paper' and 2 for 'scissors'.\n"))

if choice1 >= 3 or choice1 < 0:
    print(f"You typed invalid number, you loose! {Loose}")
else:
    print(game_images[choice1])

    computerChoice = random.randint(0,2)
    print("Computer choose:")
    print(game_images[computerChoice])

    if choice1 >= 3 or choice1 < 0:
        print("You typed invalid number, you loose!")
    elif choice1 == 0 and computerChoice == 2:
        print(f"You win! {Win}")
    elif computerChoice == 0 and choice1 == 2:
        print(f"You Loose! {Loose}")
    elif computerChoice > choice1:
        print(f"You loose! {Loose}")
    elif choice1 > computerChoice:
        print(f"You win!{Win}")
    elif computerChoice == choice1:
        print(f"It's a draw! {draw}")
