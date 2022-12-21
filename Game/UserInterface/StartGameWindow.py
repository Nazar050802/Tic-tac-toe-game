import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

from UserInterface.GameWindowSettingsPlayerVsPlayer import GameWindowSettingsPlayerVsPlayer
from UserInterface.GameWindowSettingsPlayerVsComputer import GameWindowSettingsPlayerVsComputer
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow

window_size = [320, 220]
window_name = "Game mode"
game_modes_buttons = [["PLAYER VS PLAYER", "TkinterStyle/images/player_vs_player_icon.png"],
                      ["PLAYER VS COMPUTER", "TkinterStyle/images/player_vs_computer_icon.png"]]


class StartGameWindow(AdditionalWindow):
    def __init__(self, parent_window=None):
        super().__init__(window_size, window_name, parent_window)
        self.set_window_background_image("TkinterStyle/images/start_game_window_background.png",
                                         [0, 0], [-2, 1])

        self.window_style = {"Togglebutton": ["Calibri", 12]}
        self.set_window_style(self.window_style)

        self.create_game_modes()

    def create_game_modes(self):
        self.columnconfigure(0, weight=1)

        labelframe = ttk.LabelFrame(self, text="CHOOSE GAME MODE")
        labelframe.grid(row=0, pady=(6, 0))

        for i in range(len(game_modes_buttons)):
            frame = tk.Frame(master=labelframe)
            frame.grid(row=i+1, column=0, padx=5, pady=10)

            button_image = Image.open(game_modes_buttons[i][1])
            button_image = button_image.resize((16, 16))
            button_image_tk = ImageTk.PhotoImage(button_image, master=self)
            button = ttk.Button(master=frame,
                                text=game_modes_buttons[i][0],
                                width=24,
                                style="Togglebutton",
                                command=lambda button_text=game_modes_buttons[i][0]: self.button_click_handling(button_text),
                                image=button_image_tk, compound="left")
            button.image = button_image_tk
            button.pack(padx=5, pady=5)

        frame = tk.Frame(master=self)
        frame.grid(row=len(game_modes_buttons)+2, column=0, padx=14, pady=(18, 0))

        button_image = Image.open('TkinterStyle/images/navigation_back_icon.png')
        button_image = button_image.resize((14, 14))
        button_image_tk = ImageTk.PhotoImage(button_image, master=self)
        button = ttk.Button(master=frame,
                            text="BACK TO MAIN MENU",
                            style="Togglebutton",
                            command=lambda: self.back_to_main_window(),
                            image=button_image_tk, compound="left")
        button.image = button_image_tk
        button.pack(padx=5, pady=5)

    def back_to_main_window(self):
        self.grab_release()
        self.parent_window.set_window_style(self.parent_window.window_style)
        self.parent_window.deiconify()
        self.destroy()

    def button_click_handling(self, button_text):
        if button_text == game_modes_buttons[0][0]:
            self.withdraw()
            self.grab_release()

            game_window = GameWindowSettingsPlayerVsPlayer(self)
            game_window.grab_set()

        elif button_text == game_modes_buttons[1][0]:
            self.withdraw()
            self.grab_release()

            game_window = GameWindowSettingsPlayerVsComputer(self)
            game_window.grab_set()

