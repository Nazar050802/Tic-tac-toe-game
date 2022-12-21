import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

from UserInterface.GeneralClassesAndFunctions import MainWindow
from UserInterface.AboutWindow import AboutWindow
from UserInterface.SettingsWindow import SettingsWindow
from UserInterface.StartGameWindow import StartGameWindow

window_size = [260, 300]
main_menu_buttons = [["START GAME", "TkinterStyle/images/start_icon.png"],
                     ["SETTINGS", "TkinterStyle/images/gear_icon.png"],
                     ["ABOUT", "TkinterStyle/images/about_icon.png"],
                     ["EXIT", "TkinterStyle/images/close_icon.png"]]
window_name = "Tic-tac-toe"


class MainMenu(MainWindow):

    def __init__(self):
        super().__init__(window_size, window_name)

        self.set_window_background_image("TkinterStyle/images/main_menu_background.png",
                                         [0, 20], [-3, -2])
        self.window_style = {"Togglebutton": ["Calibri", 16]}
        self.set_window_style(self.window_style)

        self.place_main_menu_buttons()

    def button_click_handling(self, button_text: str):
        if button_text == main_menu_buttons[0][0]:
            self.withdraw()

            start_game = StartGameWindow(self)
            start_game.grab_set()

        elif button_text == main_menu_buttons[1][0]:
            self.withdraw()

            settings_window = SettingsWindow(self)
            settings_window.grab_set()

        elif button_text == main_menu_buttons[2][0]:
            self.withdraw()

            about_window = AboutWindow(self)
            about_window.grab_set()

        elif button_text == main_menu_buttons[3][0]:
            self.quit()

    def place_main_menu_buttons(self):
        self.columnconfigure(0, weight=1)

        for i in range(len(main_menu_buttons)):
            frame = tk.Frame(master=self)
            frame.grid(row=i, column=0, padx=5, pady=14)

            button_image = Image.open(main_menu_buttons[i][1])
            button_image = button_image.resize((16, 16))
            button_image_tk = ImageTk.PhotoImage(button_image, master=self)
            button = ttk.Button(master=frame,
                                text=main_menu_buttons[i][0],
                                style="Togglebutton",
                                command=lambda button_text=main_menu_buttons[i][0]: self.button_click_handling(button_text),
                                image=button_image_tk, compound="left")
            button.image = button_image_tk
            button.pack(padx=5, pady=5)


if __name__ == "__main__":

    app = MainMenu()
    app.mainloop()
