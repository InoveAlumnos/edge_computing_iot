# Ejemplos de clase

En esta práctica continuaremos explorando técnicas de visión por computadora.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Detector de colores
Comenzaremos por explorar el archivo segmentacion.py

__NOTA__: No es necesario entrar en el detalle de la clase armada en el archivo, pero si en el código dentro del bloque __main__.

Explorar como la imagen es transformada cuando pasa por las etapas del detector. Observar los archivos:
- segmentacion_output.jpg


Observar las imágenes de salida con diferentes imágenes de entrada.


### 2 - Parámetros configurables
Los parámetros de configuración del segmentador por colores del algoritmo "kmeans" se encuentran en está línea de código:
```python
K = 4
```

- K representa la cantidad de segmento de colores a buscar. En este caso, el sistema busca los 4 colores más representativos de la imagen y los agrupa.

Analice que sucede si modifica este valor (máximo k=6)


### 3 - Ensayo punta a punta del detector
Abrir el archivo de configuración ".env" y modificar el tipo detector a emplear:
```
TIPO_DETECTOR=colores
```

Lanzar la aplicación (si es que no está lanzada) de visión:
```
python3 vision.py
```

Observar en la aplicación de "camera capture" como se comporta este filtro (debe configurar el tipo de filtro deseado a observar).

