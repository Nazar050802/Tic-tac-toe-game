import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import Controller.CommunicationWithConfig as CommunicationWithConfig

from PIL import Image, ImageTk
from UserInterface.GameWindow import GameWindow
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow

import random


window_size = [320, 300]
window_name = "Player Information"


class WindowPlayerInformation(AdditionalWindow):
    def __init__(self, parent_window=None, number_of_players: int = 2, board_size: int = 3,
                 computer_difficult: int = -1):

        super().__init__(window_size, window_name, parent_window)
        self.set_window_background_image("TkinterStyle/images/menu_get_player_information_background.png",
                                         [0, 0], [-2, 1])

        self.window_style = {"Togglebutton": ["Calibri", 12]}
        self.set_window_style(self.window_style)

        self._all_player_symbols = list(CommunicationWithConfig.get_from_config_player_symbols())
        if len(self._all_player_symbols) > 0:
            self._all_player_symbols.remove("X")
            self._all_player_symbols.remove("O")

        self._all_player_symbols = ["X", "O"] + random.sample(self._all_player_symbols, 8)
        self._game_settings = {"number_of_players": number_of_players, "board_size": board_size,
                               "players": [], "computer_difficult": computer_difficult, "does_game_finish": False}

        self.create_get_info_about_players()

    def set_computer_information(self, computer_name: str = ""):
        available_symbols = list(self._all_player_symbols)
        for i in self._game_settings["players"]:
            if i["player_symbol"] not in ["", " "]:
                available_symbols.remove(i["player_symbol"])

        self._game_settings["players"].append({"player_name": f"{computer_name}",
                                               "player_symbol": f"{random.choice(available_symbols)}"})

        self._game_settings["number_of_players"] += 1

    def create_start_game_button(self, entry_player_name, combobox_player_symbols):

        def start_game():
            # Set the last player data
            if self.get_and_set_user_input_data(-1, entry_player_name, combobox_player_symbols):

                self.withdraw()
                self.grab_release()

                if self._game_settings["computer_difficult"] != -1:
                    self.set_computer_information("[(#$@;_COMPUTER_;@$#)]")

                game_window = GameWindow(self, self._game_settings)
                game_window.grab_set()

        frame = tk.Frame(master=self)
        frame.grid(row=2, column=0, padx=14, pady=8)

        button_image = Image.open('TkinterStyle/images/game_start_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        button = ttk.Button(master=frame,
                            width=20,
                            text="START GAME",
                            style="Togglebutton",
                            command=start_game,
                            image=button_image_tk, compound="left")
        button.image = button_image_tk
        button.pack(pady=(8, 16))

    def create_return_button(self):
        frame = tk.Frame(master=self)
        frame.grid(row=3, column=0, padx=14, pady=8)

        button_image = Image.open('TkinterStyle/images/navigation_back_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        button = ttk.Button(master=frame,
                            text="BACK TO GAME MENU",
                            style="Togglebutton",
                            command=lambda: self.back_to_main_window(),
                            image=button_image_tk, compound="left")
        button.image = button_image_tk
        button.pack(pady=5)

    def create_get_player_names_and_symbols(self, current_player: int = 0):

        # Create LabelFrame
        labelframe_name_of_player = ttk.LabelFrame(self, text=f"INPUT NAME OF PLAYER {current_player + 1}")
        labelframe_name_of_player.grid(row=0, pady=6)

        # Create frame inside LabelFrame
        frame_number_name_of_player = tk.Frame(master=labelframe_name_of_player)
        frame_number_name_of_player.grid(row=0, pady=6, padx=18)

        entry_player_name = ttk.Entry(master=frame_number_name_of_player)
        entry_player_name.pack(padx=(7, 7), pady=6)

        # Create LabelFrame
        labelframe_symbol_of_player = ttk.LabelFrame(self, text=f"CHOOSE SYMBOL OF PLAYER {current_player + 1}")
        labelframe_symbol_of_player.grid(row=1)

        # Create frame inside LabelFrame
        frame_symbol_of_player = tk.Frame(master=labelframe_symbol_of_player)
        frame_symbol_of_player.grid(row=0, pady=6)

        combobox_values = [i for i in self._all_player_symbols]
        for i in self._game_settings["players"]:
            if i["player_symbol"] not in ["", " "]:
                combobox_values.remove(i["player_symbol"])

        combobox_player_symbols = ttk.Combobox(master=frame_symbol_of_player,
                                               values=combobox_values,
                                               state="readonly")
        combobox_player_symbols.pack(padx=(18, 0), pady=6)

        try:
            if current_player + 1 != self._game_settings["number_of_players"]:
                self.create_next_player_button(current_player, labelframe_name_of_player, labelframe_symbol_of_player,
                                               entry_player_name, combobox_player_symbols)
            else:
                self.create_start_game_button(entry_player_name, combobox_player_symbols)
        except:
            pass

    def get_and_set_user_input_data(self, current_player, entry_player_name, combobox_player_symbols) -> bool:
        player_name = entry_player_name.get()
        player_symbol = combobox_player_symbols.get()

        all_player_names = []
        for i in self._game_settings["players"]:
            all_player_names.append(i["player_name"])

        all_player_symbols = []
        for i in self._game_settings["players"]:
            all_player_symbols.append(i["player_symbol"])

        if len(player_name) > 0 and all(x.isspace() or x.isalnum() for x in player_name) and\
                player_symbol not in ["", " "] and player_name not in all_player_names and\
                player_symbol not in all_player_symbols:

            self._game_settings["players"][current_player]["player_name"] = player_name
            self._game_settings["players"][current_player]["player_symbol"] = player_symbol

            return True
        else:
            if not (len(player_name) > 0 and all(x.isspace() or x.isalnum() for x in player_name)):
                mb.showwarning("Attention", "Incorrect player name !\nYou can only use letters, numbers and spaces !")
            elif player_name in all_player_names:
                mb.showwarning("Attention", "Incorrect player name !\nPlayer name already in use !")
            if player_symbol in ["", " "]:
                mb.showwarning("Attention", "Incorrect player symbol !\nPlease choose player symbol !")
            elif player_symbol in all_player_symbols:
                mb.showwarning("Attention", "Incorrect player symbol !\nPlayer symbol already in use !")

        return False

    def create_next_player_button(self, current_player, labelframe_name_of_player, labelframe_symbol_of_player,
                                  entry_player_name, combobox_player_symbols):

        def next_player():
            if self.get_and_set_user_input_data(current_player, entry_player_name, combobox_player_symbols):
                labelframe_name_of_player.destroy()
                labelframe_symbol_of_player.destroy()
                button.destroy()

                self.create_get_player_names_and_symbols(current_player + 1)

        frame = tk.Frame(master=self)
        frame.grid(row=2, column=0, padx=14, pady=8)

        button_image = Image.open('TkinterStyle/images/next_step_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        button = ttk.Button(master=frame,
                            width=20,
                            text="NEXT PLAYER",
                            style="Togglebutton",
                            command=next_player,
                            image=button_image_tk, compound="left")
        button.image = button_image_tk
        button.pack(pady=(8, 16))

    def create_get_info_about_players(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        for _ in range(self._game_settings["number_of_players"]):
            self._game_settings["players"].append({"player_name": "", "player_symbol": ""})

        self.create_get_player_names_and_symbols()

        self.create_return_button()

    def back_to_main_window(self):
        self.grab_release()
        self.parent_window.set_window_style(self.parent_window.window_style)
        self.parent_window.deiconify()
        self.destroy()