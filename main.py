
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import cv2
import numpy as np
import matplotlib.pyplot as plt



# from rotate import rotate_image
from text import *

# TODO
#       Cambiar todas las imagenes a jpg Pablo
#       Convertir a escala de gris Cesar  
#       Rescalar las imagenes para mejor presentacion Cesar
#       Modificar el frame para mayor presentacion Jesus ✅
#       Agregar un menu superior para guardar y cargar imagenes Jesus ✅
#       Arreglar los fitlros Jesus ✅
#       Maximo y minimo separado Pablo
#       Filtro de orden n (Popup) Cesar mi primera chamba
#       Filtros de vecinos 4 y 8 Jesus ✅
#       Sustraccion Jesus ✅
#       Adicion Jesus ✅
#       Inversion fotgrafica Jesus ✅
#       Inversion binaria Jesus ✅ 
#       Modificar los kenrels segun el usuario Pablo
#       Falta collage Pablo Jesus



#       Implementar la modificacion de color de ojos  Vemos
#       Implementar la segmentacion para N renglones Cesarin Tilin


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
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.botonesbg)
        self.menu_frame.pack(side="left", fill="y")

        self.create_buttons()

    def create_content_frame(self):
        self.contenido_frame = tk.Frame(self.root, bg=self.colorbg)
        self.contenido_frame.pack(expand=True, fill="both")

        self.contenido_help_frame = tk.Frame(self.root, bg=self.colorbg)
        self.contenido_help_frame.pack(expand=True, fill="both")

        # self.collage_frame = tk.Frame(self.root, bg=self.colorbg)
        # self.collage_frame.pack(expand=True, fill="both")

        self.label = tk.Label(
            self.contenido_frame,
            text="Cargue una imagen para empezar",
            font=("Montserrat", 25),
            bg=self.colorbg,
            fg="White",
        )
        self.label.pack(expand=True, fill="both")

    def call_help_frames(self):
        if not hasattr(self, "help_frame"):  # Verificar si help_frame ya existe
            self.help_frame = tk.Frame(self.contenido_help_frame, bg=self.colorbg)
            self.label_help = tk.Label(
                self.help_frame,
                text=PROCESAMIENTO_IMAGENES,
                font=("Montserrat", 15),
                bg=self.colorbg,
                fg="White",
            )
            self.label_help.pack(expand=True, fill="both")
            self.help_frame.pack(expand=True, fill="both")

    def toggle_frames(self):
        self.call_help_frames()
        if self.contenido_frame.winfo_ismapped():
            self.contenido_frame.pack_forget()
            self.contenido_help_frame.pack(expand=True, fill="both")
        else:
            self.contenido_help_frame.pack_forget()
            self.contenido_frame.pack(expand=True, fill="both")

    def call_collage_frame(self):
        if not hasattr(self, "collage_frame_in"):
            self.collage_frame_in = tk.Frame(self.collage_frame, bg=self.colorbg)

            self.frames = []

            for _ in range(2):
                frame = tk.Frame(self.collage_frame_in, width=400, height=400)
                frame.pack(side="left", padx=5, pady=5)
                self.frames.append(frame)

            self.load_images_button = tk.Button(
                self.collage_frame_in, text="Cargar Imágenes", command=self.load_images
            )
            self.load_images_button.pack(side="bottom", pady=5)

            self.collage_frame_in.pack(expand=True, fill="both", anchor="center")

    def load_images(self):
        collage_images = []

        for _ in range(2):
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
            image = image.resize((400, 400))
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(frame, image=photo)
            label.image = photo
            label.pack()

            photo_images.append(photo)

        self.root.photo_images = photo_images

    def toggle_frames_collage(self):
        self.call_collage_frame()
        if self.contenido_frame.winfo_ismapped():
            self.contenido_frame.pack_forget()
            self.collage_frame.pack(expand=True, fill="both")
        else:
            self.collage_frame.pack_forget()
            self.contenido_frame.pack(expand=True, fill="both")

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
        menu_superior.add_cascade(label="Archivo", menu=opcion1)
        
        self.root.config(menu=menu_superior)
        opcion2 = tk.Menu(menu_superior, tearoff=0)
        opcion2.add_command(label="Ayuda", command=self.help_buttons)
        menu_superior.add_cascade(label="Ayuda", menu=opcion2)

        menu_superior.add_command(
            label="Deshacer ultimo cambio", command=self.undo,compound="left"
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


    def cargar_imagen(self):
        if hasattr(self, "image_label"):
            self.image_label.destroy()
            self.image_labelProcesada.destroy()

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

    def help_buttons(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.menuCollage = tk.Frame(self.menu_frame, width=150, bg=self.sidemenucolorbg)
        self.menuCollage.pack(side="left", fill="y")

        self.boton_width = 20
        buttons_data = [
            ("Procesamiento de Imágenes", self.toggle_frames),
            ("Contenido", self.toggle_frames),
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
        botonRegresar_1 = tk.Button(
            self.menuCollage,
            text="Regresar",
            command=self.regresar,
            width=self.boton_width,
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar_1.config(state="normal")
        botonRegresar_1.pack(side="bottom")

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
            self.image_label.pack(expand=True, anchor="center", padx=50, pady=50)
        self.label.destroy()

    def mostrar_imagenProcesada(self, imagen):

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
            self.image_labelProcesada.config(image=photo)
            self.image_labelProcesada.image = photo
            self.image_labelProcesada.pack(expand=True, anchor="center", padx=50, pady=50)
        self.label.destroy()

    def undo(self):
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
        self.mostrar_imagenProcesada(self.imagen_procesada)
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

        # Convertir la imagen a escala de grises (blanco y negro)
        image = image.convert("L")

        # Invertir los colores (inversión binaria)
        image = Image.eval(image, lambda x: 255 if x < 128 else 0)

        self.imagen_procesada = image
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)
        pass

    def inversionF(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen
        self.invertida = Image.eval(image, lambda x: 255 - x)
        self.imagen_procesada = self.invertida
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

        pass

    def seleccionar_imagen(self):
            # Abrir una ventana de diálogo para seleccionar la imagen
            ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])

            if not ruta_imagen:
                print("No se seleccionó ninguna imagen.")
                return None

            return Image.open(ruta_imagen)

    def seleccionar_imagen(self):
        # Abrir una ventana de diálogo para seleccionar la imagen
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])

        if not ruta_imagen:
            print("No se seleccionó ninguna imagen.")
            return None

        return Image.open(ruta_imagen)

    def adicion(self):
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

        # Combinar las dos imágenes, por ejemplo, sumando los valores de píxeles
        imagen_combinada_array = np.clip(base_array + nueva_imagen_array, 0, 255)

        # Convertir el array combinado de nuevo a una imagen Pillow
        imagen_combinada = Image.fromarray(np.array(imagen_combinada_array, dtype=np.uint8))

        self.imagen_procesada = imagen_combinada
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)



    def sustraccion(self):
        if hasattr(self, "imagen_procesada"):
            imagen_base = self.imagen_procesada
        else:
            imagen_base = self.imagen

        # Seleccionar una nueva imagen
        segunda_imagen = self.seleccionar_imagen()

        if segunda_imagen is None:
            return

        # Redimensionar la segunda imagen para que tenga las mismas dimensiones que la imagen base
        segunda_imagen = segunda_imagen.resize(imagen_base.size)

        # Convertir ambas imágenes a arrays NumPy
        base_array = np.array(imagen_base)
        segunda_imagen_array = np.array(segunda_imagen)

        # Realizar la operación de sustracción de píxeles
        imagen_sustraida_array = np.clip(base_array - segunda_imagen_array, 0, 255)

        # Convertir el array resultante de nuevo a una imagen Pillow
        imagen_sustraida = Image.fromarray(np.array(imagen_sustraida_array, dtype=np.uint8))

        self.imagen_procesada = imagen_sustraida
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def collage(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.menuCollage = tk.Frame(self.menu_frame, width=150, bg=self.sidemenucolorbg)
        self.menuCollage.pack(side="left", fill="y")

        self.boton_width = 20
        buttons_data = [
            ("Basic", self.toggle_frames_collage),
            ("Panel", self.toggle_frames_collage),
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
        # ventana_collage = tk.Toplevel(ventana)
        # app_collage = ImageCollageApp(ventana_collage, app_processing)
        pass

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
        # Rotar la imagen 45 grados
        if hasattr(self, "imagen_procesada"):
            self.imagen_procesada = self.imagen_procesada.rotate(45)
        else:
            self.imagen = self.imagen.rotate(45)

        # Mostrar la imagen rotada
        self.mostrar_imagenProcesada(self.imagen_procesada)

        # Actualizar el historial de cambios
        self.HistorialdeCambios(self.imagen_procesada)

    def Espejo(self):
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
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def Filtros(self):
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
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)
        


    def FiltroMedia(self):
        print ("Filtro Media")
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = np.array(image)
        image = cv2.filter2D(image, -1, np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def FiltroMediana(self):
        print ("Filtro Mediana")
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = np.array(image)

        image = cv2.medianBlur(image, 3)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

        
    def FiltroGausiano(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image = np.array(image)

        image = cv2.GaussianBlur(image, (3, 3), 0)
        image = Image.fromarray(image)
        self.imagen_procesada = image
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

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
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)


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
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)


    def FiltroLaplaciano4Vecinos(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Definir el kernel para el filtro laplaciano de 4 vecinos
        kernel_laplaciano = np.array([[0, 1, 0],
                                      [1, -4, 1],
                                      [0, 1, 0]])

        # Aplicar el filtro laplaciano utilizando la función filter2D de OpenCV
        imagen_laplaciano_array = cv2.filter2D(image_array, -1, kernel_laplaciano)

        # Convertir el array filtrado de nuevo a una imagen Pillow
        imagen_laplaciano = Image.fromarray(np.array(imagen_laplaciano_array, dtype=np.uint8))

        self.imagen_procesada = imagen_laplaciano
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def FiltroLaplaciano8Vecinos(self):
        if hasattr(self, "imagen_procesada"):
            image = self.imagen_procesada
        else:
            image = self.imagen

        image_array = np.array(image)

        # Definir el kernel para el filtro laplaciano de 8 vecinos
        kernel_laplaciano = np.array([[1, 1, 1],
                                      [1, -8, 1],
                                      [1, 1, 1]])

        # Aplicar el filtro laplaciano utilizando la función filter2D de OpenCV
        imagen_laplaciano_array = cv2.filter2D(image_array, -1, kernel_laplaciano)

        # Convertir el array filtrado de nuevo a una imagen Pillow
        imagen_laplaciano = Image.fromarray(np.array(imagen_laplaciano_array, dtype=np.uint8))

        self.imagen_procesada = imagen_laplaciano
        self.mostrar_imagenProcesada(self.imagen_procesada)
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
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagenProcesada(self.imagen_procesada)
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
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Escalar los valores para que estén en el rango 0-255
        filtered_image = cv2.convertScaleAbs(filtered_image)

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagenProcesada(self.imagen_procesada)
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
        filtered_image = cv2.addWeighted(
            filtered_image_x, 0.5, filtered_image_y, 0.5, 0
        )

        # Crear una imagen de Pillow a partir del array resultante
        filtered_image = Image.fromarray(filtered_image)

        self.imagen_procesada = filtered_image
        self.mostrar_imagenProcesada(self.imagen_procesada)
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
        self.mostrar_imagenProcesada(self.imagen_procesada)
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
        self.mostrar_imagenProcesada(self.imagen_procesada)
        self.HistorialdeCambios(self.imagen_procesada)

    def CambiodeColordeOjos(self):
        pass

    def Segmentación(self):
        pass

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


if __name__ == "__main__":
    ventana = tk.Tk()
    
    app_processing = ImageProcessingApp(ventana)
    ventana.mainloop()