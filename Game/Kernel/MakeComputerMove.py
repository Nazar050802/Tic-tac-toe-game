from Kernel.ComputerDifficulties.EasyMode import make_easy_move
from Kernel.ComputerDifficulties.NormalMode import make_normal_move
from Kernel.ComputerDifficulties.HardMode import make_hard_move

from Kernel.Board import Board
from Kernel.PlayerUnit import PlayerUnit


def get_computer_move(players: list[PlayerUnit], board: Board,
                       computer_index_in_players_list: int = 0, difficult_of_computer: int = 0):

    if difficult_of_computer == 0:
        return make_easy_move(board)

    elif difficult_of_computer == 1:
        return make_normal_move(players, board, computer_index_in_players_list)

    elif difficult_of_computer == 2:
        return make_hard_move(players, board, computer_index_in_players_list)
