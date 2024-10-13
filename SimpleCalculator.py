import tkinter as tk

# create the main window
root = tk.Tk()

# declare the entry width ...
entry = tk.Entry(root, width=20, font=("Arial",20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=10)


