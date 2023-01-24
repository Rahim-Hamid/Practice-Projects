from random import randint

lis = ["Rock", "Paper", "Scissors"]

computer = lis[randint(0, 2)]


player = True
player_win = 0
computer_win = 0

while True:

    


    player = input("Rock, Paper or Scissors: ")

    if player == computer:
        print("Tie!")

    elif player == "Paper":
        if computer == "Scissors":
            print("The Computer used Scissors to slice the Paper")
            computer_win += 1
        elif computer == "Rock":
            print("The Player used Paper to defeat Rock")
            player_win += 1

    elif player == "Rock":
        if computer == "Paper":
            print("The Computer used Paper to defeat Rock")
            computer_win += 1
        elif computer == "Scissors":
            print("The Player used Rock to break the Scissors")
            player_win += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("The Computer used Rock to break the Scissors")
            computer_win += 1
        elif computer == "Paper":
            print("The Player used Scissors to slice the Paper")
            player_win += 1
    

    ans = input("Play Again(Y/N): ")
    if ans.lower() != 'y':

        print("Player Score:", player_win)
        print("Computer Score:", computer_win)
        break
