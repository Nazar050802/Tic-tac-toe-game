import random

from Kernel.Board import Board
from Kernel.PlayerUnit import PlayerUnit
from Kernel.Rules import find_winner


def find_winning_position(players: list[PlayerUnit], board: Board, computer_player_index: int = 0):
    computer_symbol = players[computer_player_index].get_player_side()
    computer_name = players[computer_player_index].get_player_name()

    possible_moves = []
    for i in range(board.get_size()):
        for k in range(board.get_size()):

            if board.get_board()[i][k] == "":
                possible_moves.append([i, k])

    for move in possible_moves:
        board.change_value_of_playing(move[0], move[1], computer_symbol)

        if find_winner(players, board) == computer_name:
            board.change_value_of_playing(move[0], move[1], "")
            return [move[0], move[1]]

        board.change_value_of_playing(move[0], move[1], "")

    return [-1, -1]


def block_opponent(players: list[PlayerUnit], board: Board, computer_player_index: int = 0):
    interfere_move = [-1, -1]

    player_symbols = []
    for i in players:
        if i.get_player_side() != players[computer_player_index].get_player_side():
            player_symbols.append(i.get_player_side())

    possible_moves = []
    for i in range(board.get_size()):
        for k in range(board.get_size()):

            if board.get_board()[i][k] == "":
                possible_moves.append([i, k])

    if len(possible_moves) > 0:

        for i in player_symbols:
            for possible_move in possible_moves:

                board.change_value_of_playing(possible_move[0], possible_move[1], i)

                if find_winner(players, board) != "":
                    board.change_value_of_playing(possible_move[0], possible_move[1], "")
                    interfere_move = possible_move
                    return [interfere_move, possible_moves]

                board.change_value_of_playing(possible_move[0], possible_move[1], "")

    return [interfere_move, possible_moves]


def make_normal_move(players: list[PlayerUnit], board: Board, computer_player_index: int = 0):

    winning_position = find_winning_position(players, board, computer_player_index)
    if winning_position != [-1, -1]:
        return winning_position

    estimated_move = block_opponent(players, board, computer_player_index)
    if estimated_move[0] == [-1, -1]:
        return random.choice(estimated_move[1])

    return estimated_move[0]

