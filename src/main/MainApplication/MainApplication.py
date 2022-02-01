import tkinter as tk
from PIL import Image, ImageTk

class MainApplication(tk.Tk):

    def __init__(self, software_version: str):
        super().__init__()

        # root window
        self.title('legeno-rune-setter')
        # self.geometry('640x480')
        self.geometry('900x600')
        self.resizable(False, False)

        _toolbar = tk.Frame(self)
        _left_runes = tk.Frame(self)
        _right_runes = tk.Frame(self)

        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=10, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')

        # Top
        _toolbar.grid(row=0, column=0, sticky='nsew', columnspan=2)
        _toolbar.rowconfigure(0, weight=1)
        _toolbar.columnconfigure(0, weight=1, uniform='a')   # Edit name button
        _toolbar.columnconfigure(1, weight=8, uniform='a')   # rune page selection
        _toolbar.columnconfigure(2, weight=1, uniform='a')   # save button
        _toolbar.columnconfigure(3, weight=1, uniform='a')   # new rune page button
        _toolbar.columnconfigure(4, weight=1, uniform='a')   # trash button

        # debugging purpose
        # TODO: switch to actual objects
        _edit_button = tk.Button(_toolbar, text="Edit")
        rune_pages = ['Aatrox_rune1', 'Aatrox_rune2', 'Aatrox_rune3']
        tkvar = tk.StringVar(self)
        tkvar.set('Aatrox_rune1')
        _rune_pages_selection = tk.OptionMenu(_toolbar, tkvar, *rune_pages)
        _save_button = tk.Button(_toolbar, text="SAVE")
        _new_rune_page_button = tk.Button(_toolbar, text="+")
        _trash_button = tk.Button(_toolbar, text="-")

        _edit_button.grid(row=0, column=0, sticky='nsew')
        _rune_pages_selection.grid(row=0, column=1, sticky='nsew')
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

        img = Image.open("../resources/precision/Precision_rune.png")
        img_tk = ImageTk.PhotoImage(img)
        _precision_button = tk.Button(_left_runes_row0, image=img_tk)
        _precision_button.photo = img_tk
        _precision_button.grid(row=0, column=0)

        img = Image.open("../resources/domination/Domination_rune.png")
        img = img.convert('L')
        img_tk = ImageTk.PhotoImage(img)
        _precision_button = tk.Button(_left_runes_row0, image=img_tk)
        _precision_button.photo = img_tk
        _precision_button.grid(row=0, column=1)

        img = Image.open("../resources/sorcery/Sorcery_rune.png")
        img = img.convert("L")
        img_tk = ImageTk.PhotoImage(img)
        _precision_button = tk.Button(_left_runes_row0, image=img_tk)
        _precision_button.photo = img_tk
        _precision_button.grid(row=0, column=2)

        img = Image.open("../resources/resolve/Resolve_rune.png")
        img = img.convert("L")
        img_tk = ImageTk.PhotoImage(img)
        _precision_button = tk.Button(_left_runes_row0, image=img_tk)
        _precision_button.photo = img_tk
        _precision_button.grid(row=0, column=3)

        img = Image.open("../resources/inspiration/Inspiration_rune.png")
        img = img.convert("L")
        img_tk = ImageTk.PhotoImage(img)
        _precision_button = tk.Button(_left_runes_row0, image=img_tk)
        _precision_button.photo = img_tk
        _precision_button.grid(row=0, column=4)

        _left_runes_row1.rowconfigure(0, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(0, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(1, weight=1, uniform='a')
        _left_runes_row1.columnconfigure(2, weight=1, uniform='a')

        img = Image.open("../resources/precision/Press_the_Attack_rune.png")
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        _press_the_attack_button = tk.Button(_left_runes_row1, image=img_tk, border=0)
        _press_the_attack_button.photo = img_tk
        # _press_the_attack_button["bg"] = "white"
        _press_the_attack_button.grid(row=0, column=0)

        img = Image.open("../resources/precision/Lethal_Tempo_rune.png")
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row1, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=1)

        img = Image.open("../resources/precision/Fleet_Footwork_rune.png")
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row1, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=2)

        img = Image.open("../resources/precision/Conqueror.png")
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row1, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=3)

        _left_runes_row2.rowconfigure(0, weight=1)
        _left_runes_row2.columnconfigure(0, weight=1)
        _left_runes_row2.columnconfigure(1, weight=1)
        _left_runes_row2.columnconfigure(2, weight=1)

        img = Image.open("../resources/precision/Overheal_rune.png")
        img = img.resize((50, 50))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row2, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=0)

        img = Image.open("../resources/precision/Triumph_rune.png")
        img = img.resize((50, 50))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row2, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=1)

        img = Image.open("../resources/precision/Presence_of_Mind_rune.png")
        img = img.resize((50, 50))
        img_tk = ImageTk.PhotoImage(img)
        _lethal_tempo_button = tk.Button(_left_runes_row2, image=img_tk, border=0)
        _lethal_tempo_button.photo = img_tk
        _lethal_tempo_button.grid(row=0, column=2)

        _left_runes_row3.rowconfigure(0, weight=1)
        _left_runes_row3.columnconfigure(0, weight=1)
        _left_runes_row3.columnconfigure(1, weight=1)
        _left_runes_row3.columnconfigure(2, weight=1)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Legend-_Alacrity_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row3, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=0)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Legend-_Tenacity_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row3, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=1)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Legend-_Bloodline_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row3, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=2)

        _left_runes_row4.rowconfigure(0, weight=1)
        _left_runes_row4.columnconfigure(0, weight=1)
        _left_runes_row4.columnconfigure(1, weight=1)
        _left_runes_row4.columnconfigure(2, weight=1)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Coup_de_Grace_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row4, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=0)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Cut_Down_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row4, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=1)

        img = ImageTk.PhotoImage(Image.open("../resources/precision/Last_Stand_rune.png"))
        _lethal_tempo_button = tk.Button(_left_runes_row4, image=img, border=0)
        _lethal_tempo_button.photo = img
        _lethal_tempo_button.grid(row=0, column=2)

        # Bottom Right
        _right_runes.grid(row=1, column=1, sticky='nsew')
        _right_runes.columnconfigure(0, weight=1)
        _right_runes.rowconfigure(0, weight=2)
        _right_runes.rowconfigure(1, weight=1)
        _right_runes.rowconfigure(2, weight=1)
        _right_runes.rowconfigure(3, weight=1)
        _right_runes.rowconfigure(4, weight=1)
        _right_runes.rowconfigure(5, weight=1)
        _right_runes.rowconfigure(6, weight=1)

        # TODO: might be better if toolbar, left_runes, and right_runes are separate objects, and widgets are attributes


if __name__ == "__main__":
    root = MainApplication("default")
    root.mainloop()
