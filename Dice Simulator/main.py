import tkinter
import random

root = tkinter.Tk()

root.geometry("700x600")
root.title("Dice Simulator".center(160))

label = tkinter.Label(root, font = ("times",200))



def roll():
    num = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text = f'{random.choice(num)}{random.choice(num)}')
    label.pack()


button = tkinter.Button(root, text = "Roll the dice", command = roll)
button.place(x = 330, y = 0)

root.mainloop()
