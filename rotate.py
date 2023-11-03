import cv2
import numpy as np
import math


def rotate_image(mat, angle):
    # dimensiones de la imagen
    height, width = mat.shape[:2]
    # punto central
    image_center = (width / 2, height / 2)

    # matriz de rotación
    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)

    # valores absolutos del coseno y seno de la matriz de rotación
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    # nuevas dimensiones del cuadro delimitador
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # ajuste del centro de rotación en la matriz de transformación
    rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    rotation_mat[1, 2] += bound_h / 2 - image_center[1]

    # aplicar rotación a la imagen
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))

    return rotated_mat


def largest_rotated_rect(w, h, angle):
    """
    Dada una caja delimitadora rectangular que ha sido rotada por un ángulo (en
    radianes), calcula las dimensiones del mayor rectángulo (con lados paralelos a los ejes x e y)
    dentro de la caja delimitadora rotada.
    """

    quadrant = int(math.floor(angle / (math.pi / 2))) & 3
    sign_alpha = angle if ((quadrant & 1) == 0) else math.pi - angle
    alpha = (sign_alpha % math.pi + math.pi) % math.pi

    bb_w = w * math.cos(alpha) + h * math.sin(alpha)
    bb_h = w * math.sin(alpha) + h * math.cos(alpha)

    gamma = math.atan2(bb_w, bb_w) if (w < h) else math.atan2(bb_w, bb_w)

    delta = math.pi - alpha - gamma

    length = h if (w < h) else w

    d = length * math.cos(alpha)
    a = d * math.sin(alpha) / math.sin(delta)

    y = a * math.cos(gamma)
    x = y * math.tan(gamma)

    return (x, y)


def crop_around_center(image, width, height):
    image_size = (image.shape[1], image.shape[0])
    image_center = (int(image_size[0] * 0.5), int(image_size[1] * 0.5))

    if width > image_size[0]:
        width = image_size[0]

    if height > image_size[1]:
        height = image_size[1]

    x1 = int(image_center[0] - width * 0.5)
    x2 = int(image_center[0] + width * 0.5)
    y1 = int(image_center[1] - height * 0.5)
    y2 = int(image_center[1] + height * 0.5)

    return image[y1:y2, x1:x2]


# Cargar la imagen
image_path = "img/lena.png"  # Reemplaza esto con la ruta de tu imagen
image = cv2.imread(image_path)

if image is None:
    print(f"No se pudo cargar la imagen en {image_path}")
else:
    # Rotar la imagen
    rotated_image = rotate_image(image, 45)

    # Recortar la imagen rotada
    largest_height, largest_width = largest_rotated_rect(
        rotated_image.shape[1], rotated_image.shape[0], math.radians(45)
    )
    cropped_image = crop_around_center(rotated_image, largest_width, largest_height)

    # Mostrar la imagen recortada
    cv2.imshow("Cropped Rotated Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Cargar la imagen
# image = cv2.imread("img/lena.png")

# # Definir la matriz de rotación (por ejemplo, rotación de 45 grados)
# rotation_matrix = cv2.getRotationMatrix2D(
#     (image.shape[1] / 2, image.shape[0] / 2), 45, 1
# )

# # Aplicar la rotación a la imagen original
# rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# # Ajustar el tamaño de la imagen para contener completamente la rotada
# new_width = int(image.shape[1] * np.sqrt(2))
# new_height = int(image.shape[0] * np.sqrt(2))
# resized_image = cv2.resize(rotated_image, (new_width, new_height))

# # Mostrar la imagen
# cv2.imshow("Rotada y ajustada", resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
