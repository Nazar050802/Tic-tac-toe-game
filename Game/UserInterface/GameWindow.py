import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import Controller.CommunicationWithKernel as CommunicationWithKernel

from PIL import Image, ImageTk
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow


window_size = [40, 140]
window_name = "Game"
button_color = ["#2B3A55", "#BE3144", "#4B125C", "#EC7700", "#28CC9E", "#007CB9", "#9973E2", "#4E3620", "#446E5C"]


class GameWindow(AdditionalWindow):

    def __init__(self, parent_window, game_settings: dict):
        self._game_settings = game_settings

        window_size_with_buttons = [window_size[0], window_size[1]]
        self.window_style = {"Togglebutton": ["Calibri bold", 26],
                             "BackButton.Togglebutton": ["Calibri", 11]}

        if self._game_settings["board_size"] > 7:
            self.window_style["Togglebutton"][1] -= int(1.4 * self._game_settings["board_size"] - 7)

            if self._game_settings["board_size"] > 13:
                window_size_with_buttons[0] += (70 - (self._game_settings["board_size"] - 7) * 4) * self._game_settings[
                    "board_size"]
            else:
                window_size_with_buttons[0] += (70 - (self._game_settings["board_size"] - 7) * 3) * self._game_settings["board_size"]
            window_size_with_buttons[1] += (60 - (self._game_settings["board_size"] - 7) * 3) * self._game_settings["board_size"]

        else:
            window_size_with_buttons[0] += 70 * self._game_settings["board_size"]
            window_size_with_buttons[1] += 60 * self._game_settings["board_size"]

        super().__init__([window_size_with_buttons[0],
                          window_size_with_buttons[1]],
                         window_name, parent_window)

        # set_tkinter_theme(self)

        self.set_window_style(self.window_style)
        self.set_button_color()

        self._board_array = []

        self._buttons = []
        self._buttons_size = [2, 2]
        if self._game_settings["board_size"] > 13:
            self._buttons_size = [1, 0]

        self._back_button = None

        self._current_turn = []
        self._current_player = 0

        self.place_buttons()

    def set_button_color(self):
        copied_button_colors = list(button_color)

        for i in range(len(self._game_settings["players"])):
            if len(copied_button_colors) > 0:
                self._game_settings["players"][i]["player_color"] = random.choice(copied_button_colors)
                copied_button_colors.remove(self._game_settings["players"][i]["player_color"])
            else:
                self._game_settings["players"][i]["player_color"] = "#000000"

        style = ttk.Style(self)

        for i in range(len(self._game_settings["players"])):
            style.configure(f"Player{i}.Togglebutton",
                            foreground=f'{self._game_settings["players"][i]["player_color"]}')

    def place_buttons(self):
        self._board_array = []
        for i in range(self._game_settings["board_size"]):
            temp_array = []
            for k in range(self._game_settings["board_size"]):
                temp_array.append(-1)
            self._board_array.append(temp_array)

        self.withdraw()

        self._current_player = random.randint(0, self._game_settings["number_of_players"] - 1)
        player_who_makes_first_move = self._game_settings["players"][self._current_player]["player_name"]

        if player_who_makes_first_move == "[(#$@;_COMPUTER_;@$#)]":
            player_who_makes_first_move = "COMPUTER"

        mb.showinfo("Attention", f'This player makes the first move: '
                                 f'{player_who_makes_first_move}\n')
        self.deiconify()
        self.place_game_buttons()
        self.create_return_button()

    def button_click_handling(self, row, column):

        def disable_all_buttons():
            for i in range(len(self._buttons)):
                for k in range(len(self._buttons[i])):
                    self._buttons[i][k].state(["disabled"])

        if self._board_array[row][column] == -1:

            self._board_array[row][column] = self._current_player

            # Change text on button board
            self._buttons[row][column].configure(
                text=str(self._game_settings["players"][self._board_array[row][column]]["player_symbol"]).upper(),
                style=f"Player{self._board_array[row][column]}.Togglebutton")

            find_winner = CommunicationWithKernel.check_the_board_for_the_winner(self._board_array,
                                                                                 self._game_settings["players"])

            if find_winner[0] == 1:
                self._game_settings["does_game_finish"] = True
                disable_all_buttons()

                if find_winner[1] == "[(#$@;_COMPUTER_;@$#)]":
                    find_winner[1] = "COMPUTER"

                self._back_button.state(["disabled"])

                # Change text Label current turn to winner text
                ttk.Style(self).configure(style='My.TLabel',
                                          foreground=f"{self._game_settings['players'][self._current_player]['player_color']}")
                self._current_turn[1].configure(text=f"Winner: {find_winner[1]}")

                if not mb.askyesno("Game Finished", f'The winner is the player with the name: {find_winner[1]}\n'
                                                    f'His gaming symbol: '
                                                    f'{self._game_settings["players"][self._current_player]["player_symbol"]}\n\n'
                                                    f'Do you want to look at the playing board one last time?'):
                    self.back_to_main_window()
                else:
                    self._back_button.state(["!disabled"])
                    disable_all_buttons()

            elif find_winner[0] == 2:
                self._game_settings["does_game_finish"] = True
                disable_all_buttons()

                self._back_button.state(["disabled"])

                # Change text Label current turn to draw text
                ttk.Style(self).configure(style='My.TLabel', foreground=f"#000000")
                self._current_turn[1].configure(text=f"Draw !")

                if not mb.askyesno("Game Finished", f'Draw!\n'
                                                    f'Do you want to look at the playing board one last time?'):
                    self.back_to_main_window()
                else:
                    self._back_button.state(["!disabled"])
                    disable_all_buttons()
            else:
                self._current_player += 1
                if self._current_player >= self._game_settings["number_of_players"]:
                    self._current_player = 0

                if self._game_settings["players"][self._current_player]["player_name"] == "[(#$@;_COMPUTER_;@$#)]":
                    self.computer_move()
                else:
                    # Change text Label current turn
                    ttk.Style(self).configure(style='My.TLabel',
                                              foreground=f"{self._game_settings['players'][self._current_player]['player_color']}")
                    self._current_turn[1].configure(
                        text=f"{self._game_settings['players'][self._current_player]['player_name']}"
                             f"'s turn")

    def computer_move(self):
        computer_move = CommunicationWithKernel.make_computer_move_with_data_conversion(
            self._board_array, self._game_settings["players"],
            self._current_player,
            self._game_settings["computer_difficult"])

        self.button_click_handling(computer_move[0], computer_move[1])

    def place_game_buttons(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Create label with text "Current turn"
        style_current_turn = ttk.Style(self)
        style_current_turn.configure(style='My.TFrame', background="#E5E5E5")
        style_current_turn.configure(style='My.TLabel', background="#E5E5E5",
                                     foreground=f"{self._game_settings['players'][self._current_player]['player_color']}")

        self._current_turn.append(ttk.Frame(master=self, style="My.TFrame"))

        self._current_turn.append(ttk.Label(master=self._current_turn[0], style='My.TLabel',
                                            text=f"{self._game_settings['players'][self._current_player]['player_name']}"
                                                 f"'s turn"))
        self._current_turn[1].config(font=("Calibri bold", 14))

        self._current_turn[1].pack(anchor="center", pady=2)
        self._current_turn[0].grid(row=0, sticky="nswe", pady=(0, 12))

        # Create playing buttons
        frame_with_board = tk.Frame(master=self)
        frame_with_board.grid(row=1, sticky="n")

        for c in range(self._game_settings["board_size"]):
            frame_with_board.columnconfigure(index=c, weight=1)
        for r in range(self._game_settings["board_size"]):
            frame_with_board.rowconfigure(index=r, weight=1)

        for r in range(self._game_settings["board_size"]):
            temp_button_array = []

            for c in range(self._game_settings["board_size"]):
                btn = ttk.Button(frame_with_board,
                                 text="",
                                 width=self._buttons_size[0],
                                 style="Togglebutton",
                                 command=lambda i=r, k=c: self.button_click_handling(i, k))

                btn.grid(row=r, column=c, ipady=self._buttons_size[1], padx=3, pady=3)

                temp_button_array.append(btn)

            self._buttons.append(temp_button_array)

        # If the computer makes the first move, make its move
        if self._game_settings["players"][self._current_player]["player_name"] == "[(#$@;_COMPUTER_;@$#)]":
            self.computer_move()

    def back_to_main_window(self):
        def end_with_this_window():
            self.grab_release()

            self.parent_window.set_window_style(self.parent_window.window_style)
            self.parent_window.back_to_main_window()

            self.destroy()

        # Show attention
        if not self._game_settings["does_game_finish"]:
            if mb.askyesno("Attention",
                           "Are you sure you want to leave the game?\nYou will lose your current progress."):
                end_with_this_window()
        else:
            end_with_this_window()

    def create_return_button(self):
        frame = tk.Frame(master=self)
        frame.grid(row=2, column=0, padx=14, pady=(30, 4))

        button_image = Image.open('TkinterStyle/images/navigation_back_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        self._back_button = ttk.Button(master=frame,
                            text="BACK TO GAME MENU",
                            style="BackButton.Togglebutton",
                            command=lambda: self.back_to_main_window(),
                            image=button_image_tk, compound="left")
        self._back_button.image = button_image_tk
        self._back_button.pack(pady=5)