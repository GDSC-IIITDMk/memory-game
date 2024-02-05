from tkinter import*
from tkinter.ttk import *
import os
import cv2
import random,time

class start(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.introfr=Frame(self)
        self.introfr.pack(anchor=CENTER, expand=True, fill=BOTH)
        self.vidcanvas=Canvas(self.introfr)
        self.vidcanvas.pack()
        self.startbut =Button(self.vidcanvas,text="(start_img)",command=lambda :self.start_game(parent,controller))
        button1_window = self.vidcanvas.create_window(600,400,anchor="se", window=self.startbut)

    def videoplay(self):
        self.cap = cv2.VideoCapture("intro_video.mp4")
        self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
            img = cv2.resize(frame, (600, 400))
            img = PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
            self.vidcanvas.create_image(0, 0, anchor=NW, image=img)
            self.vidcanvas.img = img  # Save reference to avoid garbage collection
            self.after(10, self.show_frame)  # Update every 10 milliseconds
        else:
            self.cap.release()

    def start_game(self,parent,controller):
        controller.fup(controller.level,controller.intro)

class level(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.cont=controller
        self.emojifr = Frame(self)
        self.emojifr.pack(anchor=CENTER, expand=True, fill=BOTH)
        self.emojis_directory = "emojis"
        self.image_size = 150
        self.emojis_images = self.load_and_resize_images(self.emojis_directory, self.image_size)
        self.create_buttons()
        self.selected_imgs=[]

    def create_buttons(self):
        random.shuffle(self.emojis_images)
        blist = []
        for i in range(3):
            row = []
            for j in range(4):
                if self.emojis_images:
                    index = (i * 4) + j
                    if index < len(self.emojis_images):
                        button = Button(self.emojifr, image=self.emojis_images[index][0], command=lambda i=self.emojis_images[index][1]: self.index_selected(i))
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
                images.append([resized_image,str(filename)])
        return images

    def index_selected(self, index):
        print(index, "selected")
        if index not in self.selected_imgs :
            if (len(self.selected_imgs)==11):
                print("you won")
                self.cont.fup(self.cont.end, self.cont.level)
                self.cont.end.start(1, 0 ,self.selected_imgs)
            else:
                self.selected_imgs.append(index)
                self.emojis_images = self.load_and_resize_images(self.emojis_directory, self.image_size)
                self.create_buttons()
                self.update()
        else:
            print("OUT")
            self.cont.fup(self.cont.end, self.cont.level)
            self.cont.end.start(0,index,self.selected_imgs)

class End(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.cont = controller
        self.res = StringVar()
        self.lostfr=Frame(self).pack(anchor="s")
        self.selected_grid=Frame(self).pack(anchor="s")
    def start(self,result,wrong,selected_list=list(),**kwargs):
        if result:
            self.res.set("Great")
        else:
            self.res.set("Well Try")

        lostlab = Label(self.lostfr, text=self.res.get(), font=("Verdana", 34))
        lostlab.pack(anchor="n")
        self.emojis_images=self.cont.level.emojis_images
        blist = []
        for i in range(3):
            row = []
            for j in range(4):
                if self.emojis_images:
                    index = (i * 4) + j
                    if index < len(self.emojis_images):
                        selectedlab = Label(self.selected_grid, image=self.emojis_images[index][0])
                        selectedlab.pack()
                        row.append(selectedlab)
                    else:
                        break  # Stop creating buttons if we run out of images
            blist.append(row)
        self.update()
class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, **kwargs)
        box = Frame(self)
        box.pack(fill=BOTH, expand=1)
        self.intro=start(box,self)
        self.level= level(box, self)
        self.end=End(box,self)
        self.start=start(box,self)
        self.title('Memory Game')
        self.fup(self.intro)

    def fup(self, f, *args):
        f.tkraise()
        for a in args:
            a.forget()
        f.pack(fill=BOTH, expand=1)
        if f is self.intro:
            self.intro.videoplay()
            self.intro.vidcanvas.config(height=400, width=600)
            self.update()
game=window()
game.resizable(False, False)
game.mainloop()
