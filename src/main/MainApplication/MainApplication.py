import tkinter as tk


class MainApplication(tk.Tk):

    def __init__(self, software_version: str):
        super().__init__()

        # root window
        self.title('legeno-rune-setter')
        # self.geometry('640x480')
        self.geometry('900x600')
        self.resizable(False, False)

        # TODO: remove borderwidth and bg; for debugging purpose only
        _toolbar = tk.Frame(self, borderwidth=1, bg='cyan')
        _left_runes = tk.Frame(self, borderwidth=1, bg='red')
        _right_runes = tk.Frame(self, borderwidth=1, bg='blue')

        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=10, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1,weight=1, uniform='a')

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






        # Bottom
        _left_runes.grid(row=1, column=0, sticky='nsew')
        _right_runes.grid(row=1, column=1, sticky='nsew')

        # TODO: might be better if toolbar, left_runes, and right_runes are separate objects, and widgets are attributes


if __name__ == "__main__":
    root = MainApplication("default")
    root.mainloop()
