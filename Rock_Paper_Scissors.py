from random import randint

def computer_move():
    computer_input = randint(1, 3)

    if computer_input == 1:
        chosen = "r"
    elif computer_input == 2:
        chosen = "p"
    else:
        chosen = "s"

    return chosen


print("Welcome to Rock, Paper, Scissors!")
play = True

while play:
    quit = input("Continue Game? y/n ")
    if quit == "n":
        print("Thanks for playing!")
        play = False
    elif quit == "y":
        player_input = input("Rock(r), Paper(p), Scissors(s)?")
        computer_input = computer_move()

        print(player_input, "vs", computer_input)
        if player_input == computer_input:
            print("Draw!")

        elif player_input == "r" and computer_input == "p":
            print("Computer wins!")

        elif player_input == "r" and computer_input == "s":
            print("Player wins!")

        elif player_input == "p" and computer_input == "s":
            print("Computer Wins!")

        elif player_input == "p" and computer_input == "r":
            print("Player wins!")

        elif player_input == "s" and computer_input == "r":
            print("Computer Wins!")

        elif player_input == "s" and computer_input == "p":
            print("Player wins!")
    else:
        print("Invalid Entry")
        continue