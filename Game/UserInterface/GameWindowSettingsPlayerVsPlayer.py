import tkinter as tk
import tkinter.ttk as ttk
import Controller.CommunicationWithConfig as CommunicationWithConfig

from PIL import Image, ImageTk
from UserInterface.GetInformationAboutPlayersWindow import WindowPlayerInformation
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow

window_size = [320, 300]
window_name = "Game Settings"


class GameWindowSettingsPlayerVsPlayer(AdditionalWindow):
    def __init__(self, parent_window=None):
        super().__init__(window_size, window_name, parent_window)

        self.set_window_background_image("TkinterStyle/images/menu_player_vs_player_background.png",
                                         [0, 0], [-2, 1])

        self.window_style = {"Togglebutton": ["Calibri", 12]}
        self.set_window_style(self.window_style)

        self._number_of_players = None
        self._board_size = None
        self.create_game_settings()

    def create_setting_number_of_players(self, current_number_of_players):
        def update_current_number_of_players(event):
            label_with_current_number_of_players.configure(text=get_current_number_of_players())

        def get_current_number_of_players():
            return current_number_of_players.get()

        number_of_players = CommunicationWithConfig.get_from_config_amounts_of_players()
        current_number_of_players.set(number_of_players["min_amount"])

        # Create LabelFrame
        labelframe_number_of_players = ttk.LabelFrame(self, text="SELECT NUMBER OF PLAYERS")
        labelframe_number_of_players.grid(row=0)

        # Create frame inside LabelFrame
        frame_number_of_players = tk.Frame(master=labelframe_number_of_players)
        frame_number_of_players.grid(row=0, pady=6)

        # Create Scale with number of players
        scale_with_number_of_players = ttk.Scale(master=frame_number_of_players,
                                                 from_=number_of_players["min_amount"],
                                                 to=number_of_players["max_amount"],
                                                 orient="horizontal",
                                                 variable=current_number_of_players,
                                                 command=update_current_number_of_players)
        scale_with_number_of_players.pack(padx=38)

        # Create label with current number of players
        label_with_current_number_of_players = ttk.Label(master=frame_number_of_players,
                                                         text=get_current_number_of_players())

        label_with_current_number_of_players.pack()

    def create_setting_board_size(self, current_board_size):
        def update_current_number_of_players(event):
            label_with_current_board_size.configure(text=get_current_number_of_players())

        def get_current_number_of_players():
            return current_board_size.get()

        number_of_players = CommunicationWithConfig.get_from_config_size_of_board()
        current_board_size.set(number_of_players["min_size"])

        # Create LabelFrame
        labelframe_board_size = ttk.LabelFrame(self, text="SELECT BOARD SIZE")
        labelframe_board_size.grid(row=1, pady=10)

        # Create frame inside LabelFrame
        frame_number_board_size = tk.Frame(master=labelframe_board_size)
        frame_number_board_size.grid(row=0, pady=6)

        # Create Scale with board size
        scale_with_board_size = ttk.Scale(master=frame_number_board_size,
                                          from_=number_of_players["min_size"],
                                          to=number_of_players["max_size"],
                                          orient="horizontal",
                                          variable=current_board_size,
                                          command=update_current_number_of_players)
        scale_with_board_size.pack(padx=38)

        # Create label with current board size
        label_with_current_board_size = ttk.Label(master=frame_number_board_size,
                                                  text=get_current_number_of_players())

        label_with_current_board_size.pack()

    def create_next_step_button(self):
        frame = tk.Frame(master=self)
        frame.grid(row=2, column=0, padx=14)

        button_image = Image.open('TkinterStyle/images/next_step_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        button = ttk.Button(master=frame,
                            width=20,
                            text="NEXT STEP",
                            style="Togglebutton",
                            command=lambda: self.next_step_window(),
                            image=button_image_tk, compound="left")
        button.image = button_image_tk
        button.pack(padx=5, pady=(5, 20))

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
        button.pack(padx=5, pady=5)

    def create_game_settings(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._number_of_players = tk.IntVar()
        self.create_setting_number_of_players(self._number_of_players)

        self._board_size = tk.IntVar()
        self.create_setting_board_size(self._board_size)

        self.create_next_step_button()
        self.create_return_button()

    def next_step_window(self):
        self.withdraw()
        self.grab_release()

        game_window = WindowPlayerInformation(self, self._number_of_players.get(), self._board_size.get())
        game_window.grab_set()

    def back_to_main_window(self):
        self.grab_release()
        self.parent_window.set_window_style(self.parent_window.window_style)
        self.parent_window.deiconify()
        self.destroy()
