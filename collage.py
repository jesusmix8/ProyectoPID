import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np


class ImageCollageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Collage de Imágenes")
        self.root.geometry("800x600")

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
            label.image = photo  # Mantener una referencia al objeto PhotoImage
            label.pack()

            photo_images.append(photo)

        # Necesario para evitar que los objetos PhotoImage sean eliminados
        self.root.photo_images = photo_images


if __name__ == "__main__":
    ventana = tk.Tk()
    app = ImageCollageApp(ventana)
    ventana.mainloop()
