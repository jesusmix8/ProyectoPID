import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesamiento de Imágenes")
        self.root.geometry("1250x650")
        self.root.minsize(700, 400)

        self.colorbg = "#27374D"
        self.sidemenubg = "#526D82"
        self.botonesbg = "#9DB2BF"

        self.create_menu_frame()
        self.create_content_frame()
        self.create_buttons()

        # Sidemenu 2 (inicialmente oculto)
        self.create_sidemenu2()
        self.hide_sidemenu2()

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=150, bg=self.sidemenubg)
        self.menu_frame.pack(side="left", fill="y")

    def create_content_frame(self):
        self.contenido_frame = tk.Frame(self.root, bg=self.colorbg)
        self.contenido_frame.pack(expand=True, fill="both")
        self.label = tk.Label(self.contenido_frame, text="Cargue una imagen para empezar", font=("Montserrat", 25), bg=self.colorbg, fg="White")
        self.label.pack(expand=True, fill="both")

    def create_buttons(self):
        self.boton_width = 20
        buttons_data = [
            ("Ecualización", self.opcion1),
            ("Mostrar Sidemenu 2", self.toggle_sidemenu2),  # Nuevo botón para mostrar el segundo sidemenu
            ("Salir", self.root.quit)
        ]

        for text, command in buttons_data:
            button = tk.Button(self.menu_frame, text=text, command=command, width=self.boton_width, font=("Montserrat"), bg=self.botonesbg)
            button.pack()

    def create_sidemenu2(self):
        self.sidemenu2_frame = tk.Frame(self.root, width=150, bg="yellow")  # Cambia el color a tu preferencia
        self.sidemenu2_frame.pack(side="left", fill="y")

        # Agrega botones específicos para el sidemenu2
        button = tk.Button(self.sidemenu2_frame, text="Opción 1 del Sidemenu 2", command=self.opcion2, width=self.boton_width, font=("Montserrat"), bg=self.botonesbg)
        button.pack()

    def hide_sidemenu2(self):
        self.sidemenu2_frame.pack_forget()

    def show_sidemenu2(self):
        self.sidemenu2_frame.pack(side="left", fill="y")

    def cargar_imagen(self):
        rutadeArchivo = filedialog.askopenfilename(title="Seleccione una imagen")
        if rutadeArchivo:
            imagen = Image.open(rutadeArchivo)
            return imagen
        return None

    def desactivar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="disabled")

    def activar_botones(self):
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal")

    def opcion1(self):
        # Implementa la funcionalidad de la opción 1 aquí
        pass

    def opcion2(self):
        # Implementa la funcionalidad de la opción 2 aquí
        pass

    def toggle_sidemenu2(self):
        if self.sidemenu2_frame.winfo_viewable():
            self.hide_sidemenu2()
        else:
            self.show_sidemenu2()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ImageProcessingApp(ventana)
    ventana.mainloop()
