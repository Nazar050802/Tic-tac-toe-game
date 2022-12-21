from Kernel.Kernel import Kernel


def get_from_config_amount_of_computer_difficulties():
    return Kernel.config.get_amount_of_computer_difficulties()


def get_from_config_computer_difficulties():
    return Kernel.config.get_computer_difficulties()


def get_from_config_amounts_of_players():
    return {"min_amount": Kernel.config.get_min_amount_of_players(),
            "max_amount": Kernel.config.get_max_amount_of_players()}


def get_from_config_size_of_board():
    return {"min_size": Kernel.config.get_min_size_of_board(),
            "max_size": Kernel.config.get_max_size_of_board()}


def get_from_config_player_symbols():
    return Kernel.config.get_player_symbols()


def get_current_tkinter_theme():
    return Kernel.config.get_current_tkinter_theme()


def get_path_current_tkinter_theme():
    return Kernel.config.get_tkinter_themes()[Kernel.config.get_current_tkinter_theme()]


def set_current_tkinter_theme(status: int):
    if status == 0:
        Kernel.config.set_current_tkinter_theme(list(Kernel.config.get_tkinter_themes().keys())[0])
    elif status == 1:
        Kernel.config.set_current_tkinter_theme(list(Kernel.config.get_tkinter_themes().keys())[1])


def get_tkinter_theme_in_int() -> int:
    if Kernel.config.get_current_tkinter_theme() == list(Kernel.config.get_tkinter_themes().keys())[0]:
        return 0
    elif Kernel.config.get_current_tkinter_theme() == list(Kernel.config.get_tkinter_themes().keys())[1]:
        return 1
