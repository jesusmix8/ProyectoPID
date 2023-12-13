import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk


class CollageAppFiveVertical:
    def __init__(self):
        self.ventana_collage_1x3 = tk.Toplevel()
        self.ventana_collage_1x3.geometry("1250x850")
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
                (250, 250), Image.ANTIALIAS
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
        collage.paste(self.imagenes[3].resize((750, 250), Image.ANTIALIAS), (0, 250))

        # Imagen en la columna 1, fila 3 (se alarga para llenar el espacio)
        collage.paste(self.imagenes[4].resize((750, 250), Image.ANTIALIAS), (0, 500))

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
            self.imagenes[0].resize((ancho // 3, alto), Image.ANTIALIAS), (0, 0)
        )
        collage_personalizado.paste(
            self.imagenes[1].resize((ancho // 3, alto), Image.ANTIALIAS),
            (ancho // 3, 0),
        )
        collage_personalizado.paste(
            self.imagenes[2].resize((ancho // 3, alto), Image.ANTIALIAS),
            (2 * (ancho // 3), 0),
        )
        collage_personalizado.paste(
            self.imagenes[3].resize((ancho, alto // 2), Image.ANTIALIAS), (0, alto // 2)
        )
        collage_personalizado.paste(
            self.imagenes[4].resize((ancho, alto // 2), Image.ANTIALIAS), (0, alto // 2)
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
            "Ingresa el orden de las imágenes (p. ej., 0 1 2 3): ",
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


if __name__ == "__main__":
    app = CollageAppFiveVertical()
    app.crear_botones()
    tk.mainloop()
