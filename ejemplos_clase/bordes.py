import time
import cv2
import numpy as np

class Bordes():
    def __init__(self):
        self.contornos = None
    
    def __call__(self, image):
        t0 = time.time()
       
        # Transformar la imagen en esacala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Aplicar algortimo Canny para encontrar bordes
        # Hay que ajustar los filtros min y max según el
        # fondo y la luz
        edged = cv2.Canny(gray, 50, 400)
        
        # Encontrar los contornos formados por esos bordes
        contours, hierarchy = cv2.findContours(edged, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        self.contornos = contours

        t = time.time()
        print(self.__class__.__name__,'time =', t-t0)

    def draw(self, image):
        # Dibujar todos los contornos en la imagen
        if self.contornos is not None:
            cv2.drawContours(image, self.contornos, -1, (0, 255, 0), 1)
        return image


if __name__ == "__main__":
    # Cargar una de las imagenes disponibles
    image = cv2.imread('objetos.jpg')
    
    # Transformar la imagen en esacala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar algortimo Canny para encontrar bordes
    # Hay que ajustar los filtros min y max según el
    # fondo y la luz
    edged = cv2.Canny(gray, 50, 400)  
    cv2.imwrite("contornos.jpg", edged)

    
    # Encontrar los contornos formados por esos bordes
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print("Cantidad de contornos encontrados " + str(len(contours)))
    
    # Dibujar todos los contornos en la imagen inicial
    cv2.drawContours(image, contours, -1, (0, 255, 0), 1)
    cv2.imwrite("bordes_output.jpg", image)
