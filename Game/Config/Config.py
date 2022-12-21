import json
import os


class Config:
    def __init__(self):
        self._file_name = None
        self._working_directory = None

        self._data = {}

        self.initialize_file_json()

    def create_json(self, json_data: dict):

        with open(self._file_name, 'w+') as file:
            json.dump(json_data, file)

    def read_json(self):
        with open(self._file_name, 'r+') as file:
            output_data = json.load(file)
        return output_data

    def change_working_directory(self):
        # Get current directory
        temp_working_directory = os.getcwd()
        last_dir = ""
        for i in reversed(temp_working_directory.split("\\")):
            if i not in ["", " "]:
                last_dir = i
                break

        # Change or create working directory
        if last_dir != f"{self._working_directory}":
            try:
                does_directory_exist = False

                for i in os.listdir(os.getcwd()):

                    if os.path.isdir(f"{temp_working_directory}\\{i}") and i == self._working_directory:
                        does_directory_exist = True
                        os.chdir(f"{self._working_directory}/")
                        break

                if not does_directory_exist:
                    os.mkdir(f"{self._working_directory}/")
                    os.chdir(f"{self._working_directory}/")

            except:
                return False

        return True

    def initialize_file_json(self):
        # Initialize file name and working directory
        self._file_name = "config.json"
        self._working_directory = "Config"

        # This is basic data which will use for settings
        basic_data = {
            "debug_mode": True,
            "amount_of_computer_difficulties": 3,
            "computer_difficulties": ["easy", "normal", "hard"],
            "min_amount_of_players": 2,
            "max_amount_of_players": 4,
            "player_symbols": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
                               'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z', 'X', "O"],
            "min_size_of_board": 3,
            "max_size_of_board": 15,
            "tkinter_themes": {"light": "TkinterStyle/style/azure_light/azure.tcl",
                               "dark": "TkinterStyle/style/azure_dark/azure.tcl"},
            "current_tkinter_theme": "light"
        }

        current_directory = os.getcwd()

        # If we can change working directory we will create or open JSON file
        if self.change_working_directory():

            # Create JSON file with configs if not exists
            if not os.path.exists(self._file_name):
                self.create_json(basic_data)

            # Read JSON file and create new if empty
            self._data = self.read_json()
            if len(self._data) == 0:
                self.create_json(basic_data)

            try:
                os.chdir(current_directory)
            except:
                pass

    def write_new_data(self):
        current_directory = os.getcwd()

        if self.change_working_directory():
            self.create_json(self._data)

        try:
            os.chdir(current_directory)
        except:
            pass

    # Make getters and setters
    def get_debug_mode(self):
        return self._data["debug_mode"]

    def set_debug_mode(self, new_debug_mode: bool):
        self._data["debug_mode"] = new_debug_mode
        self.write_new_data()

    def get_amount_of_computer_difficulties(self):
        return self._data["amount_of_computer_difficulties"]

    def set_amount_of_computer_difficulties(self, new_amount_of_computer_difficulties: int):
        self._data["amount_of_computer_difficulties"] = new_amount_of_computer_difficulties
        self.write_new_data()

    def get_computer_difficulties(self):
        return self._data["computer_difficulties"]

    def set_computer_difficulties(self, new_computer_difficulties: list[str]):
        if new_computer_difficulties == self.get_amount_of_computer_difficulties():
            self._data["computer_difficulties"] = new_computer_difficulties
            self.write_new_data()

    def get_max_amount_of_players(self):
        return self._data["max_amount_of_players"]

    def set_max_amount_of_players(self, new_max_amount_of_players: int):
        self._data["max_amount_of_players"] = new_max_amount_of_players
        self.write_new_data()

    def get_min_amount_of_players(self):
        return self._data["min_amount_of_players"]

    def set_min_amount_of_players(self, new_min_amount_of_players: int):
        self._data["min_amount_of_players"] = new_min_amount_of_players
        self.write_new_data()

    def get_player_symbols(self):
        return self._data["player_symbols"]

    def set_player_symbols(self, new_player_symbols: list):
        self._data["player_symbols"] = new_player_symbols
        self.write_new_data()

    def get_min_size_of_board(self):
        return self._data["min_size_of_board"]

    def set_min_size_of_board(self, new_min_size_of_board: int):
        self._data["min_size_of_board"] = new_min_size_of_board
        self.write_new_data()

    def get_max_size_of_board(self):
        return self._data["max_size_of_board"]

    def set_max_size_of_board(self, new_max_size_of_board: int):
        self._data["max_size_of_board"] = new_max_size_of_board
        self.write_new_data()

    def get_tkinter_themes(self):
        return self._data["tkinter_themes"]

    def set_tkinter_themes(self, new_tkinter_themes: dict):
        self._data["tkinter_themes"] = new_tkinter_themes
        self.write_new_data()

    def get_current_tkinter_theme(self):
        return self._data["current_tkinter_theme"]

    def set_current_tkinter_theme(self, new_current_tkinter_theme: str):
        self._data["current_tkinter_theme"] = new_current_tkinter_theme
        self.write_new_data()

