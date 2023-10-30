import tkinter as tk

root = tk.Tk()
root.geometry('800x1000')
root.title("Imagenes")

lista = ['C:/Users/pauca/M7Basicos/Imagenes/Atleti.png', 'C:/Users/pauca/M7Basicos/Imagenes/Sevilla.png', 'C:/Users/pauca/M7Basicos/Imagenes/Valencia.png', 'C:/Users/pauca/M7Basicos/Imagenes/Madrid.png', 'C:/Users/pauca/M7Basicos/Imagenes/Barca.png']

def salir():
    root.destroy()

def siguiente():
    global imagen_actual
    if imagen_actual < len(lista) - 1:
        imagen_actual += 1
        mostrar_imagen(imagen_actual)

def anterior():
    global imagen_actual
    if imagen_actual > 0:
        imagen_actual -= 1
        mostrar_imagen(imagen_actual)

def mostrar_imagen(index):
    image = tk.PhotoImage(file=lista[index])
    imagen_label.configure(image=image)
    imagen_label.image = image  # Para evitar que la imagen sea eliminada por el recolector de basura

    numimagenes.config(text=f'Imagen {index + 1} de {len(lista)}')

    # Habilitar o deshabilitar el botón "Anterior" según la imagen actual
    if imagen_actual == 0:
        botonanterior["state"] = "disabled"
    else:
        botonanterior["state"] = "normal"

x, y = 10, 80
button_width, button_height = 80, 60

imagen_actual = 0

imagen_label = tk.Label(root)
imagen_label.place(x=10, y=10)

botonsalir = tk.Button(root, text="Salir", command=salir, font=('Arial', 10))
botonsalir.place(x=80, y=380, width=button_width, height=button_height)

botonsiguiente = tk.Button(root, text="Siguiente", command=siguiente, font=('Arial', 10))
botonsiguiente.place(x=160, y=380, width=button_width, height=button_height)

botonanterior = tk.Button(root, text="Anterior", command=anterior, font=('Arial', 10),state="disabled")
botonanterior.place(x=240, y=380, width=button_width, height=button_height)

numimagenes = tk.Label(root,text="Imagen " + str(len(lista)) + " de total", bd=10, relief="sunken", anchor="e")
numimagenes.place(x=350, y=380)
mostrar_imagen(imagen_actual)

root.mainloop()
