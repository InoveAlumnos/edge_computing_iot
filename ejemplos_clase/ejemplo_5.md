# Ejemplos de clase

En esta práctica continuaremos explorando técnicas de visión por computadora.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Detector de objectos
Antes de comenzar, debemos descargar el modelo de IA de detección de objetos "yolo" dentro de la misma carpeta "ejemplos_clase":
```sh
$ wget https://pjreddie.com/media/files/yolov3.weights
```
```sh
$ wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
```

Comenzaremos por explorar el archivo objectos.py

__NOTA__: No es necesario entrar en el detalle de la clase armada en el archivo, pero si en el código dentro del bloque __main__.

Explorar como la imagen es transformada cuando pasa por las etapas del detector. Observar los archivos:
- detection_output.jpg


Observar las imágenes de salida con diferentes imágenes de entrada.


### 2 - Datos que retorna el sistema
Observar el dato que retorna el sistema en la variable "detections".
- Por un lado verá la coordenada en píxeles de la ubicación del objeto en la imagen (x, y, w, h).
- Por otro lado verá el tipo de objeto detectado.
- Por otro lado verá la confianza que tiene el detector sobre cada detección puntual.

Estos datos pueden utilizarse para postprocesarse y crear distintas aplicaciones como:
- Dectar la presencia de un objeto (una persona, una pieza, un producto)
- Contar candiad de elementos en una imagen o video.
- Determinar si un objeto está en una zona no permitida o peligrosa.
- Determinar si una persona tiene elementos de seguridad puestos.
- Determinar si una persona está usando un objeto no permitido (ej: el celular mientras maneja).


### 3 - Ensayo punta a punta del detector
Abrir el archivo de configuración ".env" y modificar el tipo detector a emplear:
```
TIPO_DETECTOR=objetos
```

Lanzar la aplicación (si es que no está lanzada) de visión:
```
python3 vision.py
```

Observar en la aplicación de "camera capture" como se comporta este filtro (debe configurar el tipo de filtro deseado a observar).

