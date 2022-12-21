import tkinter as tk
import tkinter.ttk as ttk

from PIL import Image, ImageTk
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow

window_size = [360, 140]
window_name = "About"


class AboutWindow(AdditionalWindow):
    def __init__(self, parent_window=None):
        super().__init__(window_size, window_name, parent_window)

        self.set_window_background_image("TkinterStyle/images/about_menu_background.png",
                                         [21, 26], [-3, 1])
        self.window_style = {"Togglebutton": ["Calibri", 12]}
        self.set_window_style(self.window_style)
        self.create_about_text()

    def create_about_text(self):
        self.columnconfigure(0, weight=1)

        about_text = """"Tic-tac-toe Game" was made by Mozharov Nazar, 
                    a first-year student at MFF UK.\n
             Contacts: nazar050802@gmail.com"""

        frame = tk.Frame(master=self)
        frame.grid(row=0, column=0, padx=14, pady=14)

        label = ttk.Label(master=frame, text=about_text, anchor="center", font=("Calibri", 12))
        label.pack()

        frame = tk.Frame(master=self)
        frame.grid(row=1, column=0, padx=14, pady=8)

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
