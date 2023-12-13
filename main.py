from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FLASHY")
window.config(background=BACKGROUND_COLOR)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.pack()

left_image = PhotoImage(file="./images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0)
left_button.pack()

window.mainloop()
