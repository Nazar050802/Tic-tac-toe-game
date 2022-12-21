import random

from Kernel.Board import Board


def make_easy_move(board: Board) -> list[int]:
    possible_moves = []
    for i in range(board.get_size()):
        for k in range(board.get_size()):

            if board.get_board()[i][k] == "":
                possible_moves.append([i, k])

    return random.choice(possible_moves)
