import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


# the radiobutton
class RuneButtonRadioButton(tk.Radiobutton):
    def __init__(self, master, variable, **kwargs):
        tk.Radiobutton.__init__(self, master, **{**kwargs, 'variable': variable, 'indicatoron': 0})

        # delete this line ~ only for text version purposes
        self.configure(width=5)

        self.__bound = False
        self.__bind_names = ['<Enter>', '<Leave>', '<1>']
        self.__bind_states = ['hover', 'up', 'down']
        self.__bind_ids = [None] * 3

        self.__var = variable
        self.__var.trace('w', self.__adjust)
        self.__adjust()

    # bind all events ~ change "text" to "image" at the end of the lambda
    def __bindings(self):
        for i, (name, state) in enumerate(zip(self.__bind_names, self.__bind_states)):
            self.__bind_ids[i] = self.bind(name, lambda e, s=state: self.configure(text=s))
        self.__bound = True

    # unbind all events
    def __unbindings(self):
        if self.__bound:
            for name, id in zip(self.__bind_names, self.__bind_ids):
                self.unbind(name, id)
            self.__bound = False

    def __adjust(self, *args):
        if self.__var.get() == self['value']:
            # change "text" to "image"
            self['text'] = 'sel'
            if self.__bound:
                self.__unbindings()
        else:
            if not self.__bound:
                # change "text" to "image"
                self['text'] = 'up'
                self.__bindings()


selection = tk.StringVar()
selection.set('3')

# DO NOT CHANGE the "name" argument
# images = dict(
#    up=ImageTk.PhotoImage(Image.open('up.png'), name='up'),
#    hover=ImageTk.PhotoImage(Image.open('hover.png'), name='hover'),
#    down=ImageTk.PhotoImage(Image.open('down.png'), name='down'),
#    sel=ImageTk.PhotoImage(Image.open('selected.png'), name='sel'),
# )

# the loop
for n in range(4):
    RuneButtonRadioButton(root, variable=selection, value=f'{n}').grid(row=0, column=n)

root.mainloop()
