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
#       Implementar opciones de erosionar y dilatar
#       Implementar la modificacion de color de ojos
#       Implementar la segmentacion para N renglones


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

        self.create_menu_frame()
        self.create_content_frame()
        self.desactivar_botones()
        self.create_functionbotones()
        

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenucolorbg)
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
            ("Modificar color de ojos", self.CambiodeColordeOjos),
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
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.menuCollage = tk.Frame(self.menu_frame, width=150 , bg=self.sidemenucolorbg)
        self.menuCollage.pack(side="left", fill="y" )

        self.boton_width = 20
        buttons_data = [
            ("Basic", self.basic),
            ("Panel", self.panel),
        ]
        # mostrar los botones para elegir el tipo de collage
        for text, command in buttons_data:
            button = tk.Button(
                self.menuCollage,
                text=text,
                command=command,
                width=self.boton_width,
                font=("Montserrat"),
                bg=self.botonesbg,
            )
            button.pack()

        # boton para regresar al menu principal
        botonRegresar = tk.Button(
            self.menuCollage,
            text="Regresar",
            command=self.regresar,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar.config(state="normal")
        botonRegresar.pack(side="bottom")

    def basic(self):
        if hasattr(self, "imagen_procesada"):
            # Si ya hay una imagen procesada, úsala como base
            img = np.array(self.imagen)
        elif hasattr(self, "imagen"):
            # Si no, usa la imagen original
            img = np.array(self.imagen)
        else:
            return
        # basic collage
        h_stack = np.hstack((img, img))
        v_stack = np.vstack((h_stack, h_stack))

        self.imagen = Image.fromarray(v_stack)
        self.HistorialdeCambios(self.imagen)
        self.mostrar_imagen(self.imagen)

    def panel(self):
        pass

    def regresar(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.create_buttons()
        self.create_functionbotones()
        self.botonLoadImage.destroy()
        self.activar_botones()


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
        #Deleete buttons from menu_frame
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.menuFiltros = tk.Frame(self.menu_frame, width=150 , bg=self.sidemenucolorbg)
        self.menuFiltros.pack(side="left", fill="y" )


        self.boton_width = 20
        buttons_data = [
            ("Filtro Moda", self.FiltroModa),
            ("Filtro Media", self.FiltroMedia),
            ("Filtro mediana", self.FiltroMediana),
            ("Filtro Gausiano", self.FiltroGausiano),
            ("Filtro Maximos y minimos", self.FiltroMaxMin),
            ("Filtro Laplaciano", self.FiltroLaplaciano),
            ("Filtro Prewitt", self.FiltroPrewitt),
            ("Filtro Sobel", self.FiltroSobel),
            ("Filtro Roberts", self.FiltroRoberts)
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
        #Aplicar el filtro moda a la imagen
        pass
        

    def FiltroMedia(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = np.array(image)


        image = cv2.blur(image,(3,3))
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

        



    def FiltroMediana(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen
        
        image = np.array(image)

        image = cv2.medianBlur(image,3)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)
        pass

    def FiltroGausiano(self):

        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen
        
        image = np.array(image)

        image = cv2.GaussianBlur(image,(3,3),0)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)


    def FiltroMaxMin(self):
        pass

    def FiltroLaplaciano(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen
        
        image_array = np.array(image)

        # Aplicar el filtro Laplaciano a la imagen
        filtered_image = cv2.Laplacian(image_array, cv2.CV_64F)

        # Escalar los valores para que estén en el rango 0-255
        filtered_image = cv2.convertScaleAbs(filtered_image)

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)


        

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
        filtered_image = cv2.addWeighted(filtered_image_x, 0.5, filtered_image_y, 0.5, 0)

            # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def FiltroSobel(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar el filtro Sobel a la imagen
        filtered_image_x = cv2.Sobel(image_array, cv2.CV_64F, 1, 0, ksize=3)
        filtered_image_y = cv2.Sobel(image_array, cv2.CV_64F, 0, 1, ksize=3)
        filtered_image = cv2.addWeighted(filtered_image_x, 0.5, filtered_image_y, 0.5, 0)

        # Escalar los valores para que estén en el rango 0-255
        filtered_image = cv2.convertScaleAbs(filtered_image)

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)


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
        filtered_image = cv2.addWeighted(filtered_image_x, 0.5, filtered_image_y, 0.5, 0)

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def Erosionar(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar la operación de erosión a la imagen
        kernel = np.ones((3, 3), np.uint8)  # Puedes ajustar el tamaño del kernel
        eroded_image = cv2.erode(image_array, kernel, iterations=1)

        # Crear una imagen de Pillow a partir del array resultante
        eroded_image = Image.fromarray(eroded_image)

        self.imagen_procesada = eroded_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)
       

    def Dilatar(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Aplicar la operación de dilatación a la imagen
        kernel = np.ones((3, 3), np.uint8)  # Puedes ajustar el tamaño del kernel
        dilated_image = cv2.dilate(image_array, kernel, iterations=1)

        # Crear una imagen de Pillow a partir del array resultante
        dilated_image = Image.fromarray(dilated_image)

        self.imagen_procesada = dilated_image
        self.mostrar_imagen(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def CambiodeColordeOjos(self):
        pass

    def Segmentación(self):
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


if __name__ == "__main__":
    ventana = tk.Tk()
    app = ImageProcessingApp(ventana)
    ventana.mainloop()
