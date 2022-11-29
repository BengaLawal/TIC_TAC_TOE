from board import Board
from player import Player

# https://inventwithpython.com/chapter10.html

# def replace_char_in_str(string, position, character):
#     """string[:position] - gives string until position given (not including)\n
#     + character - adds character given to the end of string
#     + string[position+1:] - gives rest of string from after position given
#     """
#     return string[:position] + character + string[position+1:]

# TODO 1: Track player score
# TODO 2: Simplify check_if_three_symbols_connect func and turn
# TODO 3: Add option to go against computer

board = Board()
player_1 = Player('Player 1', 'X')
player_2 = Player('Player 2', 'O')


def placement_on_board(placement_, player):
    """Places player symbol on board"""
    if placement_:
        board.board[int(placement_) - 1] = player.symbol


def no_space_to_play(move):
    """Return true if out of space"""
    if move == 9:
        return True


def spot_is_empty(placement_):
    if board.board[int(placement_)-1] == " ":
        return True


def play_game():
    turn = 0  # turn 0 for player 1 and turn 1 for player 2
    moves = 0  #

    playing = True
    while playing:
        if turn == 0:  # player 1 turn
            placement_1 = input(f'where do you want to place your symbol {player_1.name} ({player_1.symbol})?\n')
            if spot_is_empty(placement_1):
                placement_on_board(placement_1, player_1)  # place symbol where specified
                if board.check_if_three_symbols_connect(placement_1):  # if 3 symbols connect
                    print(f'{player_1.name} ({player_1.symbol}) wins')
                    player_1.score += 1  # add 1 to player score
                    print(f'Player 1 score: {player_1.score}\n'  # print final score
                          f'Player 2 score: {player_2.score}')
                    playing = False
                else:  # if there are no 3 connecting
                    moves += 1
                    if no_space_to_play(moves):  # tie if there is no space to play
                        print('It is a tie')
                        playing = False
                    turn += 1
            else:
                print("Play at a different spot")

        elif turn == 1:  # player 2 turn
            placement_2 = input(f'where do you want to place your symbol {player_2.name} ({player_2.symbol})?\n')
            if spot_is_empty(placement_2):
                placement_on_board(placement_2, player_2)  # place symbol where specified
                if board.check_if_three_symbols_connect(placement_2):
                    print(f'{player_2.name} ({player_2.symbol}) wins')
                    player_2.score += 1
                    print(f'Player 1 score: {player_1.score}\n'
                          f'Player 2 score: {player_2.score}')
                    playing = False
                else:
                    moves += 1
                    if no_space_to_play(moves):
                        print('It is a tie')
                        playing = False
                    turn -= 1
            else:
                print("Play at a different spot")

        board.print_board()


still_playing = True
while still_playing:
    board.print_board()
    response = input('Do you want to play TIC TAC TOE? y/n').lower()
    if response == 'y':
        board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        play_game()
    elif response == 'n':
        print("Good bye")
        still_playing = False
