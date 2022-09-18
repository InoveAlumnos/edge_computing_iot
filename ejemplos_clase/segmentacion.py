import time
import numpy as np
import cv2

class Segmentacion():
    def __init__(self):
        self.labels = []
        self.centers = []

        # Color de cada capa
        self.colors = [
            [0, 255, 0],
            [255, 0, 255],
            [0, 0, 255],
            [255, 0, 0],
            [255, 255, 0],
            [0, 255, 255],
        ]
    
    def __call__(self, image):
        t0 = time.time()
       
        Z = np.float32(image.reshape((-1,3)))

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        # se dividirá la imagen en 4 grupo de colores (los más representativos)
        K = 4
        ret, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        self.labels = labels
        self.centers = centers
            
        t = time.time()
        print(self.__class__.__name__,'time =', t-t0)

    def draw(self, image):
        # Generar una nueva imagen donde
        # cada grupo esté representado por un color distinto
        seg_image = image.copy()
        labels_img = self.labels.reshape(image.shape[:-1])
        for i in range(len(self.centers)):
            mask = labels_img == i
            seg_image[mask, :] = self.colors[i]
        return seg_image


if __name__ == "__main__":
    img = cv2.imread('objetos.jpg')
    Z = np.float32(img.reshape((-1,3)))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # se dividirá la imagen en 4 grupo de colores (los más representativos)
    K = 4
    ret, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Color de cada capa
    colors = [
        [0, 255, 0],
        [255, 0, 255],
        [0, 0, 255],
        [255, 0, 0],
        [255, 255, 0],
        [0, 255, 255],
    ]

    # Generar una nueva imagen donde
    # cada grupo esté representado por un color distinto
    seg_image = img.copy()
    labels_img = labels.reshape(img.shape[:-1])
    for i in range(len(centers)):
        mask = labels_img == i
        seg_image[mask, :] = colors[i]

    cv2.imwrite('segmentacion_output.jpg', seg_image)

