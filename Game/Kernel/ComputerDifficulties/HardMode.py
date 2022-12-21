import random

from Kernel.Board import Board
from Kernel.Rules import find_winner
from Kernel.PlayerUnit import PlayerUnit

from Kernel.ComputerDifficulties.NormalMode import block_opponent


class ComputerHardMode:
    def __init__(self, players: list[PlayerUnit], board: Board, computer_player_index: int = 0):

        self._computer_move = []
        self._players = players
        self._board = board
        self._computer_player_index = computer_player_index

    def identify_optimal_move(self):
        # Try to find winning position
        winning_position = self.find_winning_position()
        if winning_position != [-1, -1]:
            return winning_position

        # Block the opponent's wins
        estimated_interfere_move = block_opponent(self._players, self._board, self._computer_player_index)
        all_possible_moves = estimated_interfere_move[1]
        if estimated_interfere_move[0] != [-1, -1]:
            return estimated_interfere_move[0]

        estimated_interfere_move_for_big_board = self.block_win_on_big_board()
        if estimated_interfere_move_for_big_board != [-1, -1]:
            if estimated_interfere_move_for_big_board in all_possible_moves:
                return estimated_interfere_move_for_big_board

        # If computer goes first
        if self.does_board_is_clear():
            if self._board.get_size() <= 5:
                center_position = self._board.get_size() // 2

                if self._board.get_size() % 2 == 0:
                    return [random.randint(center_position - 1, center_position),
                            random.randint(center_position - 1, center_position)]
                else:
                    return [center_position, center_position]

        # If the opponent is not in the center
        central_free_positions = self.get_free_central_positions()
        if central_free_positions:
            return random.choice(central_free_positions)

        # Block and made bifurcations
        output_block_bifurcation = self.block_bifurcation()
        if output_block_bifurcation is not None:
            if output_block_bifurcation in all_possible_moves:
                return output_block_bifurcation

        # Find free position for computer
        suitable_move = self.find_free_position()
        if suitable_move != [-1, -1]:
            if suitable_move in all_possible_moves:
                return suitable_move

        return random.choice(estimated_interfere_move[1])

    def does_board_is_clear(self):
        for i in range(self._board.get_size()):
            for k in range(self._board.get_size()):
                if self._board.get_board()[i][k] != "":
                    return False
        return True

    def find_free_position(self):
        computer_symbol = self._players[self._computer_player_index].get_player_side()

        size_of_board = self._board.get_size()
        current_board = self._board.get_board()

        board_size_factor = size_of_board
        if board_size_factor > 5:
            board_size_factor = 5

        all_possible_moves = []

        # Try to find horizontal position
        for i in range(size_of_board):

            find_computer_position = False

            temp_calc = [[0, 0], [0, 0], [0, 0], [0, 0]]
            for k in range(size_of_board):

                flag_next_cell_is_computer = False
                if k + 1 != size_of_board:
                    if current_board[i][k + 1] == computer_symbol:
                        flag_next_cell_is_computer = True

                if current_board[i][k] == computer_symbol or find_computer_position or flag_next_cell_is_computer:

                    find_computer_position = True

                    if current_board[i][k] == computer_symbol:
                        temp_calc[0][1] += 1

                    if current_board[i][k] != computer_symbol and current_board[i][k] != "":
                        find_computer_position = False
                        temp_calc[0] = [0, 0]

                    elif current_board[i][k] == "" or current_board[i][k] == computer_symbol:
                        first_possible = []
                        if current_board[i][k] == "":
                            first_possible = [i, k]

                        for n in range(k + 1, size_of_board):
                            if len(first_possible) == 0:
                                if current_board[i][n] == "":
                                    first_possible = [i, n]

                            if current_board[i][n] == computer_symbol or current_board[i][n] == "":
                                temp_calc[0][0] += 1

                                if current_board[i][n] == computer_symbol:
                                    temp_calc[0][1] += 1

                            elif current_board[i][n] != computer_symbol and current_board[i][n] != "":
                                temp_calc[0] = [0, 0]

                            if temp_calc[0][0] >= board_size_factor:
                                all_possible_moves.append(
                                    {"move": first_possible, "number_of_computer_cells": temp_calc[0][1],
                                     "line": "h"})

                    if current_board[k][i] == computer_symbol:
                        temp_calc[1][1] += 1

                    if current_board[k][i] != computer_symbol and current_board[k][i] != "":
                        find_computer_position = False
                        temp_calc[1] = [0, 0]

                    elif current_board[k][i] == "" or current_board[k][i] == computer_symbol:
                        first_possible = []
                        if current_board[k][i] == "":
                            first_possible = [k, i]

                        for n in range(k + 1, size_of_board):
                            if len(first_possible) == 0:
                                if current_board[n][i] == "":
                                    first_possible = [n, i]

                            if current_board[n][i] == computer_symbol or current_board[n][i] == "":
                                temp_calc[1][0] += 1

                                if current_board[n][i] == computer_symbol == computer_symbol:
                                    temp_calc[1][1] += 1

                            elif current_board[n][i] != computer_symbol and current_board[n][i] != "":
                                temp_calc[1] = [0, 0]

                            if temp_calc[1][0] >= board_size_factor:
                                all_possible_moves.append(
                                    {"move": first_possible, "number_of_computer_cells": temp_calc[1][1],
                                     "line": "v"})

                    temp_calc[2] = [0, 0]
                    temp_calc[3] = [0, 0]
                    for j in range(0, size_of_board):
                        if i + j < size_of_board and k + j < size_of_board:

                            if current_board[i + j][k + j] == computer_symbol:
                                temp_calc[2][1] += 1

                            if current_board[i + j][k + j] != computer_symbol and current_board[i + j][k + j] != "":
                                find_computer_position = False
                                temp_calc[2] = [0, 0]

                            elif current_board[i + j][k + j] == "" or current_board[i + j][k + j] == computer_symbol:

                                first_possible = []
                                if current_board[i + j][k + j] == "":
                                    first_possible = [i + j, k + j]

                                for n in range(k + j + 1, size_of_board):
                                    if len(first_possible) == 0:
                                        if current_board[i + j][n] == "":
                                            first_possible = [i + j, n]

                                    if current_board[i + j][n] == computer_symbol or current_board[i + j][n] == "":
                                        temp_calc[2][0] += 1

                                        if current_board[i + j][n] == computer_symbol:
                                            temp_calc[2][1] += 1

                                    elif current_board[i + j][n] != computer_symbol and current_board[i + j][n] != "":
                                        temp_calc[2] = [0, 0]

                                    if temp_calc[2][0] >= board_size_factor:
                                        all_possible_moves.append(
                                            {"move": first_possible, "number_of_computer_cells": temp_calc[2][1]
                                                , "line": "d"})

                            if current_board[i + j][size_of_board - 1 - (k + j)] == computer_symbol:
                                temp_calc[3][1] += 1

                            if current_board[i + j][size_of_board - 1 - (k + j)] != computer_symbol and \
                                    current_board[i + j][size_of_board - 1 - (k + j)] != "":
                                find_computer_position = False
                                temp_calc[3] = [0, 0]

                            elif current_board[i + j][size_of_board - 1 - (k + j)] == "" or \
                                    current_board[i + j][size_of_board - 1 - (k + j)] == computer_symbol:

                                first_possible = []
                                if current_board[i + j][size_of_board - 1 - (k + j)] == "":
                                    first_possible = [i + j, size_of_board - 1 - (k + j)]

                                for n in range(size_of_board - 1 - (k + j), -1, -1):
                                    if len(first_possible) == 0:
                                        if current_board[i + j][n] == "":
                                            first_possible = [i + j, n]

                                    if current_board[i + j][n] == computer_symbol or current_board[i + j][n] == "":
                                        temp_calc[3][0] += 1

                                        if current_board[i + j][n] == computer_symbol:
                                            temp_calc[3][1] += 1

                                    elif current_board[i + j][n] != computer_symbol and current_board[i + j][n] != "":
                                        temp_calc[3] = [0, 0]

                                    if temp_calc[3][0] >= board_size_factor:
                                        all_possible_moves.append(
                                            {"move": first_possible,
                                             "number_of_computer_cells": temp_calc[3][1], "line": "r_d"})

        if len(all_possible_moves) > 0:
            all_possible_moves = sorted(all_possible_moves, key=lambda d: d['number_of_computer_cells'], reverse=True)
            return all_possible_moves[0]['move']

        return [-1, -1]

    def get_free_central_positions(self):
        computer_symbol = self._players[self._computer_player_index].get_player_side()
        central_free_positions = []
        center_position = self._board.get_size() // 2

        if self._board.get_size() % 2 == 0:
            for i in range(center_position - 1, center_position + 1, 1):
                for k in range(center_position - 1, center_position + 1, 1):
                    if self._board.get_board()[i][k] == "":
                        central_free_positions.append([i, k])
                    if self._board.get_board()[i][k] == computer_symbol:
                        return []
        else:
            if self._board.get_board()[center_position][center_position] == "":
                central_free_positions.append([center_position, center_position])

        return central_free_positions

    def block_bifurcation(self):

        computer_symbol = self._players[self._computer_player_index].get_player_side()

        all_corner = []

        for i in range(0, self._board.get_size() - 2, 1):
            priority = 0
            for k in range(0, self._board.get_size() - 2, 1):

                temp_board = []
                for j in range(i, 3 + i):
                    temp_board.append(self._board.get_board()[j][k: k + 3])

                corner = [[0, 0], [0, -1], [-1, 0], [-1, -1]]

                if temp_board[1][1] != "" and temp_board[1][1] != computer_symbol:
                    priority = 1

                for j in corner:
                    if temp_board[j[0]][j[1]] == computer_symbol:
                        break

                    if temp_board[j[0]][j[1]] == "" and priority == 1:
                        all_corner.append([j[0], j[1]])

                if len(all_corner) > 0:
                    output = random.choice(all_corner)

                    if output is not None:
                        if output[0] == -1:
                            output[0] = 2
                        if output[1] == -1:
                            output[1] = 2

                        output[0] += i
                        output[1] += k

                        return output
                else:
                    break

        return None

    def block_win_on_big_board(self):
        computer_symbol = self._players[self._computer_player_index].get_player_side()

        size_of_board = self._board.get_size()
        current_board = self._board.get_board()

        if size_of_board < 5:
            return [-1, -1]

        board_size_factor = 5

        # Try to find horizontal position
        for player_symbol in self._players:
            player_symbol = player_symbol.get_player_side()

            if player_symbol != computer_symbol:
                for i in range(size_of_board):
                    temp_calc = [0, 0, 0, 0]

                    computer_status_horizontal = False
                    computer_status_vertical = False

                    for k in range(size_of_board):

                        if current_board[i][k] == player_symbol:
                            temp_calc[0] += 1
                        elif current_board[i][k] == "":
                            if not computer_status_horizontal:
                                if temp_calc[0] == (board_size_factor - 2):
                                    return [i, k]
                            else:
                                computer_status_horizontal = False
                                temp_calc[0] = 0
                        elif current_board[i][k] == computer_symbol:
                            computer_status_horizontal = True
                        else:
                            temp_calc[0] = 0

                        if current_board[k][i] == player_symbol:
                            temp_calc[1] += 1
                        elif current_board[k][i] == "":
                            if not computer_status_vertical:
                                if temp_calc[1] == (board_size_factor - 2):
                                    return [k, i]
                            else:
                                computer_status_vertical = False
                                temp_calc[1] = 0
                        elif current_board[k][i] == computer_symbol:
                            computer_status_vertical = True
                        else:
                            temp_calc[1] = 0

                        temp_calc[2] = 0
                        temp_calc[3] = 0
                        computer_status_diagonal = False
                        computer_status_reversible_diagonal = False

                        for j in range(0, size_of_board):
                            if i + j < size_of_board and k + j < size_of_board:

                                if current_board[i + j][k + j] == player_symbol:
                                    temp_calc[2] += 1
                                elif current_board[i + j][k + j] == "":
                                    if not computer_status_diagonal:
                                        if temp_calc[2] == (board_size_factor - 2):
                                            return [i + j, k + j]
                                    else:
                                        computer_status_diagonal = False
                                        temp_calc[2] = 0
                                elif current_board[i + j][k + j] == computer_symbol:
                                    computer_status_diagonal = True
                                else:
                                    temp_calc[2] = 0

                                if current_board[i + j][size_of_board - 1 - (k + j)] == player_symbol:
                                    temp_calc[3] += 1
                                elif current_board[i + j][size_of_board - 1 - (k + j)] == "":
                                    if not computer_status_reversible_diagonal:
                                        if temp_calc[3] == (board_size_factor - 2):
                                            return [i + j, size_of_board - 1 - (k + j)]
                                    else:
                                        computer_status_reversible_diagonal = False
                                        temp_calc[3] = 0
                                elif current_board[i + j][size_of_board - 1 - (k + j)] == computer_symbol:
                                    computer_status_reversible_diagonal = True
                                else:
                                    temp_calc[3] = 0

        return [-1, -1]

    def find_winning_position(self):
        computer_symbol = self._players[self._computer_player_index].get_player_side()
        computer_name = self._players[self._computer_player_index].get_player_name()

        possible_moves = []
        for i in range(self._board.get_size()):
            for k in range(self._board.get_size()):

                if self._board.get_board()[i][k] == "":
                    possible_moves.append([i, k])

        for move in possible_moves:
            self._board.change_value_of_playing(move[0], move[1], computer_symbol)

            if find_winner(self._players, self._board) == computer_name:
                self._board.change_value_of_playing(move[0], move[1], "")
                return [move[0], move[1]]

            self._board.change_value_of_playing(move[0], move[1], "")

        return [-1, -1]


def make_hard_move(players: list[PlayerUnit], board: Board, computer_player_index: int = 0):
    return ComputerHardMode(players, board, computer_player_index).identify_optimal_move()
