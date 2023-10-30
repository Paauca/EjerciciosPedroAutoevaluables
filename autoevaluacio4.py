import tkinter as tk

def mostrar_valor():
    etiqueta_valor.config(text=f"Valor del primer boton: {boton1.get()}, Valor del segundo boton: {boton2.get()}")

root = tk.Tk()
root.geometry('400x400')
root.title("Botones deslizantes")

boton1 = tk.Scale(root, from_=0, to=100, orient='vertical')
boton1.grid(row=0, column=1, rowspan=2, sticky='nse')

boton2 = tk.Scale(root, from_=0, to=100, orient='horizontal')
boton2.grid(row=2, column=0, columnspan=2, sticky='ew')

boton_actual = tk.Button(root, text="Mostrar Valor", command=mostrar_valor)
boton_actual.grid(row=0, column=0)

etiqueta_valor = tk.Label(root, text="")
etiqueta_valor.grid(row=0, column=1)

root.mainloop()
