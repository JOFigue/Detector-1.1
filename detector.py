import cv2
import numpy as np
import imutils
import os


# Carpeta de positivos, si no existe se crea la carpeta
Datos = 'p'
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Coordenadas para la imagen, asi recortarlas en la resolucion deseada
x1, y1 = 190, 80
x2, y2 = 450,398

count = 0

while True:
    ret, frame =cap.read()
    if ret == False: break
    # Se crea un frame con un rectangulo y un frame copia el cual contiene lo que esta dentro del rectangulo
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    # Reescalar imagen para no demorar el proceso
    objeto = imutils.resize(objeto, width = 38)

    cv2.imshow('frame', frame)
    cv2.imshow('objeto',objeto)

    k = cv2.waitKey(1)
    if k==27:
        break

    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
        count = count + 1

cap.release()
cv2.destroyAllWindows()

