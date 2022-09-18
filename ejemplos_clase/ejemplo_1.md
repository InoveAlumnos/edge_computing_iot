# Ejemplos de clase

### 1 - Preparar el entorno de trabajo

En esta práctica exploraremos crear crear un stream de datos de una cámara utilizando el celular

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Conectarse por ssh desde una terminal del host:
```
$ ssh inove@<ip_dispositivo>
```

Crear la carpeta "clase_7" para trabajar sobre los ejemplos de esta clase:
```sh
$ mkdir clase_7
```

Ingresar a la carpeta creada y clonar la carpeta del repositorio de esta clase:
```sh
$ cd clase_7
$ git https://github.com/InoveAlumnos/edge_computing_iot
$ cd edge_computing_iot
```

### 2 - Descargar el repositorioes de cámaras para el curso
Comencemos por descargar el repositorio que utilizaremos para conectar el celular con MQTT generando un stream de datos de video, y el sistema de captura de video que utilizaremos para ensayar distintos algoritmos.

Dentro de esta carpeta de clase_7, clonar el repositorio de prometheus:
```sh
$ git clone https://github.com/InoveAlumnos/camera_iot
```

Ingresar a la carpeta del repositorio descargado y lanzar el docker-compose:
```sh
$ docker-compose build
$ docker-compose up
```

El sistema lanzará dos aplicaciones
- Camera stream: la cual genera los datos de camara
- Camera capture: la cual captura y permite visualizar los datos de la cámara


### 3 - Camera stream
Para comenzar a generador datos de cámara (stream de video) debemos conectarnos a esta aplicación con un dispositivo que posea una cámara (puede ser una notebook o un celular).

Comenzar ensayando primero desde la notebook / PC con cámara ingresando a la URL:
```
https://<ip_VM>:5020
```

__IMPORTANTE__: No olvidarse de anteponer el "https" antes de la IP. Esta aplicación utiliza la cámara y por lo tanto necesita se ejecutada en HTTPS con consentimiento del usuario.

Al lanzar la app podrá ver unos botones para elegir:
- La cámara a utilizar
- El modo (cámara frontal o de atras)
- Comenzar (play) o dentener (pause) el stream.

Esta aplicación ni bien comience a funcionar y enviar datos se publicarán en MQTT al tópico:
```
"sensores/camara/raw"
```

Puede utilizar mosquitto_sub o mosqutto Explorer para verificar el correcto funcionamiento de MQTT.


### 4 - Camera capture desde la PC
Para comenzar a visualizar los datos de cámara (stream de video) debemos conectarnos a la aplicación "camera captura" desde nuestra PC.

Ingresando a la URL:
```
http://<ip_VM>:5021
```

__IMPORTANTE__: En este caso no debe colocar "https" dado que esta app no accede al stream de video utilizando los sensores, sino que recibe los datos por MQTT.

Esta app está escuchando diferentes tópicos MQTT que hiremos detallando en otros ejemplos:
- sensores/camara/raw
- sensores/camara/detecciones

En este caso que aún solo estamos utilizando "camera stream" debe dejar el selector de video en "raw" para recibir la transmisión de video.

Las imagenes que se reflejan en esta aplicación se actualizan cada 2 segundos.


### 5 - Camera stream desde el celular
- Primero debe desconectar su PC de la aplicación de "camara stream" para que no haya colisión de stream de video.
- En su celular ingrese a la siguiente URL:
```
http://<ip_VM>:5021
```

Realizar una demostración de como funciona la cámara frontal y de atras, siempre mostrando los datos de video que llegan a "camera capture".
- Lance el stream de video ni bien enciende la app en el celular, mostrar como las capturas de ese video se reflejan en "camera captura".
- Repita el procedimiento pero cambie a cámara de atras tocando el botón verde antes de lanzar el stream de video (debe actualizar la página para que vuelva a aparecer el botón verde).