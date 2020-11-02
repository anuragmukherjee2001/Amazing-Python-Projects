import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Translate:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator".center(130))
        self.root.geometry("800x800+0+0")
        # self.root.resizable(0,0)

        heading = tk.Label(
                        root, 
                        text = "Welcome to our Translator", 
                        font = ("Helvita 18 bold"),
                        bg = "gray",
                        fg = "White",
                        height = 2,
                        )

        heading.place(
                        x = 0, 
                        y = 0, 
                        relwidth = 1,
                        )

        language_selection = tk.Label(
                            root, 
                            text = "Select the Language:",
                            font = ("Helvita 15 bold"),
                            ) 

        language_selection.place(
                                x = 0, 
                                y = 90,
                                )

        language_box = ttk.Combobox(
                            root, 
                            font = ("Times New Roman", 12),
                            justify = tk.CENTER,
                            state = "readonly"
                            )

        language_box['values'] = (
                                "Select",
                                "English",
                                "German",
                                "Greek", 
                                "Hindi", 
                                "French",
                                )                    

        language_box.place(x = 250, y = 90) 

        language_box.current(0) 

        label2 = tk.Label(
                        root, 
                        text = "Enter the text below:", 
                        font = ("Times New Roman bold", 16),
                        ) 

        label2.place(
                    x = 0, 
                    y = 160,
                    )

        text_widget = tk.Text(
                root,
                height = 20,
                width = 95,
                bg = "light yellow",
                bd = 3,
                ) 

        text_widget.place(
                        x = 10, 
                        y = 200,
                        )                       

root = tk.Tk()

r1 = Translate(root)

root.mainloop()

