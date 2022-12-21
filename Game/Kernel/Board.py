from Kernel.Kernel import Kernel


class Board:

    def __init__(self, new_board=None, size: int = None):
        self._board = None
        self._size = size

        if new_board is not None:
            self.set_board(new_board)

        elif size is not None:
            self._board = []
            for i in range(size):
                temp_arr = []
                for k in range(size):
                    temp_arr.append("")
                self._board.append(temp_arr)

    def set_board(self, new_board):
        self._board = new_board

    def get_board(self):
        return self._board

    def set_size(self, new_size):
        if Kernel.config.get_min_size_of_board() <= new_size <= Kernel.config.get_max_size_of_board():
            self._size = new_size
        else:
            raise ValueError("Incorrect size of board!")

    def get_size(self):
        return self._size

    def change_value_of_playing(self, pos_x: int, pos_y: int, new_value: str):
        self._board[pos_x][pos_y] = new_value
