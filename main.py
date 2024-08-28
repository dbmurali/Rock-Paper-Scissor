import random
from ascii_art import gameover
from ascii_art import rock,paper,scissors
restart=True
while restart:
    game=[rock,paper,scissors]
    user=int(input("0-rock, 1- paper, 2- scissors\n"))
    bot=random.randint(0,2)
    print(game[user])
    print(game[bot])


    if user>=3 or user<0:
            print("INVALAID INPUT")
    elif user==0 and bot==2:
            print("YOU WIN")
    elif user==2 and bot==0:
            print("YOU loss")
    elif user>bot:
            print("YOU WIN")
    elif user<bot:
            print("YOU LOSS")
    elif user==bot:
            print("DRAW")

    restart_choice=input("Select \"y\" to restart or \"n\" for end the game").lower()
    if restart_choice=="y":
            restart=True
    else:
            restart=False
            print(gameover)