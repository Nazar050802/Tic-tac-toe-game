import tkinter as tk
import tkinter.ttk as ttk
import os

from PIL import Image, ImageTk
from Controller.CommunicationWithConfig import get_path_current_tkinter_theme


class AdditionalWindow(tk.Toplevel):
    def __init__(self, window_size: list[int] = None, window_name: str = "", parent_window=None):
        self.parent_window = parent_window
        super().__init__(self.parent_window)

        self.window_size = window_size
        self.window_name = window_name

        self.title(self.window_name)
        create_window(self, self.window_size[0], self.window_size[1])
        place_window_middle_screen(self, self.window_size[0], self.window_size[1])

        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('TkinterStyle/images/logo.png')))

        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.bind('<Escape>', lambda e: self.quit)

    def set_window_style(self, dict_with_font_size: dict = None):
        set_window_style(self, dict_with_font_size)

    def set_window_background_image(self, path: str, proportions_resize: list[int] = [],
                                    background_place_coordinates: list[int] = []):
        set_window_background_image(self, path, proportions_resize, background_place_coordinates)


class MainWindow(tk.Tk):
    def __init__(self, window_size: list[int] = None, window_name: str = ""):
        super().__init__()

        self.window_size = window_size
        self.window_name = window_name

        self.title(self.window_name)
        create_window(self, self.window_size[0], self.window_size[1])
        place_window_middle_screen(self, self.window_size[0], self.window_size[1])

        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('TkinterStyle/images/logo.png')))

        set_tkinter_theme(self)

    def set_window_style(self, dict_with_font_size: dict = None):
        set_window_style(self, dict_with_font_size)

    def set_window_background_image(self, path: str, proportions_resize: list[int] = [],
                                    background_place_coordinates: list[int] = []):
        set_window_background_image(self, path, proportions_resize, background_place_coordinates)


def set_window_style(root, dict_with_font_style: dict = None):
    style = ttk.Style(root)

    for key in dict_with_font_style.keys():
        style.configure(key, font=(dict_with_font_style[key][0], dict_with_font_style[key][1]))


def set_window_background_image(root, path: str, proportions_resize: list[int] = [],
                                background_place_coordinates: list[int] = []):
    background_image = Image.open(path)
    background_image = background_image.resize((root.window_size[0] + proportions_resize[0],
                                                root.window_size[1] + proportions_resize[1]))
    background_image_tk = ImageTk.PhotoImage(background_image, master=root)

    background_label = tk.Label(root, image=background_image_tk)
    background_label.image = background_image_tk
    background_label.place(x=background_place_coordinates[0], y=background_place_coordinates[1])


def change_working_directory(change_dir_name):
    try:
        last_dir = ""
        for i in reversed(os.getcwd().split("\\")):
            if i not in ["", " "]:
                last_dir = i
                break

        if last_dir != change_dir_name:
            os.chdir(f"{change_dir_name}/")

    except:
        pass


def set_tkinter_theme(root):
    style = ttk.Style(root)
    root.tk.call('source', get_path_current_tkinter_theme())
    style.theme_use('azure')


def place_window_middle_screen(root, window_size_x: int, window_size_y: int, coefficient: float = 1.0):
    x = int((root.winfo_screenwidth() - window_size_x * coefficient) // 2)
    y = int((root.winfo_screenheight() - window_size_y * coefficient) // 2)
    root.wm_geometry(f"+{x}+{y}")


def create_window(root, window_size_x, window_size_y):
    root.minsize(window_size_x, window_size_y)
    root.resizable(False, False)
