from tkinter import *
from images import *


player = "Blue"


def main():
    root = Tk()
    root.title("Pente")
    root.geometry("760x760")

    for row in range(19):
        for column in range(19):
            label = Label(root, image=getImage(row, column), width=27, height=27, padx=0, pady=0)
            label.grid(row=row, column=column)
            label.bind("<Enter>", enter)
            label.bind("<Leave>", leave)
            label.bind("<Button-1>", play)

    root.mainloop()


def enter(e):
    print("Enter")
    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column']
    e.widget.config(image=getBeadImage(row, column, player))


def leave(e):
    print("Leave")
    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column']
    e.widget.config(image=getImage(row, column))


def play(e):
    print("Play")
    global player
    row = e.widget.grid_info()['row']
    column = e.widget.grid_info()['column'] 
    e.widget.config(image=getBeadImage(row, column, player))
    e.widget.unbind("<Enter>")
    e.widget.unbind("<Leave>")
    # e.widget.unbind("<Button-1>")
    nextPlayer()


def nextPlayer():
    global player
    if player == "Blue":
        player = "Red"
    else:
        player = "Blue"


main()