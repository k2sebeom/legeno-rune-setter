import json


class RuneLoader:
    def __init__(self):
        with open('./saved_runes.json', 'r', encoding='utf8') as rune_file:
            self.rune_data = json.loads(rune_file.read())
        
    def get_runes(self, champ_name: str):
        champ_name = champ_name.lower()
        return self.rune_data.get(champ_name, None)
    