import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb

from PIL import Image, ImageTk
from UserInterface.GeneralClassesAndFunctions import AdditionalWindow

from UserInterface.GeneralClassesAndFunctions import change_working_directory
from Controller.CommunicationWithConfig import set_current_tkinter_theme, get_tkinter_theme_in_int


window_size = [360, 140]
window_name = "Settings"


class SettingsWindow(AdditionalWindow):
    def __init__(self, parent_window=None):
        super().__init__(window_size, window_name, parent_window)

        self.set_window_background_image("TkinterStyle/images/about_menu_background.png",
                                         [18, 20], [-3, 1])
        self.window_style = {"Togglebutton": ["Calibri", 12],
                             "Switch": ["Calibri", 13]}
        self.set_window_style(self.window_style)

        self.place_settings()

    def place_settings(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_change_tkinter_theme()
        self.create_back_menu_button()

    def create_change_tkinter_theme(self):
        flag_enable_disable = tk.IntVar()
        flag_enable_disable.set(get_tkinter_theme_in_int())

        def theme_changed():
            change_working_directory("../Config")
            set_current_tkinter_theme(flag_enable_disable.get())
            change_working_directory("../UserInterface")

            mb.showinfo("Attention", "To apply the settings, please restart the game !")

        frame = tk.Frame(master=self)
        frame.grid(row=0, column=0, pady=(2, 8))

        check_button = ttk.Checkbutton(master=frame,
                                       style="Switch",
                                       text='Enable dark theme',
                                       command=theme_changed,
                                       variable=flag_enable_disable,
                                       onvalue=1,
                                       offvalue=0)
        check_button.pack(padx=5, pady=5)

    def create_back_menu_button(self):
        frame = tk.Frame(master=self)
        frame.grid(row=1, column=0, pady=8)

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
