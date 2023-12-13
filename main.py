from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FLASHY")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=2)


# right_image = PhotoImage(file="./images/right.png")
# right_button = Button(image=right_image, highlightthickness=0)
# right_button.grid(row=2, column=0)
#
# left_image = PhotoImage(file="./images/wrong.png")
# left_button = Button(image=left_image, highlightthickness=0)
# left_button.grid(row=2, column=1)

window.mainloop()
