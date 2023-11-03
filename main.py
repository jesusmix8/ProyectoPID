import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt


# TODO
# BUG    Arreglar la rotacion de la imagen para que no se pierda informacion
#       Implementar la inversión fotográfica
#       Implementar que al momento de presionar la opcion de filtros abrir un menu con las filtros disponibles y que al seleccionar uno se aplique a la imagen
#       Implementar opciones de erosionar y dilatar
#       Implementar la modificacion de color de ojos
#       Implementar la segmentacion para N renglones
#       Posibilidad de guardar la imagen procesada???????


class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Imágenes")
        self.root.geometry("1250x650")
        self.root.minsize(1200, 650)  # Ancho x Alto

        self.colorbg = "#27374D"
        self.sidemenubg = "#526D82"
        self.botonesbg = "#9DB2BF"

        self.historial = []

        self.create_menu_frame()
        self.create_content_frame()
        self.create_buttons()
        self.create_functionbotones()
        self.desactivar_botones()

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenubg)
        self.menu_frame.pack(side="left", fill="y")

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

        # en la esquina superior izquierda colocar un boton con una imagen para poder deshacer la ultima accion
        self.imagen = Image.open("img/undo.png")
        self.imagen = self.imagen.resize((50, 50), Image.BOX)
        photo = ImageTk.PhotoImage(self.imagen)
        self.botonUndo = tk.Button(
            self.contenido_frame,
            image=photo,
            command=self.undo,
            bg=self.colorbg,
            fg="White",
        )
        self.botonUndo.image = photo
        self.botonUndo.place(x=0, y=0)

    def create_buttons(self):
        self.boton_width = 20
        buttons_data = [
            ("Ecualización", self.Ecualización),
            ("Inversion binaria", self.InversionB),
            ("Inversión fotográfica", self.inversionF),
            ("Crear collage", self.collage),
            ("Rotar imagen 45°", self.Rotar),
            ("Espejo", self.Espejo),
            ("Filtros", self.Filtros),
            ("Erosionar", self.Erosionar),
            ("Dilatar", self.Dilatar),
            ("Modificar color de ojos", self.ojos),
            ("Segmentación para \n N renglones", self.Segmentación),
            ("Reset imagen", self.reset),
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

        botonSalir = tk.Button(
            self.menu_frame,
            text="Salir",
            command=self.root.destroy,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonSalir.config(state="normal")
        botonSalir.pack(side="bottom")

        botonLoadNewImage = tk.Button(
            self.menu_frame,
            text="Cargar una nueva imagen",
            command=self.cargar_imagen,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonLoadNewImage.config(state="disabled")
        botonLoadNewImage.pack(side="bottom")

        boton_save_image = tk.Button(
            self.menu_frame,
            text="Guardar imagen",
            command=self.save_image,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        boton_save_image.config(state="disabled")
        boton_save_image.pack(side="bottom")

    def cargar_imagen(self):
        if hasattr(self, "image_label"):
            self.image_label.destroy()

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

    def save_image(self):
        if hasattr(self, "imagen_procesada"):
            filetypes = [("Archivos de imagen", "*.png"), ("Todos los archivos", "*.*")]
            ruta_guardado = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=filetypes
            )
            if ruta_guardado:
                self.imagen_procesada.save(ruta_guardado)
                messagebox.showinfo("Guardado", "La imagen se ha guardado.")
        else:
            messagebox.showerror("Error", "No hay una imagen procesada para guardar.")

    def mostrar_imagen(self, imagen):
        if imagen:
            max_width = 1000
            max_height = 600
            width, height = imagen.size
            if width > max_width or height > max_height:
                ratio = min(max_width / width, max_height / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                imagen = imagen.resize((new_width, new_height))

            photo = ImageTk.PhotoImage(imagen)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.image_label.pack(expand=True, anchor="center")
        self.label.destroy()

    def undo(self):
        if len(self.historial) > 1:
            self.historial.pop()
            ultimaimagen = self.historial[-1]
            self.imagen_procesada = ultimaimagen
            self.imagen = ultimaimagen
            self.mostrar_imagen(ultimaimagen)
        else:
            messagebox.showerror("Error", "No hay cambios que deshacer")

    def HistorialdeCambios(self, Image):
        self.historial.append(Image)

    def Ecualización(self):
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
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        axes[0].plot(histoOriginal, color="black")
        axes[0].set_title("Histograma Original")

        axes[1].plot(histoEcualizada, color="red")
        axes[1].set_title("Histograma Ecualizado")

        plt.show()

    def InversionB(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen
        self.invertida = Image.eval(image, lambda x: 255 - x)
        self.imagen_procesada = self.invertida
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def inversionF(self):
        pass

    def collage(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenubg)
        self.menu_frame.pack(side="left", fill="y")

        self.boton_width = 20
        buttons_data = [
            ("Basic", self.basic),
            ("Panel", self.panel),
        ]
        # mostrar los botones para elegir el tipo de collage
        for text, command in buttons_data:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                width=self.boton_width,
                font=("Montserrat"),
                bg=self.botonesbg,
            )
            button.pack(side="left")

        # boton para regresar al menu principal
        botonRegresar = tk.Button(
            self.menu_frame,
            text="Regresar",
            command=self.regresar,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar.config(state="normal")
        botonRegresar.pack(side="left")

    # def basic(self):
    #     if hasattr(self, "imagen_procesada"):
    #         # Si ya hay una imagen procesada, úsala como base
    #         img = np.array(self.imagen)
    #     elif hasattr(self, "imagen"):
    #         # Si no, usa la imagen original
    #         img = np.array(self.imagen)
    #     else:
    #         return
    #     # # basic collage
    #     # h_stack = np.hstack((img, img))
    #     # v_stack = np.vstack((h_stack, h_stack))

    #     # self.imagen = Image.fromarray(v_stack)
    #     # self.HistorialdeCambios(self.imagen)
    #     # self.mostrar_imagen(self.imagen)

    #     # generar un frame de 4 x 4 para que en cada frame se coloque una imagen diferente
    #     # y que cada imagen sea la misma

    def basic(self):
        # # generar un frame de 2 x 2 para que en cada frame se coloque una imagen diferente
        # # en cada frame se coloca una imagen diferente
        # if hasattr(self, "imagen_procesada"):
        #     # Si ya hay una imagen procesada, úsala como base
        #     img = np.array(self.imagen)
        # elif hasattr(self, "imagen"):
        #     # Si no, usa la imagen original
        #     img = np.array(self.imagen)
        # else:
        #     return

        # # call the function to create the collage
        # collage = ImageCollageApp(self.root)
        # collage.create_collage(img)

        # if __name__ == "__main__":
        #     ventana = tk.Tk()
        #     app = ImageCollageApp(ventana)
        #     ventana.mainloop()
        pass

    def panel(self):
        pass

    def regresar(self):
        self.menu_frame.destroy()

    def Rotar(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        imagenRotada = image.rotate(45)
        self.imagen_procesada = imagenRotada
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def Espejo(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        imagenEspejo = image.transpose(Image.FLIP_LEFT_RIGHT)
        self.imagen_procesada = imagenEspejo
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def Filtros(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenubg)
        self.menu_frame.pack(side="left", fill="y")

        self.boton_width = 20
        buttons_data = [
            ("Moda", self.basic),
            ("Media", self.panel),
            ("Mediana", self.panel),
            ("Gaussiano", self.panel),
            ("Maximos y minimos", self.panel),
            ("Filtro de Laplaciano", self.panel),
            ("Filtro de prewitt", self.panel),
            ("Filtro de Sobel", self.panel),
            ("Filtro de Roberts", self.panel),
        ]
        # mostrar los botones para elegir el tipo de collage
        for text, command in buttons_data:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                width=self.boton_width,
                font=("Montserrat"),
                bg=self.botonesbg,
            )
            button.pack(side="left")

        botonRegresar = tk.Button(
            self.menu_frame,
            text="Regresar",
            command=self.regresar,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar.config(state="normal")
        botonRegresar.pack(side="left")

        # Implementa la lógica para la opción 1
        pass

    def Erosionar(self):
        # Implementa la lógica para la opción 1
        pass

    def Dilatar(self):
        # Implementa la lógica para la opción 1
        pass

    def ojos(self):
        # Implementa la lógica para la opción 1
        pass

    def Segmentación(self):
        # Implementa la lógica para la opción 1
        pass

    def reset(self):
        self.imagen_procesada = self.imagen
        self.mostrar_imagen(self.imagen_procesada)

    def desactivar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") != "Salir":
                widget.config(state="disabled")

    def activar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal")


class ImageCollageApp:
    def __init__(self, root, image_processing_app):
        self.root = root
        self.root.title("Collage de Imágenes")
        self.root.geometry("800x600")

        self.image_processing_app = image_processing_app

        self.frames = []

        for i in range(2):
            for j in range(2):
                frame = tk.Frame(self.root, width=400, height=300)
                frame.grid(row=i, column=j, padx=5, pady=5)
                self.frames.append(frame)

        self.load_images_button = tk.Button(
            self.root, text="Cargar Imágenes", command=self.load_images
        )
        self.load_images_button.grid(row=2, column=0, columnspan=2, pady=10)

    def load_images(self):
        collage_images = []

        for _ in range(4):
            image_path = filedialog.askopenfilename(
                title="Seleccione una imagen",
                filetypes=[("Archivos de imagen", "*.jpg; *.png")],
            )
            if image_path:
                image = Image.open(image_path)
                collage_images.append(image)

        self.display_images(collage_images)

    def display_images(self, images):
        photo_images = []

        for frame, image in zip(self.frames, images):
            image = image.resize((200, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(frame, image=photo)
            label.image = photo
            label.pack()

            photo_images.append(photo)

        self.root.photo_images = photo_images

        # Aquí llamamos a la función de la clase ImageProcessingApp para mostrar la imagen
        self.image_processing_app.mostrar_imagen(images[0])


if __name__ == "__main__":
    ventana = tk.Tk()
    app_processing = ImageProcessingApp(ventana)

    # Crear una ventana secundaria para ImageCollageApp
    ventana_collage = tk.Toplevel(ventana)
    app_collage = ImageCollageApp(ventana_collage, app_processing)

    ventana.mainloop()
