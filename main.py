from tkinter import *
from random import choice, shuffle

root = Tk()
root.title("State Word Shuffle Game")
root.geometry("600x400")

my_label = Label(root, text="", font=("Helvetica", 32))
my_label.pack(pady=20)

def shuffle_word():

    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas",
        "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii",
        "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan",
        "Minnesota", "Mississippi", "Missouri",
        "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico",
        "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington",
        "West Virginia", "Wisconsin", "Wyoming"
    ]

    # Choose a random state
    word = choice(states)

    # Convert the word into a list of letters
    break_apart_word = list(word)

    # Shuffle the letters
    shuffle(break_apart_word)

    # Convert the list back into a string
    shuffled_word = "".join(break_apart_word)

    # Display the shuffled word
    my_label.config(text=shuffled_word)


my_button = Button(
    root,
    text="Shuffle",
    command=shuffle_word
)
my_button.pack(pady=20)

root.mainloop()