# Ejemplos de clase

En esta práctica continuaremos explorando técnicas de visión por computadora.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Detector de bordes
Comenzaremos por explorar el archivo bordes.py

__NOTA__: No es necesario entrar en el detalle de la clase armada en el archivo, pero si en el código dentro del bloque __main__.

Explorar como la imagen es transformada cuando pasa por las etapas del detector. Observar los archivos:
- contornos.jpg
- bordes_output.jpg


Observar las imágenes de salida con diferentes imágenes de entrada.


### 2 - Parámetros configurables
Los parámetros de sensibilidad del detector de bordes del algoritmo "Canny" se encuentran en está línea de código:
```python
edged = cv2.Canny(gray, 50, 400) 
```

- El primer número representa el filtro inferior (threshold) de detección
- El segundo número representa el filtro superior (threshold) de detección

Analice que sucede si variamos los valores establecidos en el ejemplo.


### 3 - Ensayo punta a punta del detector
Abrir el archivo de configuración ".env" y modificar el tipo detector a emplear:
```
TIPO_DETECTOR=bordes
```

Lanzar la aplicación (si es que no está lanzada) de visión:
```
python3 vision.py
```

Observar en la aplicación de "camera capture" como se comporta este filtro (debe configurar el tipo de filtro deseado a observar).

