import tkinter as tk

# Crea la ventana main
root = tk.Tk()
root.geometry('400x500')
root.title("Calculadora")
root.iconbitmap("C:/Users/pauca/M7Basicos/iconocalculadora.ico")

entry = tk.Entry(root, font=('Arial', 20))
entry.place(x=10, y=10, width=380, height=50)

def exit():
    root.destroy()

def insert_char(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression in the entry field and display the result
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create buttons for numbers 0-9, operators, and other functions
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'Sortir'
]

x, y = 10, 80
button_width, button_height = 80, 60

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate, font=('Arial', 20)).place(x=x, y=y, width=button_width, height=button_height)
    elif button == 'C':
        tk.Button(root, text=button, command=clear_entry, font=('Arial', 20)).place(x=x, y=y, width=button_width, height=button_height)
    elif button == 'Sortir':
        tk.Button(root, text=button, command=exit, font=('Arial', 10)).place(x=300, y=400, width=button_width, height=button_height)
    else:
        tk.Button(root, text=button, command=lambda b=button: insert_char(b), font=('Arial', 20)).place(x=x, y=y, width=button_width, height=button_height)
    x += button_width
    if x > 290:
        x = 10
        y += button_height

# Start the Tkinter main loop
root.mainloop()
