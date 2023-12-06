import cv2
import numpy as np

# Cargar la imagens
imagen = cv2.imread('img/img (1).jpg')

imagencv2 = np.array(imagen)
print(imagencv2)
# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Cargar el clasificador en cascada para los ojos
cascade_ojos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Detectar los ojos
ojos = cascade_ojos.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(ojos)

# Porcentaje de reducción del tamaño del rectángulo
porcentaje_reduccion = .8

# Recorrer cada ojo detectado
for (x, y, w, h) in ojos:
    # Calcular el nuevo tamaño del rectángulo
    nuevo_w = int(w * porcentaje_reduccion)
    nuevo_h = int(h * porcentaje_reduccion)

    # Calcular las nuevas coordenadas de la esquina inferior derecha
    nuevo_x = x + nuevo_w
    nuevo_y = y + nuevo_h

    # Dibujar el rectángulo rojo alrededor del ojo con el nuevo tamaño
    cv2.rectangle(imagen, (x, y), (nuevo_x, nuevo_y), (0, 0, 255), 2)

    # Extraer el ojo de la imagen
    ojo = gris[y:nuevo_y, x:nuevo_x]

    # Aplicar un desenfoque gaussiano para reducir el ruido
    ojo = cv2.GaussianBlur(ojo, (5, 5), 0)

    # Detectar los círculos en el ojo utilizando la transformada de Hough
    circulos = cv2.HoughCircles(ojo, cv2.HOUGH_GRADIENT, dp=1.5, minDist=250, param1=90, param2=30, minRadius=10, maxRadius=50)

    # Asegurarse de que se encontró al menos un círculo
    if circulos is not None:
        # Convertir las coordenadas y radios de los círculos a enteros
        circulos = np.round(circulos[0, :]).astype("int")

        # Recorrer los círculos detectados
        for (cx, cy, radio) in circulos:
            # Dibujar el círculo en la imagen
            cv2.circle(imagen, (x+cx, y+cy), radio, (0, 255, 0), 4)

# Mostrar la imagen
imagen = cv2.resize(imagen, (0, 0), fx=0.2, fy=0.2)
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
