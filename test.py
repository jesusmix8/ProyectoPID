import tkinter as tk
from tkinter import ttk

class MyApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de barra de desplazamiento")

        # Crear un frame para la barra de desplazamiento
        scroll_frame = tk.Frame(self.root)
        scroll_frame.pack(side="left", fill="y")

        # Crear una barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical")

        # Crear un lienzo (Canvas) para contener los botones
        self.menu_canvas = tk.Canvas(scroll_frame, yscrollcommand=scrollbar.set)
        self.menu_canvas.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.menu_canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Crear un frame para contener los botones
        self.menu_frame = tk.Frame(self.menu_canvas, bg="white")
        self.menu_canvas.create_window((0, 0), window=self.menu_frame, anchor="nw")

        # Configurar el lienzo para que sea desplazable
        self.menu_frame.bind("<Configure>", self.on_frame_configure)
        self.menu_canvas.bind("<Configure>", self.on_canvas_configure)

        # Agregar botones
        buttons_data = [
            ("Moda", self.basic),
            ("Media", self.panel),
            # ... otros botones ...
        ]

        for text, command in buttons_data:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                width=20,  # Opcional: Puedes ajustar el ancho aquí
                font=("Montserrat"),
                bg="lightblue",
            )
            button.pack(side="top")

        botonRegresar = tk.Button(
            self.menu_frame,
            text="Regresar",
            command=self.regresar,
            width=20,  # Opcional: Puedes ajustar el ancho aquí
            bg="#0F2C59",
            fg="White",
            font=("Montserrat"),
        )
        botonRegresar.pack(side="top")

        # Inicializar la barra de desplazamiento
        self.menu_canvas.update_idletasks()
        self.menu_canvas.config(scrollregion=self.menu_canvas.bbox("all"))

    def on_frame_configure(self, event):
        self.menu_canvas.config(scrollregion=self.menu_canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.menu_canvas.itemconfig(self.menu_frame, width=canvas_width)

    def basic(self):
        pass

    def panel(self):
        pass

    def regresar(self):
        pass

root = tk.Tk()
app = MyApplication(root)
root.mainloop()
