from tkinter import*
from tkinter.ttk import *
import os
import random

class start(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)

class level(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.emojifr = Frame(self)
        self.emojifr.pack(anchor=CENTER, expand=True, fill=BOTH)
        emojis_directory = "emojis"
        image_size = 150
        self.emojis_images = self.load_and_resize_images(emojis_directory, image_size)
        self.create_buttons()

    def create_buttons(self):
        random.shuffle(self.emojis_images)
        blist = []
        for i in range(3):
            row = []
            for j in range(4):
                if self.emojis_images:
                    index = (i * 4) + j
                    if index < len(self.emojis_images):
                        button = Button(self.emojifr, image=self.emojis_images[index], command=lambda i=index: self.index_selected(i))
                        button.grid(row=i, column=j)
                        row.append(button)
                    else:
                        break  # Stop creating buttons if we run out of images
            blist.append(row)

    def load_and_resize_images(self, directory, size):
        images = []
        for filename in os.listdir(directory):
            if filename.endswith(".png"):  # Adjust file extension if needed
                image_path = os.path.join(directory, filename)
                image = PhotoImage(file=image_path)
                # Resize the image to a square box
                resized_image = image.subsample(image.width() // size, image.height() // size)
                images.append(resized_image)
        return images

    def index_selected(self, index):
        print(index, "selected")



class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, **kwargs)
        box = Frame(self)
        box.pack(fill=BOTH, expand=1)
        self.level= level(box, self)
        self.start=start(box,self)
        self.title('Memory Game')
        self.fup(self.level)

    def fup(self, f, *args):
        f.tkraise()
        for a in args:
            a.forget()
        f.pack(fill=BOTH, expand=1)
game=window()
game.mainloop()
