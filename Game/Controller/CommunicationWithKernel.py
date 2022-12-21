from Kernel.Rules import find_winner, does_game_finish
from Kernel.PlayerUnit import PlayerUnit
from Kernel.Board import Board
from Kernel.MakeComputerMove import get_computer_move


def convert_gui_players_list_to_kernel_player_list(players: list = []) -> list[PlayerUnit]:
    output_players = []

    for i in range(len(players)):
        output_players.append(PlayerUnit(players[i]["player_symbol"], players[i]["player_name"]))

    return output_players


def convert_gui_board_to_kernel_board(board: [], players: list = []) -> Board:
    output_board = []
    for i in range(len(board)):
        temp_arr = []
        for k in range(len(board[i])):
            if board[i][k] != -1:
                temp_arr.append(players[board[i][k]]["player_symbol"])
            else:
                temp_arr.append("")

        output_board.append(temp_arr)

    return Board(output_board, len(board))


def check_the_board_for_the_winner(board: [], players: list = []):

    kernel_board = convert_gui_board_to_kernel_board(board, players)
    kernel_players = convert_gui_players_list_to_kernel_player_list(players)
    if not does_game_finish(kernel_board):

        winner = find_winner(kernel_players, kernel_board)

        if winner == "":
            return [0, ""]
        else:
            return [1, winner]

    else:
        winner = find_winner(kernel_players, kernel_board)

        if winner == "":
            return [2, ""]
        else:
            return [1, winner]


def make_computer_move_with_data_conversion(board: [], players: list = [], computer_index_in_players_list: int = 0,
                                            computer_difficult: int = 0):
    kernel_board = convert_gui_board_to_kernel_board(board, players)
    kernel_players = convert_gui_players_list_to_kernel_player_list(players)

    return get_computer_move(kernel_players, kernel_board, computer_index_in_players_list, computer_difficult)
