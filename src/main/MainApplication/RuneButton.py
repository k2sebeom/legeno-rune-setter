import tkinter as tk
from PIL import Image, ImageTk


class RuneButton(tk.Button):

    def __init__(self, frame_name: tk.Frame, img_path: str, row=0, column=0, grayscale=False, resize=None):

        self.frame_name = frame_name
        self.img_path = img_path
        self.row = row
        self.column = column
        self.is_grayscale = grayscale
        self.resize = resize

        _img = Image.open(img_path)
        self.rgba_img = _img.convert('RGBA')
        # img = tk.PhotoImage(img_path)

        if resize:
            _img = self.rgba_img.resize(resize)
            self.rgba_img = _img
        if grayscale:
            _img = self.rgba_img.convert('L')
            self.grey_img = _img

        img_tk = ImageTk.PhotoImage(_img)

        # TODO: solve
        # img_button = super().__init__(frame_name, image=img_tk)
        img_button = tk.Button(frame_name, image=img_tk, border=0)
        img_button.photo = img_tk

        try:
            img_button.grid(row=row, column=column)
        except:
            raise ValueError("Grid values invalid")


    def invert_greyscale(self):

        if self.is_grayscale:
            img_tk = ImageTk.PhotoImage(self.rgba_img)
        else:
            img_tk = ImageTk.PhotoImage(self.rgba_img)
        img_button = tk.Button(self.frame_name, image=img_tk, border=0)
        img_button.photo = img_tk

        self.is_grayscale = not self.is_grayscale

        try:
            img_button.grid(row=self.row, column=self.column)
        except:
            raise ValueError("Grid values invalid")

