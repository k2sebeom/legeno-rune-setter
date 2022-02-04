import tkinter as tk
from PIL import Image, ImageTk
from RuneButton import RuneButton

class MainApplication(tk.Tk):

    def __init__(self, software_version: str):
        super().__init__()

        # root window
        self.title('legeno-rune-setter')
        # self.geometry('640x480')
        self.geometry('900x600')
        self.resizable(False, False)

        _toolbar = tk.Frame(self, padx=10, pady=10)
        _left_runes = tk.Frame(self, padx=30, pady=30)
        _right_runes = tk.Frame(self, padx=30, pady=30)

        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=10, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')

        # Top
        _toolbar.grid(row=0, column=0, sticky='nsew', columnspan=2)
        _toolbar.rowconfigure(0, weight=1)
        _toolbar.columnconfigure(0, weight=1, uniform='a')   # Edit name button
        _toolbar.columnconfigure(1, weight=4, uniform='a')   # rune page selection
        _toolbar.columnconfigure(2, weight=1, uniform='a')   # save button
        _toolbar.columnconfigure(3, weight=1, uniform='a')   # new rune page button
        _toolbar.columnconfigure(4, weight=1, uniform='a')   # trash button
        _toolbar.columnconfigure(5, weight=6, uniform='a')   # empty

        # debugging purpose
        # TODO: switch to actual objects
        _edit_button = tk.Button(_toolbar, text="Edit")
        rune_pages = ['Aatrox_rune1', 'Aatrox_rune2', 'Aatrox_rune3']   # TODO: check max length according to LOL API
        tkvar = tk.StringVar(self)
        tkvar.set('Aatrox_rune1')
        _rune_pages_selection = tk.OptionMenu(_toolbar, tkvar, *rune_pages)
        _save_button = tk.Button(_toolbar, text="SAVE")
        _new_rune_page_button = tk.Button(_toolbar, text="+")
        _trash_button = tk.Button(_toolbar, text="DELETE")

        _edit_button.grid(row=0, column=0, sticky='nsew')
        _rune_pages_selection.grid(row=0, column=1, sticky='nsw')
        _save_button.grid(row=0, column=2, sticky='nsew')
        _new_rune_page_button.grid(row=0, column=3, sticky='nsew')
        _trash_button.grid(row=0, column=4, sticky='nsew')

        # Bottom Left
        _left_runes.grid(row=1, column=0, sticky='nsew')
        _left_runes.columnconfigure(0, weight=1, uniform='a')
        _left_runes.rowconfigure(0, weight=1, uniform='a')
        _left_runes.rowconfigure(1, weight=1, uniform='a')
        _left_runes.rowconfigure(2, weight=1, uniform='a')
        _left_runes.rowconfigure(3, weight=1, uniform='a')
        _left_runes.rowconfigure(4, weight=1, uniform='a')

        _left_runes_row0 = tk.Frame(_left_runes)
        _left_runes_row1 = tk.Frame(_left_runes)
        _left_runes_row2 = tk.Frame(_left_runes)
        _left_runes_row3 = tk.Frame(_left_runes)
        _left_runes_row4 = tk.Frame(_left_runes)

        _left_runes_row0.grid(row=0, column=0, sticky='nsew')
        _left_runes_row1.grid(row=1, column=0, sticky='nsew')
        _left_runes_row2.grid(row=2, column=0, sticky='nsew')
        _left_runes_row3.grid(row=3, column=0, sticky='nsew')
        _left_runes_row4.grid(row=4, column=0, sticky='nsew')

        _left_runes_row0.rowconfigure(0, weight=1)
        _left_runes_row0.columnconfigure(0, weight=1)
        _left_runes_row0.columnconfigure(1, weight=1)
        _left_runes_row0.columnconfigure(2, weight=1)
        _left_runes_row0.columnconfigure(3, weight=1)
        _left_runes_row0.columnconfigure(4, weight=1)

        RuneButton(_left_runes_row0, "../resources/precision/Precision_rune.png", row=0, column=0)
        RuneButton(_left_runes_row0, "../resources/domination/Domination_rune.png", grayscale=True, row=0, column=1)
        RuneButton(_left_runes_row0, "../resources/sorcery/Sorcery_rune.png", grayscale=True, row=0, column=2)
        RuneButton(_left_runes_row0, "../resources/resolve/Resolve_rune.png", grayscale=True, row=0, column=3)
        RuneButton(_left_runes_row0, "../resources/inspiration/Inspiration_rune.png", grayscale=True, row=0, column=4)

        _left_runes_row1.rowconfigure(0, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(0, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(1, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(2, weight=1, uniform='a')

        RuneButton(_left_runes_row1, "../resources/precision/Press_the_Attack_rune.png", row=0, column=0, resize=(90, 90))
        RuneButton(_left_runes_row1, "../resources/precision/Lethal_Tempo_rune.png", row=0, column=1, grayscale=True, resize=(80, 80))
        RuneButton(_left_runes_row1, "../resources/precision/Fleet_Footwork_rune.png", row=0, column=2, grayscale=True, resize=(80, 80))
        RuneButton(_left_runes_row1, "../resources/precision/Conqueror.png", row=0, column=3, grayscale=True, resize=(80, 80))

        _left_runes_row2.rowconfigure(0, weight=1)
        _left_runes_row2.columnconfigure(0, weight=1)
        _left_runes_row2.columnconfigure(1, weight=1)
        _left_runes_row2.columnconfigure(2, weight=1)

        RuneButton(_left_runes_row2, "../resources/precision/Overheal_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_left_runes_row2, "../resources/precision/Triumph_rune.png", row=0, column=1, grayscale=True, resize=(50, 50))
        RuneButton(_left_runes_row2, "../resources/precision/Presence_of_Mind_rune.png", row=0, column=2, grayscale=True, resize=(50, 50))

        _left_runes_row3.rowconfigure(0, weight=1)
        _left_runes_row3.columnconfigure(0, weight=1)
        _left_runes_row3.columnconfigure(1, weight=1)
        _left_runes_row3.columnconfigure(2, weight=1)

        RuneButton(_left_runes_row3, "../resources/precision/Legend-_Alacrity_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_left_runes_row3, "../resources/precision/Legend-_Tenacity_rune.png", row=0, column=1, grayscale=True, resize=(50, 50))
        RuneButton(_left_runes_row3, "../resources/precision/Legend-_Bloodline_rune.png", row=0, column=2, grayscale=True, resize=(50, 50))

        _left_runes_row4.rowconfigure(0, weight=1)
        _left_runes_row4.columnconfigure(0, weight=1)
        _left_runes_row4.columnconfigure(1, weight=1)
        _left_runes_row4.columnconfigure(2, weight=1)

        RuneButton(_left_runes_row4, "../resources/precision/Coup_de_Grace_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_left_runes_row4, "../resources/precision/Cut_Down_rune.png", row=0, column=1, grayscale=True, resize=(50, 50))
        RuneButton(_left_runes_row4, "../resources/precision/Last_Stand_rune.png", row=0, column=2, grayscale=True, resize=(50, 50))

        # Bottom Right
        _right_runes.grid(row=1, column=1, sticky='nsew')
        _right_runes.columnconfigure(0, weight=1)
        _right_runes.rowconfigure(0, weight=2)
        _right_runes.rowconfigure(1, weight=2)
        _right_runes.rowconfigure(2, weight=2)
        _right_runes.rowconfigure(3, weight=2)
        _right_runes.rowconfigure(4, weight=1)
        _right_runes.rowconfigure(5, weight=1)
        _right_runes.rowconfigure(6, weight=1)

        _right_runes_row0 = tk.Frame(_right_runes)
        _right_runes_row1 = tk.Frame(_right_runes)
        _right_runes_row2 = tk.Frame(_right_runes)
        _right_runes_row3 = tk.Frame(_right_runes)
        _right_runes_row4 = tk.Frame(_right_runes)
        _right_runes_row5 = tk.Frame(_right_runes)
        _right_runes_row6 = tk.Frame(_right_runes)

        _right_runes_row0.grid(row=0, column=0, sticky='nsew')
        _right_runes_row1.grid(row=1, column=0, sticky='nsew')
        _right_runes_row2.grid(row=2, column=0, sticky='nsew')
        _right_runes_row3.grid(row=3, column=0, sticky='nsew')
        _right_runes_row4.grid(row=4, column=0, sticky='nsew')
        _right_runes_row5.grid(row=5, column=0, sticky='nsew')
        _right_runes_row6.grid(row=6, column=0, sticky='nsew')
        RuneButton(_right_runes_row4, "../resources/shards/5008.png", row=0, column=1, resize=(35, 35))

        _right_runes_row0.rowconfigure(0, weight=1)
        _right_runes_row0.columnconfigure(0, weight=1)
        _right_runes_row0.columnconfigure(1, weight=1)
        _right_runes_row0.columnconfigure(2, weight=1)
        _right_runes_row0.columnconfigure(3, weight=1)

        RuneButton(_right_runes_row0, "../resources/domination/Domination_rune.png", row=0, column=0)
        RuneButton(_right_runes_row0, "../resources/sorcery/Sorcery_rune.png", grayscale=True, row=0, column=1)
        RuneButton(_right_runes_row0, "../resources/resolve/Resolve_rune.png", grayscale=True, row=0, column=2)
        RuneButton(_right_runes_row0, "../resources/inspiration/Inspiration_rune.png", grayscale=True, row=0, column=3)

        _right_runes_row1.rowconfigure(0, weight=1)
        _right_runes_row1.columnconfigure(0, weight=1)
        _right_runes_row1.columnconfigure(1, weight=1)
        _right_runes_row1.columnconfigure(2, weight=1)
        RuneButton(_right_runes_row1, "../resources/domination/Cheap_Shot_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_right_runes_row1, "../resources/domination/Taste_of_Blood_rune.png", grayscale=True, row=0, column=1, resize=(50, 50))
        RuneButton(_right_runes_row1, "../resources/domination/Sudden_Impact_rune.png", grayscale=True, row=0, column=2, resize=(50, 50))

        _right_runes_row2.rowconfigure(0, weight=1)
        _right_runes_row2.columnconfigure(0, weight=1)
        _right_runes_row2.columnconfigure(1, weight=1)
        _right_runes_row2.columnconfigure(2, weight=1)
        RuneButton(_right_runes_row2, "../resources/domination/Zombie_Ward_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_right_runes_row2, "../resources/domination/Ghost_Poro_rune.png", grayscale=True, row=0, column=1, resize=(50, 50))
        RuneButton(_right_runes_row2, "../resources/domination/Eyeball_Collection_rune.png", grayscale=True, row=0, column=2, resize=(50, 50))

        _right_runes_row3.rowconfigure(0, weight=1)
        _right_runes_row3.columnconfigure(0, weight=1)
        _right_runes_row3.columnconfigure(1, weight=1)
        _right_runes_row3.columnconfigure(2, weight=1)
        _right_runes_row3.columnconfigure(3, weight=1)
        RuneButton(_right_runes_row3, "../resources/domination/Cheap_Shot_rune.png", row=0, column=0, resize=(50, 50))
        RuneButton(_right_runes_row3, "../resources/domination/Taste_of_Blood_rune.png", grayscale=True, row=0, column=1, resize=(50, 50))
        RuneButton(_right_runes_row3, "../resources/domination/Sudden_Impact_rune.png", grayscale=True, row=0, column=2, resize=(50, 50))
        RuneButton(_right_runes_row3, "../resources/domination/Sudden_Impact_rune.png", grayscale=True, row=0, column=3, resize=(50, 50))

        _right_runes_row4.rowconfigure(0, weight=1)
        _right_runes_row4.columnconfigure(0, weight=1)
        _right_runes_row4.columnconfigure(1, weight=1)
        _right_runes_row4.columnconfigure(2, weight=1)
        _right_runes_row4.columnconfigure(3, weight=1)

        RuneButton(_right_runes_row4, "../resources/shards/5008.png", row=0, column=1, resize=(30, 30))
        RuneButton(_right_runes_row4, "../resources/shards/5005.png", row=0, column=2, grayscale=True, resize=(30, 30))
        RuneButton(_right_runes_row4, "../resources/shards/5007.png", row=0, column=3, grayscale=True, resize=(30, 30))

        _right_runes_row5.rowconfigure(0, weight=1)
        _right_runes_row5.columnconfigure(0, weight=1)
        _right_runes_row5.columnconfigure(1, weight=1)
        _right_runes_row5.columnconfigure(2, weight=1)
        _right_runes_row5.columnconfigure(3, weight=1)

        RuneButton(_right_runes_row5, "../resources/shards/5008.png", row=0, column=1, resize=(30, 30))
        RuneButton(_right_runes_row5, "../resources/shards/5002.png", row=0, column=2, grayscale=True, resize=(30, 30))
        RuneButton(_right_runes_row5, "../resources/shards/5003.png", row=0, column=3, grayscale=True, resize=(30, 30))

        _right_runes_row6.rowconfigure(0, weight=1)
        _right_runes_row6.columnconfigure(0, weight=1)
        _right_runes_row6.columnconfigure(1, weight=1)
        _right_runes_row6.columnconfigure(2, weight=1)
        _right_runes_row6.columnconfigure(3, weight=1)

        RuneButton(_right_runes_row6, "../resources/shards/5001.png", row=0, column=1, grayscale=True, resize=(30, 30))
        RuneButton(_right_runes_row6, "../resources/shards/5002.png", row=0, column=2, resize=(30, 30))
        RuneButton(_right_runes_row6, "../resources/shards/5003.png", row=0, column=3, grayscale=True, resize=(30, 30))


if __name__ == "__main__":
    root = MainApplication("default")
    root.mainloop()
