from PIL import Image
import numpy as np
from tkinter import Tk, filedialog

def open_file_dialog():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

    return file_path

def collage_maker():
    print("Select the first image:")
    image1_path = open_file_dialog()

    print("Select the second image:")
    image2_path = open_file_dialog()

    if not image1_path or not image2_path:
        print("Image selection canceled.")
        return

    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Resize images to have the same width
    new_width = min(image1.width, image2.width)
    image1 = image1.resize((new_width, image1.height))
    image2 = image2.resize((new_width, image2.height))

    i1 = np.array(image1).astype(np.uint8)
    i2 = np.array(image2).astype(np.uint8)

    collage = np.vstack([i1, i2])

    new_image = Image.fromarray(collage)
    new_image.save("new.jpg")
    print("Collage saved as new.jpg")

# To Run The Above Function
collage_maker()
