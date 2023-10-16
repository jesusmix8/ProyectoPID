import tkinter as tk
from tkinter import PhotoImage


class TuClase:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Botón con Imagen")

        # Cargar la imagen
        self.imagen = PhotoImage(file="img/lena.png")

        # Crear un botón con la imagen
        self.boton_con_imagen = tk.Button(
            self.ventana, image=self.imagen, command=self.accion_boton
        )
        self.boton_con_imagen.pack(pady=10)

    def accion_boton(self):
        print("¡Botón con imagen presionado!")

    def iniciar(self):
        self.ventana.mainloop()


# Crear una instancia de TuClase y comenzar la aplicación
mi_app = TuClase()
mi_app.iniciar()
