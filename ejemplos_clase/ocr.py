# pip install pytesseract==0.3.10
# pip install opencv-python==4.4.0.44

# sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
# sudo apt-get update
# sudo apt-get install -y tesseract-ocr
# sudo apt-get install -y tesseract-ocr-spa

import time
import cv2
import pytesseract

class OCR():
    def __init__(self):
        self.results = None
    
    def __call__(self, image):
        t0 = time.time()
       
        # Pasar la imagen de BGR (openCV) a RGB
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Procesar la imagen
        #print(pytesseract.image_to_string(img_rgb, lang='spa'))
        self.results = pytesseract.image_to_data(img_rgb, lang='spa', output_type=pytesseract.Output.DICT)

        t = time.time()
        print(self.__class__.__name__,'time =', t-t0)

    def draw(self, image):
        # Dibujar todos los contornos en la imagen
        if self.results is not None:
            for i in range(len(self.results["text"])):
                x = self.results["left"][i]
                y = self.results["top"][i]
                w = self.results["width"][i]
                h = self.results["height"][i]
                text = self.results["text"][i]
                conf = self.results["conf"][i]

                if conf > 0:
                    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

        return image


if __name__ == "__main__":
    # Cargar una de las imagenes disponibles
    image = cv2.imread('texto_ticket.jpg')

    # Pasar la imagen de BGR (openCV) a RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Procesar la imagen
    #print(pytesseract.image_to_string(img_rgb, lang='spa'))
    results = pytesseract.image_to_data(img_rgb, lang='spa', output_type=pytesseract.Output.DICT)
    for i in range(len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        text = results["text"][i]
        conf = results["conf"][i]

        if conf > 0:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

    cv2.imwrite("texto_output.jpg", image)
