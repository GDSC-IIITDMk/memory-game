from tkinter import *
import os

window = Tk()
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

emojis_directory = "emojis"
image_size = 150  # Define the size of the square box
emojis_images = load_and_resize_images(emojis_directory, image_size)

# 2D array of buttons with emojis
blist = []
for i in range(3):
    row = []
    for j in range(4):
        if emojis_images:
            index = (i * 4) + j
            if index < len(emojis_images):
                button = Button(window, image=emojis_images[index],command=lambda:index_selected(index))
                button.grid(row=i, column=j)
                row.append(button)
            else:
                break  # Stop creating buttons if we run out of images
    blist.append(row)

window.mainloop()
