import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'


def player(x):
    if x == 'r':
        return rock
    elif x == 'p':
        return paper
    elif x == 's':
        return scissors


def choice():
    input_string = input('Choose [r]ock, [p]aper or [s]cissors: ')
    while input_string not in 'rps':
        print('Invalid input. Try again...')
        input_string = input()
    return input_string


def player_logic():
    player_choice = choice()
    player_move = player(player_choice)
    return player_move


def computer():
    computer_move = ''
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = rock
    elif random_number == 2:
        computer_move = paper
    elif random_number == 3:
        computer_move = scissors
    return computer_move


def game_logic(playerturn, computerturn):
    if playerturn == computerturn:
        print('Draw!')
    elif (playerturn == rock and computerturn == scissors) or \
            (playerturn == paper and computerturn == rock) or \
            (playerturn == scissors and computerturn == paper):
        print('YOU WIN!')
    else:
        print('YOU LOSE!')
    print(f"Your move: {playerturn} VS Computer's move: {computerturn}")


player_turn = player_logic()
computer_turn = computer()
game_logic(player_turn, computer_turn)
again = input(f'Wanna play again ? [y]es or [q]uit ?')
while again != 'q':
    if again == 'y':
        player_turn = player_logic()
        computer_turn = computer()
        game_logic(player_turn, computer_turn)
    else:
        print('Invalid input. Try again...')
    again = input(f'Wanna play again ? [y]es or [q]uit ?')
print('Exiting the game...Thank you for playing !')
