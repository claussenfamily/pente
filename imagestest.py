from tkinter import *
from images import *


def main():
    root = Tk()
    root.title("Pente")
    root.geometry("900x700")


    # Just a visual to demonstrate all the images
    # This function exists only for test purposes
    images = getImages()
    row = 0
    column = 0
    for key in images:
        Label(root, image=images[key], width=35, height=27).grid(row=row, column=column, padx=10, pady=10)
        column += 1
        if (column == 12):
            row += 1
            column = 0


    # getImage(row, column) sample usage
    # Let's say you want the image at row 0, column 0
    row += 1
    Label(root, text="Image at 0,0").grid(row=row, column=0)

    row += 1
    image = getImage(0, 0)
    Label(root, image=image, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)


    # getBeadImage(row, column, playerNumber) sample usage
    # Let's say you want the bead image
    row += 1
    column = 0
    Label(root, text="Beads at 0,0").grid(row=row, column=0)

    row += 1
    blueImage = getBeadImage(0, 0, "Blue")
    Label(root, image=blueImage, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)

    row += 1
    redImage = getBeadImage(0, 0, "Red")
    Label(root, image=redImage, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)


    # getImage(row, column) sample usage
    # Usage example, let's say you want the image at row 9, column 9 (CENTER)
    row += 1
    Label(root, text="Image at 9,9").grid(row=row, column=0)

    row += 1
    image = getImage(9, 9)
    Label(root, image=image, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)


    # getBeadImage(row, column, playerNumber) sample usage
    # Usage example, let's say you want the blue bead image at row 0, column 0
    row += 1
    Label(root, text="Beads at 9,9").grid(row=row, column=0)

    row += 1
    blueImage = getBeadImage(9, 9, "Blue")
    Label(root, image=blueImage, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)

    row += 1
    redImage = getBeadImage(9, 9, "Red")
    Label(root, image=redImage, width=27, height=27).grid(row=row, column=0, padx=0, pady=0)



    root.mainloop()



main()
