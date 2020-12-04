import random
import os

moves = {
    'Rock': {
        'beats':[
            'Scissors'
        ]
    },
    'Paper': {
        'beats': [
            'Rock'
        ]
    },
    'Scissors': {
        'beats': [
            'Paper'
        ]
    }
}

inputMap = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

def init_game():
    clear_display()
    start_game()


def start_game():

    computerWins  = 0
    playerWins = 0

    while computerWins != 2 and playerWins != 2:
        playerMove = make_move()
        computerMove = computer_move()

        print('Computer picks: ' + computerMove)

        if playerMove == computerMove:
            print('Draw! ' + playerMove + ' vs ' + computerMove)
        else:
            if player_beats_computer(playerMove, computerMove):
                print('Player wins ' + playerMove + ' beats ' + computerMove)
                playerWins += 1
            else:
                print('Computer wins ' + computerMove + ' beats ' + playerMove)
                computerWins += 1

        print('Player ' + str(playerWins) + ' - ' + str(computerWins) + ' Computer')

    if playerWins > computerWins:
        winner = 'Player'
    else:
        winner = 'Computer'

    print(winner + ' Wins!')

    play_again()

def play_again():
    """
        restart game if user inputs 'y'
    """
    choice = ''
    while choice.lower() not in ['y', 'n']:
        choice = input('Play again? (y/n): ')

    if (choice.lower() == 'y'):
        clear_display()
        init_game()

    return

def player_beats_computer(playerMove, computerMove):
    move = moves.get(playerMove)
    beats = move.get('beats')
    if computerMove in beats:
        return True

    return False

def computer_move():
    return inputMap.get(random.choice(list(inputMap.keys())))

def make_move():
    move = ''
    while move not in inputMap.keys():
        move = input('Ready? Choose (R)ock, (P)aper or (S)cissors:').lower()
        if (move not in inputMap.keys()):
            print('Fool! Choose a proper move!')

    return inputMap.get(move)


def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    init_game()