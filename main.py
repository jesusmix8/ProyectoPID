import os
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk, ImageFilter
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter.simpledialog
from tkinter import colorchooser
from tkinter import simpledialog
import time
from tkinter import PhotoImage
from skimage import filters

# TODO


#       Falta collage Pablo Jesus
class CollageAppOne:
    def __init__(self):
        self.ventana_collage_2x2 = tk.Toplevel()
        self.ventana_collage_2x2.geometry("1250x850")
        self.ventana_collage_2x2.resizable(False, False)



        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_2x2)
        self.alto_entry = tk.Entry(self.ventana_collage_2x2)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_2x2)
        self.alto_entry = tk.Entry(self.ventana_collage_2x2)

        tk.Button(
            self.ventana_collage_2x2,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_2x2, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_2x2, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_2x2,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_2x2,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(4):
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (300, 300), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 4:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (600, 600))

        for i in range(2):
            for j in range(2):
                index = i * 2 + j
                collage.paste(self.imagenes[index], (j * 300, i * 300))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_2x2, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        for i in range(2):
            for j in range(2):
                index = i * 2 + j
                # Escalar y pegar las imágenes en el collage personalizado
                imagen_escalada = self.imagenes[index].resize(
                    (ancho // 2, alto // 2), Image.Resampling.LANCZOS
                )
                collage_personalizado.paste(
                    imagen_escalada, (j * (ancho // 2), i * (alto // 2))
                )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Crea una nueva lista de imágenes en el orden especificado por el usuario
        self.imagenes = [self.imagenes[i] for i in orden]

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_2x2.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


class CollageAppTwo:
    def __init__(self):
        self.ventana_collage_3x2 = tk.Toplevel()
        self.ventana_collage_3x2.geometry("1250x950")
        self.ventana_collage_3x2.resizable(False, False)

        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_3x2)
        self.alto_entry = tk.Entry(self.ventana_collage_3x2)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_3x2)
        self.alto_entry = tk.Entry(self.ventana_collage_3x2)

        tk.Button(
            self.ventana_collage_3x2,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_3x2, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_3x2, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_3x2,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_3x2,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(6):  # Ahora se cargan 6 imágenes para el collage 3x2
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (250, 250), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 6:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (750, 750))  # Cambia las dimensiones del collage

        for i in range(3):  # 3 renglones
            for j in range(2):  # 2 columnas
                index = i * 2 + j
                width, height = 250, 250  # Dimensiones iniciales de la imagen

                if j == 1:  # Columna 2
                    # Alarga la imagen hacia la derecha
                    width *= 2

                imagen_resized = self.imagenes[index].resize(
                    (width, height), Image.Resampling.LANCZOS
                )
                collage.paste(imagen_resized, (j * 250, i * 250))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_3x2, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        for i in range(3):  # 3 renglones
            for j in range(2):  # 2 columnas
                index = i * 2 + j
                # Escalar y pegar las imágenes en el collage personalizado
                imagen_escalada = self.imagenes[index].resize(
                    (ancho // 2, alto // 3), Image.Resampling.LANCZOS
                )
                collage_personalizado.paste(
                    imagen_escalada, (j * (ancho // 2), i * (alto // 3))
                )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Crea una nueva lista de imágenes en el orden especificado por el usuario
        self.imagenes = [self.imagenes[i] for i in orden]

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3 4 5): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_3x2.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


class CollageAppThree:
    def __init__(self):
        self.ventana_collage_2x2 = tk.Toplevel()
        self.ventana_collage_2x2.geometry("1250x850")
        self.ventana_collage_2x2.resizable(False, False)

        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_2x2)
        self.alto_entry = tk.Entry(self.ventana_collage_2x2)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_2x2)
        self.alto_entry = tk.Entry(self.ventana_collage_2x2)

        tk.Button(
            self.ventana_collage_2x2,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_2x2, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_2x2, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_2x2,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_2x2,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(5):
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (250, 250), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 5:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (500, 500))  # Cambia las dimensiones del collage

        # Imagen en la primera columna, primera fila
        collage.paste(self.imagenes[0], (0, 0))

        # Imagen en la primera columna, segunda fila
        collage.paste(self.imagenes[1], (0, 250))

        # Imágenes en la segunda columna, primera fila
        collage.paste(self.imagenes[2].resize((250, 125), Image.Resampling.LANCZOS), (250, 0))
        collage.paste(self.imagenes[3].resize((250, 125), Image.Resampling.LANCZOS), (250, 125))

        # Imagen en la segunda columna, segunda fila (ocupa toda la columna y fila)
        collage.paste(self.imagenes[4].resize((500, 250), Image.Resampling.LANCZOS), (250, 250))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_2x2, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        # Escalar y pegar las imágenes en el collage personalizado
        collage_personalizado.paste(
            self.imagenes[0].resize((ancho // 2, alto // 2), Image.Resampling.LANCZOS), (0, 0)
        )
        collage_personalizado.paste(
            self.imagenes[1].resize((ancho // 2, alto // 2), Image.Resampling.LANCZOS),
            (0, alto // 2),
        )
        collage_personalizado.paste(
            self.imagenes[2].resize((ancho // 2, alto // 4), Image.Resampling.LANCZOS),
            (ancho // 2, 0),
        )
        collage_personalizado.paste(
            self.imagenes[3].resize((ancho // 2, alto // 4), Image.Resampling.LANCZOS),
            (ancho // 2, alto // 4),
        )
        collage_personalizado.paste(
            self.imagenes[4].resize((ancho, alto // 2), Image.Resampling.LANCZOS), (0, alto // 2)
        )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Verificar que los índices en el orden estén dentro del rango
        if all(0 <= i < len(self.imagenes) for i in orden):
            # Crea una nueva lista de imágenes en el orden especificado por el usuario
            self.imagenes = [self.imagenes[i] for i in orden]
        else:
            print("Error: Índices fuera de rango")

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3 4): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_2x2.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


class CollageAppFive:
    def __init__(self):
        self.ventana_collage_2x3 = tk.Toplevel()
        self.ventana_collage_2x3.geometry("1250x1250")
        self.ventana_collage_2x3.resizable(False, False)

        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_2x3)
        self.alto_entry = tk.Entry(self.ventana_collage_2x3)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_2x3)
        self.alto_entry = tk.Entry(self.ventana_collage_2x3)

        tk.Button(
            self.ventana_collage_2x3,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_2x3, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_2x3, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_2x3,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_2x3,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(7):
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (250, 250), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 7:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (500, 750))  # Cambia las dimensiones del collage

        # Imágenes en la primera columna, primera fila
        collage.paste(self.imagenes[0].resize((250, 125), Image.Resampling.LANCZOS), (0, 0))
        collage.paste(self.imagenes[1].resize((250, 125), Image.Resampling.LANCZOS), (0, 125))

        # Imagen en la primera columna, segunda fila
        collage.paste(self.imagenes[2], (0, 250))

        # Imágenes en la segunda columna, primera fila
        collage.paste(self.imagenes[3], (250, 0))
        collage.paste(self.imagenes[4].resize((250, 250), Image.Resampling.LANCZOS), (250, 250))

        # Imágenes en la segunda columna, segunda fila
        collage.paste(self.imagenes[5].resize((250, 500), Image.Resampling.LANCZOS), (250, 500))

        # Imagen en la tercera fila
        collage.paste(self.imagenes[6].resize((500, 250), Image.Resampling.LANCZOS), (0, 500))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_2x3, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        # Escalar y pegar las imágenes en el collage personalizado
        collage_personalizado.paste(
            self.imagenes[0].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS), (0, 0)
        )
        collage_personalizado.paste(
            self.imagenes[1].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS),
            (0, alto // 6),
        )
        collage_personalizado.paste(
            self.imagenes[2].resize((ancho // 2, alto // 3), Image.Resampling.LANCZOS),
            (0, alto // 3),
        )
        collage_personalizado.paste(
            self.imagenes[3].resize((ancho // 2, alto // 2), Image.Resampling.LANCZOS),
            (ancho // 2, 0),
        )
        collage_personalizado.paste(
            self.imagenes[4].resize((ancho // 2, alto // 2), Image.Resampling.LANCZOS),
            (ancho // 2, alto // 2),
        )
        collage_personalizado.paste(
            self.imagenes[5].resize((ancho // 2, alto // 3), Image.Resampling.LANCZOS),
            (ancho // 2, alto),
        )
        collage_personalizado.paste(
            self.imagenes[6].resize((ancho, alto // 2), Image.Resampling.LANCZOS), (0, alto)
        )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Verificar que los índices en el orden estén dentro del rango
        if all(0 <= i < len(self.imagenes) for i in orden):
            # Crea una nueva lista de imágenes en el orden especificado por el usuario
            self.imagenes = [self.imagenes[i] for i in orden]
        else:
            print("Error: Índices fuera de rango")

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3 4 5 6): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_2x3.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


class CollageAppSix:
    def __init__(self):
        self.ventana_collage_2x3 = tk.Toplevel()
        self.ventana_collage_2x3.geometry("1250x950")
        self.ventana_collage_2x3.resizable(False, False)

        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_2x3)
        self.alto_entry = tk.Entry(self.ventana_collage_2x3)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_2x3)
        self.alto_entry = tk.Entry(self.ventana_collage_2x3)

        tk.Button(
            self.ventana_collage_2x3,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_2x3, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_2x3, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_2x3,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_2x3,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(8):
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (250, 250), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 8:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (500, 750))  # Cambia las dimensiones del collage

        # Imagen en la columna 1, fila 1
        collage.paste(self.imagenes[0], (0, 0))

        # Imágenes en la columna 1, fila 2 (reescaladas más pequeñas)
        collage.paste(self.imagenes[1].resize((250, 125), Image.Resampling.LANCZOS), (0, 250))
        collage.paste(self.imagenes[2].resize((250, 125), Image.Resampling.LANCZOS), (0, 375))

        # Imagen en la columna 1, fila 3
        collage.paste(self.imagenes[3], (0, 500))

        # Imagen en la columna 2, fila 1
        collage.paste(self.imagenes[4], (250, 0))

        # Imagen en la columna 2, fila 2 (ocupa toda la fila)
        collage.paste(self.imagenes[5].resize((250, 250), Image.Resampling.LANCZOS), (250, 250))

        # Imágenes en la columna 2, fila 3 (reescaladas más pequeñas)
        collage.paste(self.imagenes[6].resize((250, 125), Image.Resampling.LANCZOS), (250, 500))
        collage.paste(self.imagenes[7].resize((250, 125), Image.Resampling.LANCZOS), (250, 625))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_2x3, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        # Pegar las imágenes en el collage personalizado según la distribución
        collage_personalizado.paste(
            self.imagenes[0].resize((ancho // 2, alto // 3), Image.Resampling.LANCZOS), (0, 0)
        )
        collage_personalizado.paste(
            self.imagenes[1].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS),
            (0, alto // 3),
        )
        collage_personalizado.paste(
            self.imagenes[2].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS),
            (0, alto // 2),
        )
        collage_personalizado.paste(
            self.imagenes[3].resize((ancho // 2, alto // 3), Image.Resampling.LANCZOS),
            (0, 2 * (alto // 3)),
        )
        collage_personalizado.paste(
            self.imagenes[4].resize((ancho // 2, alto), Image.Resampling.LANCZOS),
            (ancho // 2, 0),
        )
        collage_personalizado.paste(
            self.imagenes[5].resize((ancho // 2, alto), Image.Resampling.LANCZOS),
            (ancho // 2, alto // 2),
        )
        collage_personalizado.paste(
            self.imagenes[6].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS),
            (ancho // 2, 0),
        )
        collage_personalizado.paste(
            self.imagenes[7].resize((ancho // 2, alto // 6), Image.Resampling.LANCZOS),
            (ancho // 2, alto // 6),
        )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Verificar que los índices en el orden estén dentro del rango
        if all(0 <= i < len(self.imagenes) for i in orden):
            # Crea una nueva lista de imágenes en el orden especificado por el usuario
            self.imagenes = [self.imagenes[i] for i in orden]
        else:
            print("Error: Índices fuera de rango")

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3 4 5 6 7): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_2x3.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk


class CollageAppFour:
    def __init__(self):
        self.ventana_collage_1x3 = tk.Toplevel()
        self.ventana_collage_1x3.geometry("1250x950")
        self.ventana_collage_1x3.resizable(False, False)

        self.imagenes = []

        # Nuevos atributos para almacenar las dimensiones del collage
        self.ancho_entry = tk.Entry(self.ventana_collage_1x3)
        self.alto_entry = tk.Entry(self.ventana_collage_1x3)

    def crear_botones(self):
        # Crea de nuevo los widgets Entry
        self.ancho_entry = tk.Entry(self.ventana_collage_1x3)
        self.alto_entry = tk.Entry(self.ventana_collage_1x3)

        tk.Button(
            self.ventana_collage_1x3,
            text="Cargar Imágenes",
            command=self.cargar_imagenes,
        ).pack()

        # Agregar Entries para ancho y alto
        tk.Label(self.ventana_collage_1x3, text="Ancho:").pack()
        self.ancho_entry.pack()
        tk.Label(self.ventana_collage_1x3, text="Alto:").pack()
        self.alto_entry.pack()

        # Botón para guardar el collage con dimensiones personalizadas
        tk.Button(
            self.ventana_collage_1x3,
            text="Guardar Collage",
            command=self.guardar_collage,
        ).pack()

        # Botón para reordenar y mostrar el collage
        tk.Button(
            self.ventana_collage_1x3,
            text="Reordenar y Mostrar Collage",
            command=self.pedir_orden,
        ).pack()

    def cargar_imagenes(self):
        for i in range(5):
            ruta_imagen = filedialog.askopenfilename(
                title="Seleccionar Imagen {}".format(i + 1),
                filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                break  # El usuario canceló la selección

            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize(
                (250, 250), Image.Resampling.LANCZOS
            )  # Ajusta el tamaño según tus necesidades

            self.imagenes.append(imagen)

        if len(self.imagenes) == 5:
            self.mostrar_collage()

    def mostrar_collage(self):
        collage = Image.new("RGB", (750, 750))  # Cambia las dimensiones del collage

        # Imágenes en la columna 1, fila 1 (juntas horizontalmente)
        collage.paste(self.imagenes[0], (0, 0))
        collage.paste(self.imagenes[1], (250, 0))
        collage.paste(self.imagenes[2], (500, 0))

        # Imagen en la columna 1, fila 2 (se alarga para llenar el espacio)
        collage.paste(self.imagenes[3].resize((750, 250), Image.Resampling.LANCZOS), (0, 250))

        # Imagen en la columna 1, fila 3 (se alarga para llenar el espacio)
        collage.paste(self.imagenes[4].resize((750, 250), Image.Resampling.LANCZOS), (0, 500))

        collage_tk = ImageTk.PhotoImage(collage)
        label_collage = tk.Label(self.ventana_collage_1x3, image=collage_tk)
        label_collage.photo = collage_tk
        label_collage.pack()

    def guardar_collage(self):
        # Obtener las dimensiones ingresadas por el usuario
        ancho = int(self.ancho_entry.get())
        alto = int(self.alto_entry.get())

        # Crear una nueva imagen con las dimensiones proporcionadas
        collage_personalizado = Image.new("RGB", (ancho, alto))

        # Pegar las imágenes en el collage personalizado según la distribución
        collage_personalizado.paste(
            self.imagenes[0].resize((ancho // 3, alto), Image.Resampling.LANCZOS), (0, 0)
        )
        collage_personalizado.paste(
            self.imagenes[1].resize((ancho // 3, alto), Image.Resampling.LANCZOS),
            (ancho // 3, 0),
        )
        collage_personalizado.paste(
            self.imagenes[2].resize((ancho // 3, alto), Image.Resampling.LANCZOS),
            (2 * (ancho // 3), 0),
        )
        collage_personalizado.paste(
            self.imagenes[3].resize((ancho, alto // 2), Image.Resampling.LANCZOS), (0, alto // 2)
        )
        collage_personalizado.paste(
            self.imagenes[4].resize((ancho, alto // 2), Image.Resampling.LANCZOS), (0, alto // 2)
        )

        # Guardar el collage personalizado
        ruta_guardar = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg")],
        )
        if ruta_guardar:
            collage_personalizado.save(ruta_guardar)

    def reordenar_imagenes(self, orden):
        # Verificar que los índices en el orden estén dentro del rango
        if all(0 <= i < len(self.imagenes) for i in orden):
            # Crea una nueva lista de imágenes en el orden especificado por el usuario
            self.imagenes = [self.imagenes[i] for i in orden]
        else:
            print("Error: Índices fuera de rango")

    def pedir_orden(self):
        # Pide al usuario que ingrese el orden de las imágenes
        orden = simpledialog.askstring(
            "Orden de las imágenes",
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3 4): ",
        )

        # Convierte el orden a una lista de enteros
        orden = list(map(int, orden.split()))

        # Reordena las imágenes
        self.reordenar_imagenes(orden)

        # Limpia el collage actual
        for widget in self.ventana_collage_1x3.winfo_children():
            widget.destroy()

        # Vuelve a mostrar el collage con las imágenes reordenadas
        self.mostrar_collage()

        # Genera de nuevo los entries y los botones
        self.crear_botones()


class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Imágenes")
        self.root.geometry("1250x650")
        self.root.minsize(1200, 650)  # Ancho x Alto

        self.colorbg = "#27374D"
        self.sidemenucolorbg = "#526D82"
        self.botonesbg = "#9DB2BF"

        self.historial = []
        self.frames = []

        self.create_menu_frame()
        self.create_content_frame()
        self.desactivar_botones()
        self.create_functionbotones()

        self.root.bind(
            "<Control-o>", lambda event: self.cargar_imagen(event)
        )  # Ctrl+O para cargar imagen
        self.root.bind(
            "<Control-z>", lambda event: self.undo(event)
        )  # Ctrl+Z para deshacer
        self.root.bind(
            "<Control-e>", lambda event: self.Ecualización(event)
        )  # Ctrl+E para Ecualización
        self.root.bind(
            "<Control-i>", lambda event: self.InversionB(event)
        )  # Ctrl+I para Inversion Binaria
        self.root.bind(
            "<Control-f>", lambda event: self.inversionF(event)
        )  # Ctrl+F para Inversion Fotografica
        self.root.bind(
            "<Control-c>", lambda event: self.collage(event)
        )  # Ctrl+C para collage
        self.root.bind(
            "<Control-a>", lambda event: self.adicion(event)
        )  # Ctrl+A para Adición
        self.root.bind(
            "<Control-s>", lambda event: self.sustraccion(event)
        )  # Ctrl+E para Sustracción
        self.root.bind(
            "<Control-r>", lambda event: self.Rotar(event)
        )  # Ctrl+R para rotar 45°
        self.root.bind(
            "<Control-m>", lambda event: self.Espejo(event)
        )  # Ctrl+M para Espejo
        self.root.bind(
            "<Control-l>", lambda event: self.Filtros(event)
        )  # Ctrl+L para Filtros
        self.root.bind(
            "<Alt-r>", lambda event: self.Erosionar(event)
        )  # Ctrl+E para Erosionar
        self.root.bind(
            "<Alt-d>", lambda event: self.Dilatar(event)
        )  # Ctrl+D para Dilatar
        self.root.bind(
            "<Alt-o>", lambda event: self.CambiodeColordeOjos(event)
        )  # Ctrl+O para Cambio de color de ojos
        self.root.bind(
            "<Alt-i>", lambda event: self.info(event)
        )  # Alt+I para Informacion de la imagen

        self.root.bind(
            "<Control-g>", lambda event: self.save_image(event)
        )  # Ctrl+G para Guardar

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.botonesbg)
        self.menu_frame.pack(side="left", fill="y")

        self.create_buttons()

    def create_content_frame(self):
        self.contenido_frame = tk.Frame(self.root, bg=self.colorbg)
        self.contenido_frame.pack(expand=True, fill="both")

        self.label = tk.Label(
            self.contenido_frame,
            text="Cargue una imagen para empezar",
            font=("Montserrat", 25),
            bg=self.colorbg,
            fg="White",
        )
        self.label.pack(expand=True, fill="both")

    def create_buttons(self):
        self.boton_width = 20
        buttons_data = [
            ("Ecualización", self.Ecualización),
            ("Inversion binaria", self.InversionB),
            ("Inversión fotográfica", self.inversionF),
            ("Crear collage", self.collage),
            ("Adición", self.adicion),
            ("Sustracción", self.sustraccion),
            ("Rotar imagen 45°", self.Rotar),
            ("Espejo", self.Espejo),
            ("Filtros", self.Filtros),
            ("Erosionar", self.Erosionar),
            ("Dilatar", self.Dilatar),
            ("Modificar color de ojos", self.CambiodeColordeOjos),
            ("Segmentación para \n N renglones", self.Segmentación),
        ]

        for text, command in buttons_data:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                width=self.boton_width,
                font=("Montserrat"),
                bg=self.botonesbg,
            )
            button.pack()

    def create_functionbotones(self):
        menu_superior = tk.Menu(self.root)
        opcion1 = tk.Menu(menu_superior, tearoff=0)
        opcion1.add_command(label="Reiniciar", command=self.reset)
        opcion1.add_command(label="Cargar una nueva imagen", command=self.cargar_imagen)
        opcion1.add_command(label="Guardar imagen", command=self.save_image)
        opcion1.add_command(label="Informacion de la imagen", command=self.info)
        opcion1.add_separator()
        opcion1.add_command(
            label="Convertir a \n escala de grises",
            command=self.ConvertirEscaladeGrises,
        )
        opcion1.add_separator()
        opcion1.add_command(label="Salir", command=self.root.quit)
        menu_superior.add_cascade(label="Archivo", menu=opcion1)

        self.root.config(menu=menu_superior)
        opcion2 = tk.Menu(menu_superior, tearoff=0)
        opcion2.add_command(label="Ayuda", command=self.help_buttons)

        menu_superior.add_cascade(label="Ayuda", menu=opcion2)

        menu_superior.add_command(
            label="Deshacer ultimo cambio", command=self.undo, compound="left"
        )

        self.botonLoadImage = tk.Button(
            self.contenido_frame,
            text="Cargar imagen",
            width=20,
            height=5,
            font=("Montserrat"),
            bg=self.colorbg,
            fg="White",
            command=self.cargar_imagen,
        )
        self.botonLoadImage.pack(pady=75)

    def cargar_imagen(self, event=None):
        # Verificar que se selecciono una imagen

        # Verificar si cargo una imagen anteriormente
        if hasattr(self, "image_label"):
            # Eliminar la imagen anterior junto con el historial de cambios
            self.image_label.destroy()
            self.image_labelProcesada.destroy()
            self.historial = []

        self.image_labelProcesada = tk.Label(self.contenido_frame)
        # Para mostrar la imagen procesada de lado derecho
        self.image_labelProcesada.pack(side="right")

        self.image_label = tk.Label(self.contenido_frame)  # Para mostrar la imagen
        self.image_label.pack()
        filetypes = [
            ("Archivos de imagen", "*.jpg *.tif *.bmp *.ppm *.jpeg *.png"),
            ("Todos los archivos", "*.*"),
        ]
        self.rutadeArchivo = filedialog.askopenfilename(
            title="Seleccione una imagen", filetypes=filetypes
        )
        if self.rutadeArchivo:
            self.imagen = Image.open(self.rutadeArchivo)
            self.mostrar_imagen(self.imagen)
            self.imagen_procesada = self.imagen
            self.historial.append(self.imagen)
            self.botonLoadImage.destroy()
            self.label.destroy()
            self.activar_botones()

        else:
            messagebox.showerror("Error", "No se seleccionó ninguna imagen.")
            self.desactivar_botones()
            return None

    def save_image(self, event=None):
        if hasattr(self, "imagen_procesada"):
            filetypes = [
                ("Archivos de imagen", "*.jpg;*.png;*.tif;*.bmp"),
                ("JPEG", "*.jpg"),
                ("PNG", "*.png"),
                ("TIFF", "*.tif"),
                ("BMP", "*.bmp"),
            ]
            ruta_guardado = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=filetypes
            )
            if ruta_guardado:
                self.imagen_procesada.save(ruta_guardado)
                messagebox.showinfo("Guardado", "La imagen se ha guardado.")
        else:
            messagebox.showerror("Error", "No hay una imagen procesada para guardar.")

    def info(self, event=None):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        # Obtener el tamaño de la imagen
        width, height = image.size

        # Obtener el modo de la imagen
        mode = image.mode

        # Obtener el formato de la imagen
        format = image.format

        # Obtener el nombre del archivo
        filename = self.rutadeArchivo

        # Obtener el tamaño del archivo
        file_size = os.path.getsize(filename)

        # Obtener la fecha de modificación del archivo
        file_date = time.ctime(os.path.getmtime(filename))

        # Obtener el nombre del archivo
        file_name = os.path.basename(filename)

        # Obtener el directorio del archivo
        file_dir = os.path.dirname(filename)

        messagebox.showinfo(
            "Informacion de la imagen",
            "Tamaño de la imagen: {} x {}\nModo de la imagen: {}\nFormato de la imagen: {}\nTamaño del archivo: {}\nFecha de modificación: {}\nNombre del archivo: {}\nDirectorio del archivo: {}".format(
                width, height, mode, format, file_size, file_date, file_name, file_dir
            ),
        )

    def help_buttons(self):
        # Use sys._MEIPASS when running from PyInstaller executable
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(os.path.dirname(__file__))

        # Construct the full path to the HTML file
        html_path = os.path.join(base_path, "help.html")

        # Check if the HTML file exists before trying to open it
        if os.path.exists(html_path):
            # Open the HTML file in the default web browser
            webbrowser.open("file://" + html_path, new=2)
        else:
            print(f"The HTML file '{html_path}' does not exist.")

    def mostrar_imagen(self, imagen):
        if imagen:
            max_width = 1000
            max_height = 600
            width, height = imagen.size

            # Calcula el factor de escala para ajustar la imagen a la ventana
            width_ratio = max_width / width
            height_ratio = max_height / height
            ratio = min(width_ratio, height_ratio)

            # Redimensiona la imagen proporcionalmente
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            imagen = imagen.resize((new_width, new_height))

            # Muestra la imagen
            photo = ImageTk.PhotoImage(imagen)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.image_label.pack(expand=True, anchor="center", padx=50, pady=50)

        self.label.destroy()

    def mostrar_imagenProcesada(self, imagen):
        if imagen:
            max_width = 1000
            max_height = 600
            width, height = imagen.size

            # Calcula el factor de escala para ajustar la imagen a la ventana
            width_ratio = max_width / width
            height_ratio = max_height / height
            ratio = min(width_ratio, height_ratio)

            # Redimensiona la imagen proporcionalmente
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            imagen = imagen.resize((new_width, new_height))

            # Muestra la imagen
            photo = ImageTk.PhotoImage(imagen)
            self.image_labelProcesada.config(image=photo)
            self.image_labelProcesada.image = photo
            self.image_labelProcesada.pack(
                expand=True, anchor="center", padx=50, pady=50
            )

        self.label.destroy()

    def ShowImageandSave(self, imagen):
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def undo(self, event=None):
        if len(self.historial) > 1:
            self.historial.pop()
            ultimaimagen = self.historial[-1]
            self.imagen_procesada = ultimaimagen
            self.imagen = ultimaimagen
            self.mostrar_imagenProcesada(ultimaimagen)
        else:
            messagebox.showerror("Error", "No hay cambios que deshacer")

    def HistorialdeCambios(self, Image):
        self.historial.append(Image)

    def Ecualización(self, event=None):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = image.convert("L")
        image = np.array(image)

        histoOriginal = cv2.calcHist([image], [0], None, [256], [0, 256])
        image = cv2.equalizeHist(image)
        histoEcualizada = cv2.calcHist([image], [0], None, [256], [0, 256])

        histoOriginal = histoOriginal / histoOriginal.sum()
        histoEcualizada = histoEcualizada / histoEcualizada.sum()

        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.ShowImageandSave(self.imagen_procesada)

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        axes[0].plot(histoOriginal, color="black")
        axes[0].set_title("Histograma Original")

        axes[1].plot(histoEcualizada, color="red")
        axes[1].set_title("Histograma Ecualizado")

        plt.show()

    def InversionB(self, event=None):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        # Convertir la imagen a escala de grises (blanco y negro)
        image = image.convert("L")

        # Invertir los colores (inversión binaria)
        image = Image.eval(image, lambda x: 255 if x < 128 else 0)

        self.imagen_procesada = image
        self.ShowImageandSave(self.imagen_procesada)
        pass

    def inversionF(self, event=None):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        # Verificar si la imagen tiene canales RGB
        if image.mode == "RGB":
            # La imagen tiene canales RGB
            self.invertida = Image.eval(image, lambda x: 255 - x)
            self.imagen_procesada = self.invertida
            self.ShowImageandSave(self.imagen_procesada)
        else:
            # La imagen no tiene canales RGB, manejar según sea necesario
            messagebox.showinfo(
                "Info",
                "La imagen no tiene canales RGB. No se puede aplicar la inversión fotográfica.",
            )

    def seleccionar_imagen(self):
        # Abrir una ventana de diálogo para seleccionar la imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")],
        )

        if not ruta_imagen:
            messagebox.showerror("Error", "No se seleccionó ninguna imagen.")
            return None

        return Image.open(ruta_imagen)

    def seleccionar_imagen(self):
        # Abrir una ventana de diálogo para seleccionar la imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")],
        )

        if not ruta_imagen:
            messagebox.showerror("Error", "No se seleccionó ninguna imagen.")

            return None

        return Image.open(ruta_imagen)

    def adicion(self, event=None):
        if hasattr(self, "imagen_procesada"):
            imagen_base = self.imagen_procesada
        else:
            imagen_base = self.imagen

        # Seleccionar una nueva imagen
        nueva_imagen = self.seleccionar_imagen()

        if nueva_imagen is None:
            return

        # Redimensionar la nueva imagen para que tenga las mismas dimensiones que la imagen base
        nueva_imagen = nueva_imagen.resize(imagen_base.size)

        # Convertir ambas imágenes a arrays NumPy
        base_array = np.array(imagen_base)
        nueva_imagen_array = np.array(nueva_imagen)

        if base_array.shape != nueva_imagen_array.shape:
            messagebox.showerror(
                "Error",
                "Las imágenes deben tener la misma cantidad de canales. Por favor, seleccione otra imagen.",
            )
            return
        else:
            # Combinar las dos imágenes, por ejemplo, sumando los valores de píxeles
            imagen_combinada_array = np.clip(base_array + nueva_imagen_array, 0, 255)

            # Convertir el array combinado de nuevo a una imagen Pillow
            imagen_combinada = Image.fromarray(
                np.array(imagen_combinada_array, dtype=np.uint8)
            )

            self.imagen_procesada = imagen_combinada
            self.mostrar_imagenProcesada(self.imagen_procesada)
            self.HistorialdeCambios(self.imagen_procesada)

    def sustraccion(self, event=None):
        if hasattr(self, "imagen_procesada"):
            imagen_base = self.imagen_procesada
        else:
            imagen_base = self.imagen

        base_array = np.array(imagen_base)
        # Seleccionar una nueva imagen
        segunda_imagen = self.seleccionar_imagen()
        nueva_imagen_array = np.array(segunda_imagen)

        if segunda_imagen is None:
            return
        else:
            if base_array.shape != nueva_imagen_array.shape:
                messagebox.showerror(
                    "Error",
                    "Las imágenes deben tener la misma cantidad de caneles. Por favor, seleccione otra imagen.",
                )
                return
            else:
                # Redimensionar la segunda imagen para que tenga las mismas dimensiones que la imagen base
                segunda_imagen = segunda_imagen.resize(imagen_base.size)

                # Convertir ambas imágenes a arrays NumPy
                base_array = np.array(imagen_base)
                segunda_imagen_array = np.array(segunda_imagen)

                # Realizar la operación de sustracción de píxeles
                imagen_sustraida_array = np.clip(
                    base_array - segunda_imagen_array, 0, 255
                )

                # Convertir el array resultante de nuevo a una imagen Pillow
                imagen_sustraida = Image.fromarray(
                    np.array(imagen_sustraida_array, dtype=np.uint8)
                )

                self.imagen_procesada = imagen_sustraida
                self.mostrar_imagenProcesada(self.imagen_procesada)
                self.HistorialdeCambios(self.imagen_procesada)

    def collage(self, event=None):
        def resource_path(relative_path):
            """Get absolute path to resource, works for dev and for PyInstaller"""
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        self.ventana_collage = tk.Toplevel(ventana)
        self.ventana_collage.geometry("1250x650")
        self.ventana_collage.resizable(False, False)
        frames = []

        for i in range(2):
            for j in range(3):
                frame = tk.Frame(self.ventana_collage)
                frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                frames.append(frame)

        imagen_1x1_path = resource_path("2x2.png")
        imagen_1x1 = PhotoImage(file=imagen_1x1_path)
        self.label_1x1 = tk.Label(frames[0], image=imagen_1x1)
        self.label_1x1.image = imagen_1x1
        self.label_1x1.pack(expand=True, fill="both")
        self.boton_1x1 = tk.Button(
            frames[0], text="Seleccionar", command=self.collage_2_2
        )
        self.boton_1x1.pack()

        imagen_2x3_path = resource_path("2x3.png")
        imagen_2x3 = PhotoImage(file=imagen_2x3_path)
        self.label_2x3 = tk.Label(frames[1], image=imagen_2x3)
        self.label_2x3.image = imagen_2x3
        self.label_2x3.pack(expand=True, fill="both")
        self.boton_1x2 = tk.Button(
            frames[1], text="Seleccionar", command=self.collage_3_2
        )
        self.boton_1x2.pack()

        imagen_3x3_path = resource_path("3x3.png")
        imagen_3x3 = PhotoImage(file=imagen_3x3_path)
        self.label_3x3 = tk.Label(frames[2], image=imagen_3x3)
        self.label_3x3.image = imagen_3x3
        self.label_3x3.pack(expand=True, fill="both")
        self.boton_1x3 = tk.Button(
            frames[2], text="Seleccionar", command=self.collage_5_2
        )
        self.boton_1x3.pack()

        imagen_4x3_path = resource_path("3x3.png")
        imagen_2x1 = PhotoImage(file=imagen_4x3_path)
        self.label_2x1 = tk.Label(frames[3], image=imagen_2x1)
        self.label_2x1.image = (
            imagen_2x1  # Mantener referencia para evitar que la imagen sea eliminada
        )
        self.label_2x1.pack(expand=True, fill="both")
        self.boton_2x1 = tk.Button(
            frames[3], text="Seleccionar", command=self.collage_6_2
        )
        self.boton_2x1.pack()

        imagen_2x2_path = resource_path("7.png")
        imagen_2x2 = PhotoImage(file=imagen_2x2_path)
        self.label_2x2 = tk.Label(frames[4], image=imagen_2x2)
        self.label_2x2.image = (
            imagen_2x2  # Mantener referencia para evitar que la imagen sea eliminada
        )
        self.label_2x2.pack(expand=True, fill="both")
        self.boton_2x2 = tk.Button(
            frames[4], text="Seleccionar", command=self.ccollage_7_3
        )
        self.boton_2x2.pack()

        imagen_2x3_path = resource_path("8.png")
        imagen_2x3 = PhotoImage(file=imagen_2x3_path)
        self.label_2x3 = tk.Label(frames[5], image=imagen_2x3)
        self.label_2x3.image = (
            imagen_2x3  # Mantener referencia para evitar que la imagen sea eliminada
        )
        self.label_2x3.pack(expand=True, fill="both")
        self.boton_2x3 = tk.Button(
            frames[5], text="Seleccionar", command=self.collage_8_3
        )
        self.boton_2x3.pack()

        # Configurar el peso de las filas y columnas para que se expandan con la ventana
        for i in range(2):
            self.ventana_collage.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.ventana_collage.grid_columnconfigure(j, weight=1)

    def collage_2_2(self):
        # Crear una instancia de CollageApp
        self.ventana_collage.destroy()
        collage_app = CollageAppOne()
        collage_app.crear_botones()

    def collage_3_2(self):
        self.ventana_collage.destroy()
        collage_app = CollageAppTwo()
        collage_app.crear_botones()

    def collage_5_2(self):
        self.ventana_collage.destroy()
        collage_app = CollageAppThree()
        collage_app.crear_botones()

    def collage_6_2(self):
        self.ventana_collage.destroy()
        collage_app = CollageAppFour()
        collage_app.crear_botones()

    def ccollage_7_3(self):
        self.ventana_collage.destroy()
        collage_app = CollageAppFive()
        collage_app.crear_botones()

    def collage_8_3(self):
        self.ventana_collage.destroy()
        collage_app = CollageAppSix()
        collage_app.crear_botones()

    def regresar(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.create_buttons()
        self.create_functionbotones()
        self.botonLoadImage.destroy()
        self.activar_botones()

    def Rotar(self, event=None):
        # Rotar la imagen 45 grados
        if hasattr(self, "imagen_procesada"):
            self.imagen_procesada = self.imagen_procesada.rotate(45)
        else:
            self.imagen = self.imagen.rotate(45)

        # Mostrar la imagen rotada
        self.mostrar_imagenProcesada(self.imagen_procesada)

        # Actualizar el historial de cambios
        self.HistorialdeCambios(self.imagen_procesada)

    def Espejo(self, event=None):
        if hasattr(self, "imagen_procesada"):
            original_image = self.imagen_procesada
        else:
            original_image = self.imagen

        bottom_left = original_image
        top_left = original_image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
        top_right = original_image.rotate(180)
        bottom_right = original_image.transpose(Image.FLIP_LEFT_RIGHT)

        mosaic_image = Image.new(
            "RGB", (original_image.width * 2, original_image.height * 2)
        )
        mosaic_image.paste(bottom_left, (0, original_image.height))
        mosaic_image.paste(top_left, (0, 0))
        mosaic_image.paste(top_right, (original_image.width, 0))
        mosaic_image.paste(bottom_right, (original_image.width, original_image.height))

        self.imagen_procesada = mosaic_image
        self.ShowImageandSave(self.imagen_procesada)

    def Filtros(self, event=None):
        # Deleete buttons from menu_frame
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.menuFiltros = tk.Frame(self.menu_frame, width=150, bg=self.sidemenucolorbg)
        self.menuFiltros.pack(side="left", fill="y")

        self.boton_width = 20
        buttons_data = [
            ("Filtro Moda", self.FiltroModa),
            ("Filtro Media", self.FiltroMedia),
            ("Filtro mediana", self.FiltroMediana),
            ("Filtro Gausiano", self.FiltroGausiano),
            ("Filtro Min", self.FiltroMin),
            ("Filtro Max", self.FiltroMax),
            ("Filtro de orden n", self.filtroOrdenN),
            ("Filtro Laplaciano 4 Vecinos", self.FiltroLaplaciano4Vecinos),
            ("Filtro Laplaciano 8 Vecinos", self.FiltroLaplaciano8Vecinos),
            ("Filtro Prewitt", self.FiltroPrewitt),
            ("Filtro Sobel", self.FiltroSobel),
            ("Filtro Roberts", self.FiltroRoberts),
        ]

        for text, command in buttons_data:
            button = tk.Button(
                self.menuFiltros,
                text=text,
                command=command,
                width=self.boton_width,
                font=("Montserrat"),
                bg=self.botonesbg,
            )
            button.pack()

        # boton para regresar al menu principal
        botonRegresar = tk.Button(
            self.menuFiltros,
            text="Regresar",
            command=self.regresar,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar.config(state="normal")
        botonRegresar.pack(side="bottom")

    def FiltroModa(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Apply the mode filter
        imagemoda_array = Image.fromarray(image_array).filter(ImageFilter.ModeFilter(3))

        # Convert the filtered array back to a Pillow Image
        imagemoda = Image.fromarray(np.array(imagemoda_array, dtype=np.uint8))

        self.imagen_procesada = imagemoda
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroMedia(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        size = 3
        rank = min((size * size - 1), 5)
        image_array = np.array(image)
        image = Image.fromarray(image_array).filter(
            ImageFilter.RankFilter(size=size, rank=rank)
        )
        imageMedia = Image.fromarray(np.array(image, dtype=np.uint8))
        self.imagen_procesada = imageMedia
        self.ShowImageandSave(self.imagen_procesada)

    def filtroOrdenN(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Solicitar al usuario que ingrese el valor de n
        n = simpledialog.askinteger(
            "Valor de n", "Ingrese el valor de n (1-9):", minvalue=1, maxvalue=9
        )

        if n is not None:
            size = 3
            rank = min((size * size - 1), n)

            imagemoda_array = Image.fromarray(image_array).filter(
                ImageFilter.RankFilter(size=size, rank=rank)
            )

            imagemoda = Image.fromarray(np.array(imagemoda_array, dtype=np.uint8))

            self.imagen_procesada = imagemoda
            self.mostrar_imagenProcesada(self.imagen_procesada)
            self.HistorialdeCambios(self.imagen_procesada)

    def FiltroMediana(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = np.array(image)

        image = cv2.medianBlur(image, 3)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroGausiano(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = image.filter(ImageFilter.GaussianBlur(radius=1))

        self.imagen_procesada = image
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroMin(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Apply the mode filter
        imagemoda_array = Image.fromarray(image_array).filter(ImageFilter.MinFilter(3))

        # Convert the filtered array back to a Pillow Image
        imagemoda = Image.fromarray(np.array(imagemoda_array, dtype=np.uint8))

        self.imagen_procesada = imagemoda
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroMax(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Apply the mode filter
        imagemoda_array = Image.fromarray(image_array).filter(ImageFilter.MaxFilter(3))

        # Convert the filtered array back to a Pillow Image
        imagemoda = Image.fromarray(np.array(imagemoda_array, dtype=np.uint8))

        self.imagen_procesada = imagemoda
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroLaplaciano4Vecinos(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Definir el kernel para el filtro laplaciano de 4 vecinos
        kernel_laplaciano = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

        # Aplicar el filtro laplaciano utilizando la función filter2D de OpenCV
        imagen_laplaciano_array = cv2.filter2D(image_array, -1, kernel_laplaciano)

        # Convertir el array filtrado de nuevo a una imagen Pillow
        imagen_laplaciano = Image.fromarray(
            np.array(imagen_laplaciano_array, dtype=np.uint8)
        )

        self.imagen_procesada = imagen_laplaciano
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroLaplaciano8Vecinos(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Definir el kernel para el filtro laplaciano de 8 vecinos
        kernel_laplaciano = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

        # Aplicar el filtro laplaciano utilizando la función filter2D de OpenCV
        imagen_laplaciano_array = cv2.filter2D(image_array, -1, kernel_laplaciano)

        # Convertir el array filtrado de nuevo a una imagen Pillow
        imagen_laplaciano = Image.fromarray(
            np.array(imagen_laplaciano_array, dtype=np.uint8)
        )

        self.imagen_procesada = imagen_laplaciano
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroPrewitt(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar el filtro Prewitt a la imagen
        kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        filtered_image_x = cv2.filter2D(image_array, -1, kernel_x)
        filtered_image_y = cv2.filter2D(image_array, -1, kernel_y)
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroSobel(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar el filtro Sobel a la imagen
        filtered_image_x = cv2.Sobel(image_array, cv2.CV_64F, 1, 0, ksize=3)
        filtered_image_y = cv2.Sobel(image_array, cv2.CV_64F, 0, 1, ksize=3)
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Escalar los valores para que estén en el rango 0-255
        filtered_image = cv2.convertScaleAbs(filtered_image)

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.ShowImageandSave(self.imagen_procesada)

    def FiltroRoberts(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar el filtro Roberts a la imagen
        kernel_x = np.array([[1, 0], [0, -1]])
        kernel_y = np.array([[0, 1], [-1, 0]])
        filtered_image_x = cv2.filter2D(image_array, -1, kernel_x)
        filtered_image_y = cv2.filter2D(image_array, -1, kernel_y)
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.ShowImageandSave(self.imagen_procesada)

    def open_kernel_dialog(self):
        kernel_dialog = tk.Toplevel(self.root)
        kernel_dialog.title("Tamaño del kernel")

        label = tk.Label(
            kernel_dialog, text="Ingrese el tamaño del kernel (entre 3 y 10):"
        )
        label.grid(row=0, column=0, columnspan=2, pady=10)

        spinbox_var = tk.StringVar()
        spinbox_var.set(3)  # Valor inicial

        spinbox = tk.Spinbox(
            kernel_dialog, from_=3, to=10, textvariable=spinbox_var, wrap=True
        )
        spinbox.grid(row=1, column=0, pady=10)

        def apply_erosion():
            kernel_size = int(spinbox_var.get())

            if 3 <= kernel_size <= 10:
                self.apply_erosion_with_custom_kernel(kernel_size)
                kernel_dialog.destroy()
            else:
                messagebox.showerror(
                    "Error", "El tamaño del kernel debe estar entre 3 y 10"
                )

        apply_button = tk.Button(kernel_dialog, text="Aplicar", command=apply_erosion)
        apply_button.grid(row=1, column=1, pady=10)

        kernel_dialog.mainloop()

    def apply_erosion_with_custom_kernel(self, kernel_size):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Crear una ventana para que el usuario defina los valores del kernel
        kernel_dialog = tk.Toplevel(self.root)
        kernel_dialog.title("Definir Kernel")
        kernel_dialog.geometry("300x300")
        kernel_dialog.minsize(300, 300)

        # Crear una matriz de Entry para que el usuario ingrese los valores del kernel
        entries = []
        for i in range(kernel_size):
            row_entries = []
            for j in range(kernel_size):
                entry = tk.Entry(kernel_dialog, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)

        def get_custom_kernel():
            custom_kernel = []
            try:
                for row in entries:
                    row_values = [
                        int(entry.get()) if entry.get().strip() != "" else 0
                        for entry in row
                    ]
            except:
                messagebox.showerror(
                    "Error", "Todos los valores del kernel deben ser números"
                )
                # Que todos los valores del kernel estén entre 0 y 1

                # Convertir los valores de la fila a uint8
                row_values = np.array(row_values, dtype=np.uint8)
                custom_kernel.append(row_values)
            # Convertir la lista de listas a una matriz numpy y devolverla
            return np.array(custom_kernel)

        def apply_custom_erosion():
            custom_kernel = get_custom_kernel()

            if all(0 <= value <= 1 for value in custom_kernel.flatten()):
                eroded_image = cv2.erode(image_array, custom_kernel, iterations=1)
                eroded_image = Image.fromarray(eroded_image)
                self.imagen_procesada = eroded_image
                self.mostrar_imagenProcesada(self.imagen_procesada)
                self.HistorialdeCambios(self.imagen_procesada)
                kernel_dialog.destroy()
            else:
                messagebox.showerror(
                    "Error", "Todos los valores del kernel deben estar entre 0 y 1"
                )

        apply_button = tk.Button(
            kernel_dialog, text="Aplicar", command=apply_custom_erosion
        )
        apply_button.grid(row=kernel_size, columnspan=kernel_size, pady=10)

        kernel_dialog.mainloop()

    def Erosionar(self, event=None):
        self.open_kernel_dialog()

    def apply_dilation_with_custom_kernel(self, kernel_size):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Crear una ventana para que el usuario defina los valores del kernel
        kernel_dialog = tk.Toplevel(self.root)
        kernel_dialog.title("Definir Kernel")
        kernel_dialog.geometry("300x300")
        kernel_dialog.minsize(300, 300)

        # Crear una matriz de Entry para que el usuario ingrese los valores del kernel
        entries = []
        for i in range(kernel_size):
            row_entries = []
            for j in range(kernel_size):
                entry = tk.Entry(kernel_dialog, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)

        def get_custom_kernel():
            custom_kernel = []
            try:
                for row in entries:
                    row_values = [
                        int(entry.get()) if entry.get().strip() != "" else 0
                        for entry in row
                    ]
            except:
                messagebox.showerror(
                    "Error", "Todos los valores del kernel deben ser números"
                )
                # Que todos los valores del kernel estén entre 0 y 1

                # Convertir los valores de la fila a uint8
                row_values = np.array(row_values, dtype=np.uint8)
                custom_kernel.append(row_values)
            # Convertir la lista de listas a una matriz numpy y devolverla
            return np.array(custom_kernel)

        def apply_custom_dilation():
            custom_kernel = get_custom_kernel()

            if all(0 <= value <= 1 for value in custom_kernel.flatten()):
                dilated_image = cv2.dilate(image_array, custom_kernel, iterations=1)
                dilated_image = Image.fromarray(dilated_image)
                self.imagen_procesada = dilated_image
                self.mostrar_imagenProcesada(self.imagen_procesada)
                self.HistorialdeCambios(self.imagen_procesada)
                kernel_dialog.destroy()
            else:
                messagebox.showerror(
                    "Error", "Todos los valores del kernel deben estar entre 0 y 1"
                )

        apply_button = tk.Button(
            kernel_dialog, text="Aplicar", command=apply_custom_dilation
        )
        apply_button.grid(row=kernel_size, columnspan=kernel_size, pady=10)

        kernel_dialog.mainloop()

    def Dilatar(self, event=None):
        self.open_kernel_dialog_for_dilation()

    def open_kernel_dialog_for_dilation(self):
        # Crear una nueva ventana para que el usuario ingrese el tamaño del kernel con Spinbox
        kernel_dialog = tk.Toplevel(self.root)
        kernel_dialog.title("Tamaño del Kernel")
        kernel_dialog.geometry("200x100")

        # Etiqueta y Spinbox para ingresar el tamaño del kernel
        label = tk.Label(kernel_dialog, text="Tamaño del Kernel:")
        label.pack(pady=5)

        spinbox_var = tk.IntVar()
        spinbox = tk.Spinbox(
            kernel_dialog, from_=3, to=10, textvariable=spinbox_var, width=5
        )
        spinbox.pack(pady=5)

        def apply_dilation():
            kernel_size = spinbox_var.get()
            if 3 <= kernel_size <= 10:
                self.apply_dilation_with_custom_kernel(kernel_size)
                kernel_dialog.destroy()
            else:
                messagebox.showerror(
                    "Error", "El tamaño del kernel debe estar entre 3 y 10"
                )

        # Botón para aplicar la dilatación
        apply_button = tk.Button(kernel_dialog, text="Aplicar", command=apply_dilation)
        apply_button.pack(pady=10)

        kernel_dialog.mainloop()

    def ConvertirEscaladeGrises(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = image.convert("L")
        self.imagen_procesada = image
        self.ShowImageandSave(self.imagen_procesada)

    def CambiodeColordeOjos(self, event=None):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        try:
            gris = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        except:
            messagebox.showerror("Error", "La imagen debe estar en formato RGB")
            return

        # Usar un clasificador de ojos más preciso
        def resource_path(relative_path):
                try:
                        # PyInstaller creates a temp folder and stores path in _MEIPASS
                        base_path = sys._MEIPASS
                except Exception:
                        base_path = os.path.abspath(".")

                return os.path.join(base_path, relative_path)

        haarcascade_eye_path = resource_path("haarcascade_eye.xml")

        cascade_ojos = cv2.CascadeClassifier(haarcascade_eye_path)
        
        print(cascade_ojos)


        # Ajustar los parámetros de detectMultiScale
        ojos = cascade_ojos.detectMultiScale(
            gris, scaleFactor=1.4, minNeighbors=7, minSize=(30, 30)
        )

        colorseleccionado = colorchooser.askcolor()[0]
        colorseleccionado = tuple(
            int(c) for c in colorseleccionado
        )  # Convertir a entero

        # Crear una copia de la imagen original para dibujar los círculos de color
        image_circulos = image_array.copy()

        # Recorrer los ojos detectados
        for x, y, w, h in ojos:
            # Extraer el ojo de la imagen
            ojo = gris[y : y + h, x : x + w]

            # Ajustar los parámetros de HoughCircles
            circulos = cv2.HoughCircles(
                ojo,
                cv2.HOUGH_GRADIENT,
                dp=1.5,
                minDist=250,
                param1=120,
                param2=30,
                minRadius=10,
                maxRadius=50,
            )

            if circulos is not None:
                circulos = np.round(circulos[0, :]).astype("int")

                for cx, cy, radio in circulos:
                    # Dibujar un círculo en la imagen de los círculos con el color seleccionado por el usuario
                    cv2.circle(
                        image_circulos, (x + cx, y + cy), radio, colorseleccionado, -1
                    )

        # Combinar la imagen original con la imagen de los círculos
        image_array = cv2.addWeighted(image_array, 0.7, image_circulos, 0.3, 0)

        image_array = Image.fromarray(image_array)
        self.imagen_procesada = image_array
        self.ShowImageandSave(self.imagen_procesada)

    def Segmentación_old(self):
        # Utilizar operador ternario para simplificar la asignación de la imagen
        image = (
            self.imagen_procesada if hasattr(self, "imagen_procesada") else self.imagen
        )

        image = image.convert("L")

        _, threshold_image = cv2.threshold(
            np.array(image), 128, 255, cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        image_with_contours_np = np.array(self.imagen)

        # Utilizar list comprehension para simplificar el dibujo de rectángulos
        [
            cv2.rectangle(
                image_with_contours_np, (x, y), (x + w, y + h), (0, 255, 0), 2
            )
            for x, y, w, h in [cv2.boundingRect(contour) for contour in contours]
        ]

        self.imagen_procesada = Image.fromarray(image_with_contours_np)

        # Llamar a los métodos directamente con la imagen procesada
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def Segmentación(self):
       
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen



        image = image.convert("L")
        #Como mostrar el histograma de la imagen



        hist, _ = np.histogram(np.array(image).ravel(), bins=256, range=[0, 256])

        N = simpledialog.askinteger("Valor de N", "Ingrese el valor de N:")

        picos_indices = np.argsort(-hist)[:N]

        minimos_indices = np.argmin(hist[picos_indices])

        if len(picos_indices) >= 2 and minimos_indices < len(picos_indices) - 1:
            umbral = (
                picos_indices[minimos_indices] + picos_indices[minimos_indices + 1]
            ) // 2
        else:
            umbral = picos_indices[-1]

        _, threshold_image = cv2.threshold(
            np.array(image), umbral, 255, cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )



        # Etiquetar las regiones sobre la imagen
        image_with_labels = np.array(self.imagen)
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image_with_labels, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                image_with_labels,
                str(i + 1),
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        image_with_labels = Image.fromarray(image_with_labels)

        plt.hist(np.array(image).ravel(), bins=256, range=[0, 256])
        plt.show()

        self.imagen_procesada = image_with_labels
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def reset(self):
        self.imagen_procesada = self.imagen
        self.mostrar_imagenProcesada(self.imagen_procesada)

    def desactivar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") != "Salir":
                widget.config(state="disabled")

    def activar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal")


class Collage:
    def __init__(self, image, n_rows, n_cols):
        self.image = image
        self.n_rows = n_rows
        self.n_cols = n_cols



if __name__ == "__main__":
    ventana = tk.Tk()
    app_processing = ImageProcessingApp(ventana)
    ventana.mainloop()
