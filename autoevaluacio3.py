import tkinter as tk
from tkinter import messagebox

def mostrar_etiqueta(valor):
    etiqueta.config(text=f"Has pulsado {valor}")

def ask_yes_no():
    var_fe = messagebox.askyesno("Título ask_yes_no", "Missatge")
    if var_fe:
        mostrar_etiqueta("sí")
    else:
        mostrar_etiqueta("no")

def ask_question():
    var_fe = messagebox.askquestion("Títol pregunta", "Missatge")
    if var_fe == 'yes':
        mostrar_etiqueta("sí")
    else:
        mostrar_etiqueta("no")

def ask_ok_cancel():
    var_fe = messagebox.askokcancel("Títol ok_cancel", "Missatge")
    if var_fe:
        mostrar_etiqueta("sí")
    else:
        mostrar_etiqueta("no")

def show_info():
    messagebox.showinfo("Informacion", "Esto es un panel de informacion")
    mostrar_etiqueta("sí")

def show_warning():
    messagebox.showwarning("Warning", "Cuidado")
    mostrar_etiqueta("sí")

def show_error():
    messagebox.showerror("Mostrar error", "Error")
    mostrar_etiqueta("sí")

root = tk.Tk()
root.title("Diàlegs MessageBox")

etiqueta = tk.Label(root, text="")
etiqueta.pack()

tk.Button(root, text="AskYesNo", command=ask_yes_no).pack()
tk.Button(root, text="AskQuestion", command=ask_question).pack()
tk.Button(root, text="AskOkCancel", command=ask_ok_cancel).pack()
tk.Button(root, text="ShowInfo", command=show_info).pack()
tk.Button(root, text="ShowWarning", command=show_warning).pack()
tk.Button(root, text="ShowError", command=show_error).pack()

root.mainloop()
