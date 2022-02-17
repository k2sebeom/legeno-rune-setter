import json
from database import LightDB as db


class RuneLoader:
    def __init__(self):
        with open("./saved_runes.json", "r", encoding="utf8") as rune_file:
            self.runes = db(rune_file)

    def retrieve(self, champ_name: str) -> list:
        """
        Input
        >>> champ_name: champ name string

        Returns
        >>> list of all runes under champ name
        """
        return self.runes.get(champ_name)

    def create(self, champ_name: str, data: dict):
        """

        Input
        >>> champ_name : champ name string
        >>> data : rune data dictionary

        Function:
        >>> appends new data to original json file

        """
        rune = self.runes.get_full()[champ_name]
        rune.append(data)
        self.db.set(champ_name, rune)

    def clear(self):
        """
        Clears file
        """
        self.db.reset()