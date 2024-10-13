import tkinter as tk

# create the main window
root = tk.Tk()

# declare the entry width ...
entry = tk.Entry(root, width=20, font=("Arial",20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=10)
root.title("Simple Calculator")

# function update the expression when a button is pressed
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

def evaluate():
    try:
        result = str(eval(entry.get())) # use eval to calculate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error {e}")

# function to clear entry
def clear():
    entry.delete(0, tk.END)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# lay out the button
row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, width=10, height=3, font=("Arial",14), command=clear)
    elif button == '=':
        btn = tk.Button(root, text=button, width=10, height=3, font=("Arial",14), command=evaluate)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, font=("Arial", 14), command=lambda b=button:press(b))

    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# stat the GUI loop
root.mainloop()
