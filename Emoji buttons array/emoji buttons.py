from tkinter import *
from tkinter import *

window = Tk()

# Loading Images from emojis folder
photo = PhotoImage(file = r"emojis/1.png")


# 2D array of buttons with emojis

blist = [
    [Button(window,image=photo),Button(window,image=photo),Button(window,image=photo),Button(window,image=photo)],
    [Button(window,image=photo),Button(window,image=photo),Button(window,image=photo),Button(window,image=photo)],
    [Button(window,image=photo),Button(window,image=photo),Button(window,image=photo),Button(window,image=photo)],
         ]

for i in range(3):
    for j in range(4):
        blist[i][j].grid(row=i,column=j)
mainloop()