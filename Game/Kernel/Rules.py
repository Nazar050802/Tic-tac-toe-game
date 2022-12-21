from Kernel.PlayerUnit import PlayerUnit
from Kernel.Board import Board


def find_winner(players: list[PlayerUnit], board: Board) -> str:

    number_of_points_to_win = board.get_size()
    if number_of_points_to_win > 5:
        number_of_points_to_win = 5

    current_board = board.get_board()
    size_of_board = board.get_size()

    for player in players:
        player_side = player.get_player_side()

        for i in range(0, size_of_board):
            temp_calc_sides = [0, 0, 0, 0]

            for k in range(0, size_of_board):
                # Find winner in horizontal and vertical sides
                if current_board[i][k] == player_side:
                    temp_calc_sides[0] += 1
                else:
                    temp_calc_sides[0] = 0

                if current_board[k][i] == player_side:
                    temp_calc_sides[1] += 1
                else:
                    temp_calc_sides[1] = 0

                if temp_calc_sides[1] == number_of_points_to_win or \
                        temp_calc_sides[0] == number_of_points_to_win:
                    return player.get_player_name()

                # Find winner in diagonal and reversible_diagonal sides
                diagonal_winner = True
                reversible_diagonal_winner = True
                temp_calc_sides[2] = 0
                temp_calc_sides[3] = 0

                for j in range(0, size_of_board):
                    if i + j < size_of_board and k + j < size_of_board:

                        if current_board[i+j][k+j] == player_side:
                            temp_calc_sides[2] += 1
                        elif 0 < temp_calc_sides[2] < number_of_points_to_win:
                            diagonal_winner = False

                        if current_board[i+j][size_of_board - 1 - (k+j)] == player_side:
                            temp_calc_sides[3] += 1
                        elif 0 < temp_calc_sides[3] < number_of_points_to_win:
                            reversible_diagonal_winner = False

                        if not diagonal_winner and not reversible_diagonal_winner:
                            break

                        if temp_calc_sides[2] == number_of_points_to_win or\
                                temp_calc_sides[3] == number_of_points_to_win:
                            break

                if temp_calc_sides[2] < number_of_points_to_win:
                    diagonal_winner = False

                if temp_calc_sides[3] < number_of_points_to_win:
                    reversible_diagonal_winner = False

                if diagonal_winner or reversible_diagonal_winner:
                    return player.get_player_name()

    return ""


def does_game_finish(board: Board) -> bool:
    current_board = board.get_board()
    size_of_board = board.get_size()

    for i in range(0, size_of_board):
        for k in range(0, size_of_board):
            if current_board[i][k] == "":
                return False

    return True
