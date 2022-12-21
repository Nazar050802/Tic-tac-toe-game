from Kernel.Kernel import Kernel


class PlayerUnit:
    def __init__(self, new_side: str = None, new_name: str = None):
        self._player_side = None
        self._player_name = None

        if new_side is not None:
            self.set_player_side(new_side)

        if new_name is not None:
            self.set_player_name(new_name)

    def set_player_side(self, new_player_side: str) -> None:
        if new_player_side in Kernel.config.get_player_symbols():
            self._player_side = new_player_side
        else:
            raise ValueError("Incorrect player symbol!")

    def get_player_side(self) -> str:
        return self._player_side

    def set_player_name(self, new_player_name: str) -> None:
        if new_player_name != "":
            self._player_name = new_player_name
        else:
            raise ValueError("Incorrect player name!")

    def get_player_name(self) -> str:
        return self._player_name
