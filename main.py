import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Imágenes")
        self.root.geometry("1250x650")
        self.root.minsize(1200, 650) # Ancho x Alto

        self.colorbg = "#27374D"
        self.sidemenubg = "#526D82"
        self.botonesbg = "#9DB2BF"

        self.create_menu_frame()
        self.create_content_frame()
        self.create_buttons()
        self.create_functionbotones()
        self.desactivar_botones()
        self.imagen = None  # Variable para almacenar la imagen

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenubg)
        self.menu_frame.pack(side="left", fill="y")

    def create_content_frame(self):
        self.contenido_frame = tk.Frame(self.root, bg=self.colorbg)
        self.contenido_frame.pack(expand=True, fill="both")
        self.label = tk.Label(self.contenido_frame, text="Cargue una imagen para empezar", font=("Montserrat", 25), bg=self.colorbg, fg="White")
        self.label.pack(expand=True, fill="both")
        self.image_label = tk.Label(self.contenido_frame)  # Para mostrar la imagen
        self.image_label.pack()


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
        ]

        for text, command in buttons_data:
            button = tk.Button(self.menu_frame, text=text, command=command, width=self.boton_width, font=("Montserrat"), bg=self.botonesbg)
            button.pack()

    def create_functionbotones(self):
        self.botonLoadImage = tk.Button(self.contenido_frame, text="Cargar imagen", width=20, height=5, font=("Montserrat"), bg=self.colorbg, fg="White", command=self.cargar_imagen)
        self.botonLoadImage.pack(pady=75)
        
        botonSalir = tk.Button(self.menu_frame, text="Salir", command=self.root.destroy, width=self.boton_width, bg="#0F2C59", fg="White", font=("Montserrat"))
        botonSalir.config(state="normal")
        botonSalir.pack(side="bottom" )
        
        botonLoadNewImage = tk.Button(self.menu_frame, text="Cargar una nueva imagen", command=self.cargar_imagen, width=self.boton_width, bg="#0F2C59", fg="White", font=("Montserrat"))
        botonLoadNewImage.config(state="disabled")
        botonLoadNewImage.pack(side="bottom")


    def cargar_imagen(self):
        filetypes = [
        ("Archivos de imagen", "*.jpg *.tif *.bmp *.ppm *.jpeg" ),
        ("Todos los archivos", "*.*")
        ]
        self.rutadeArchivo = filedialog.askopenfilename(title="Seleccione una imagen", filetypes=filetypes )
        if self.rutadeArchivo:
            self.imagen = Image.open(self.rutadeArchivo)
            self.mostrar_imagen(self.imagen)
        self.botonLoadImage.destroy()
        self.label.destroy()
        self.activar_botones()

    def mostrar_imagen(self, imagen):
        if imagen:
            max_width = 1000
            max_height = 600
            width, height = imagen.size
            if width > max_width or height > max_height:
                ratio = min(max_width / width, max_height / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                imagen = imagen.resize((new_width, new_height), Image.BOX)


            photo = ImageTk.PhotoImage(imagen)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.image_label.pack(expand=True, anchor="center")
        self.label.destroy()



    def Ecualización(self):
     pass # Llama al método para actualizar la imagen en el frame de contenido




    def InversionB(self):
        pass

    def inversionF(self):
        # Implementa la lógica para la opción 3
        pass

    def collage(self):
        # Implementa la lógica para la opción 1
        pass

    def Rotar(self):
        image = self.imagen
        imagenRotada = image.rotate(45)
        self.imagen_procesada = imagenRotada
        self.mostrar_imagen(self.imagen_procesada)
        self.actualizar_imagen_procesada(self.imagen_procesada)
        

        

    def Espejo(self):
        # Implementa la lógica para la opción 1
        pass

    def Filtros(self):
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
