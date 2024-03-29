from tkinter import *
# from tkinter.ttk import * //the parameters like padx pady aren't recognised while using this
import os,random


SCREENWIDTH = 1000
SCREENHEIGHT = 800

root = Tk()
root.geometry(F'{SCREENWIDTH}x{SCREENHEIGHT}')
root.title("Memory Game")


window = Frame(root)


def index_selected(index):
    print(index,"selected")
    # Do something with the index


# Function to load and resize images from the emojis directory
def load_and_resize_images(directory, size):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Adjust file extension if needed
            image_path = os.path.join(directory, filename)
            image = PhotoImage(file=image_path)
            # Resize the image to a square box
            resized_image = image.subsample(image.width() // size, image.height() // size)
            images.append(resized_image)
    return images


emojis_directory = "emojis" #using absolute path
image_size = 150 # Define the size of the square box
emojis_images = load_and_resize_images(emojis_directory, image_size)


random.shuffle(emojis_images) #shuffles the images in emojis directory
# 2D array of buttons with emojis
blist = []
for i in range(3):
    row = []
    for j in range(4):
        if emojis_images:
            index = (i * 4) + j
            if index < len(emojis_images):
                button = Button(window, width=200,height=200,padx=10,pady=10,image=emojis_images[index],command=lambda i=index:index_selected(i))
                button.grid(row=i, column=j)
                row.append(button)
            else:
                break  # Stop creating buttons if we run out of images
    blist.append(row)

title = Label(root,text="Memory Game",font=("Consolas",30),pady=25)
title.pack()

window.pack(expand=True)


window.mainloop()
