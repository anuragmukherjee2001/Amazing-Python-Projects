import tkinter as tk
import tkinter.ttk

root = tkinter.Tk()
root.title("Digital Clock".center(140))
root.resizable(0, 0)

root.iconbitmap('clock.ico')

from time import strftime

def time():
    s = strftime('%H:%M:%S %p')
    label.config(text = s)
    label.after(1000, time)

label = tkinter.Label(
                root,
                font = ("Helvitica", 80),
                background = "black",
                foreground = "cyan"
                )

label.pack(anchor = tkinter.CENTER)

time()

root.mainloop()