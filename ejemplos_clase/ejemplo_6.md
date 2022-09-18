# Ejemplos de clase

En esta práctica continuaremos explorando técnicas de visión por computadora.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Detector de rostros
Comenzaremos por explorar el archivo face.py

__NOTA__: No es necesario entrar en el detalle de la clase armada en el archivo, pero si en el código dentro del bloque __main__.

Explorar como la imagen es transformada cuando pasa por las etapas del detector. Observar los archivos:
- face_output.jpg


### 2 - Parámetros configurables
Los parámetros de sensibilidad del detector de rostros utilizando un algoritmo clasificador está línea de código:
```python
minNeighbors=8,  # threashold (más alto es más exigente)
minSize=(30, 30),  # tamaño de la cara minima
```

- minNeighbors representa el nivel de filtrado del sistema. Cuanto más alto más exigente será el algoritmo a la hora de determinar un rostro.
- minSize representa el tamaño mínimo esperado por un rostro en la imagen de entrada.

Analice que sucede si modifica el valor de minNeighbors a 4


### 3 - Ensayo punta a punta del detector
Abrir el archivo de configuración ".env" y modificar el tipo detector a emplear:
```
TIPO_DETECTOR=rostros
```

Lanzar la aplicación (si es que no está lanzada) de visión:
```
python3 vision.py
```

Observar en la aplicación de "camera capture" como se comporta este filtro (debe configurar el tipo de filtro deseado a observar).

