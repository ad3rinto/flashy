import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FLASHY")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

with open("./data/french_words.csv") as datafile:
    data = pd.read_csv(datafile)
    list_of_words = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(list_of_words)
    french_word = current_card["French"]
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

window.mainloop()
