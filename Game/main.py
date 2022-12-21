from UserInterface.MainMenu import MainMenu
from UserInterface.GeneralClassesAndFunctions import change_working_directory
from Kernel.Kernel import Kernel


def main():
    kernel = Kernel()

    change_working_directory("UserInterface")

    app = MainMenu()
    app.mainloop()


if __name__ == "__main__":
    main()
