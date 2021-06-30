import random
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os

# root stuff
root = tk.Tk()
root.geometry('100x100')
root.title('CC Screenshot Randomizer')

# popup msg
def pop_up_msg(var):
    popup = tk.Tk()
    popup.wm_title("Read!")
    label = tk.Label(popup, text=var)
    label.pack(side="top", fill="x", pady=10)
    b1 = tk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()


# frames
main_frame = tk.Frame()
title_label = tk.Label(root, text="Screenshot Shuffler", bg='Blue', fg='White').pack()

path = askdirectory(title='Select Folder')
files = os.listdir(path)
file_list = []

for f in files:
    file_list.append(f)


# Functions
def screen_store():

    screen_num = random.randint(0, len(file_list))
    rand_screen = file_list[screen_num]
    return rand_screen


def screen_image():
    r = tk.Toplevel()
    r.title("RAND SCREEN")
    rand_screen = Image.open(screen_store())
    rand_screen_size = rand_screen.size
    rand_w = rand_screen_size[0]
    rand_h = rand_screen_size[1]
    canvas = tk.Canvas(r, height=rand_h, width=rand_w)
    canvas.pack()

    rand_screen_image = ImageTk.PhotoImage(rand_screen)
    canvas.create_image(0, 0, anchor='nw', image=rand_screen_image)
    r.mainloop()


# Labels, Buttons, What else
msg = "Click button after blank screens to continue shuffling. Add images to the same folder containing the exe."
pop_up_msg(msg)
screen_shot_button = tk.Button(root, text="Random Screenshot", command=screen_image, bg="Green", fg="White")

# Display with Frames
screen_shot_button.pack()

root.mainloop()


