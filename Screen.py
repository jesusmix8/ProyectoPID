import tkinter as tk
import main
from tkinter import filedialog
from PIL import Image, ImageTk


def desactivarBotones():
    boton1.config(state="disabled")
    boton2.config(state="disabled")
    boton3.config(state="disabled")
    boton4.config(state="disabled")
    boton5.config(state="disabled")
    boton6.config(state="disabled")
    boton7.config(state="disabled")
    boton8.config(state="disabled")
    boton9.config(state="disabled")
    boton10.config(state="disabled")
    boton11.config(state="disabled")


def activarBotones():
    boton1.config(state="normal")
    boton2.config(state="normal")
    boton3.config(state="normal")
    boton4.config(state="normal")
    boton5.config(state="normal")
    boton6.config(state="normal")
    boton7.config(state="normal")
    boton8.config(state="normal")
    boton9.config(state="normal")
    boton10.config(state="normal")
    boton11.config(state="normal")


def cargarImagen():
    # la imagen que sea
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        # self.image_label.config(image=img)
        # self.image_label.image = img

    activarBotones()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Imágenes")
ventana.geometry("1250x650")
ventana.minsize(700, 400)

colorbg = "#27374D"
sidemenubg = "#526D82"
botonesbg = "#9DB2BF"
botonesfg = "White"
btncongbg = "DDE6ED"

# Crear un marco para el menú lateral
menu_frame = tk.Frame(
    ventana,
    width=1500,
    bg=sidemenubg,
)
menu_frame.pack(side="left", fill="y")


boton_width = 20
# Crear botones en el menú lateral
boton1 = tk.Button(
    menu_frame,
    text="Ecualización",
    command=main.opcion1,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton2 = tk.Button(
    menu_frame,
    text="Inversion binaria",
    command=main.opcion2,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton3 = tk.Button(
    menu_frame,
    text="Inversión fotográfica",
    command=main.opcion3,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton4 = tk.Button(
    menu_frame,
    text="Crear collage",
    command=main.opcion4,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton5 = tk.Button(
    menu_frame,
    text="Rotar imagen 45°",
    command=main.opcion5,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton6 = tk.Button(
    menu_frame,
    text="Espejo",
    command=main.opcion6,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton7 = tk.Button(
    menu_frame,
    text="Filtros",
    command=main.opcion7,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton8 = tk.Button(
    menu_frame,
    text="Erosionar",
    command=main.opcion8,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton9 = tk.Button(
    menu_frame,
    text="Dilatar",
    command=main.opcion9,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton10 = tk.Button(
    menu_frame,
    text="Modificar color de ojos",
    command=main.opcion10,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)
boton11 = tk.Button(
    menu_frame,
    text="Segmentacion para \n N renglones",
    command=main.opcion11,
    width=boton_width,
    font=("Montserrat"),
    bg=botonesbg,
)

boton12 = tk.Button(
    menu_frame,
    text="Salir",
    command=ventana.destroy,
    width=boton_width,
    bg="#0F2C59",
    fg="White",
    font=("Montserrat"),
)

boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()
boton5.pack()
boton6.pack()
boton7.pack()
boton8.pack()
boton9.pack()
boton10.pack()
boton11.pack()
boton12.pack(side="bottom")

# Crear un área de visualización principal en el lado derecho
contenido_frame = tk.Frame(ventana, bg=colorbg)
contenido_frame.pack(expand=True, fill="both")

# Crear un widget para mostrar el contenido principal
label = tk.Label(
    contenido_frame,
    text="Cargue una imagen para empezar",
    font=("Montserrat", 25),
    bg=colorbg,
    fg="White",
)
label.pack(expand=True, fill="both")

botonLoadImage = tk.Button(
    contenido_frame,
    text="Cargar imagen",
    width=20,
    height=5,
    font=("Montserrat"),
    bg="#0F2C59",
    fg="White",
    command=cargarImagen,
)
botonLoadImage.pack(pady=100)


desactivarBotones()
ventana.attributes("-alpha", True)
ventana.mainloop()
