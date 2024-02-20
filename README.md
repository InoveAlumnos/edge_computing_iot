![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---

# Edge computing! [Python]
Instalar openCV
```sh
$ sudo apt-get update
$ sudo apt-get install -y libopencv-dev python3-opencv
```

Instalar tesseract
```sh
$ sudo apt-get update
$ sudo apt-get install -y tesseract-ocr
$ sudo apt-get install -y tesseract-ocr-spa
```

Instalar las dependencias de python para esta clase:
```sh
$ python3 -m pip install pillow
$ python3 -m pip install pytesseract
```

Habilitar websockets en mosquitto
```sh
$ sudo touch /etc/mosquitto/conf.d/mosquitto.conf
echo -e "allow_anonymous true\nlistener 1883 0.0.0.0\nallow_anonymous true\nlistener 9001\nprotocol websockets" | sudo tee /etc/mosquitto/conf.d/mosquitto.conf
$ sudo service mosquitto restart
```

# En este repositorio encontrarán los siguientes archivos:

__Ejemplos que el profesor mostrará en clase__\
ejemplos_clase/


# Simuladores
De aquí en más usted podrá elegir que simuladores utilizar para las prácticas o para enviar los mensajes MQTT.

Recomendamos utilizar el simulador "drone_iot" con de celular para utilizar los sensores (GPS, incerciales) y actuadores (luz y motores) del celular, a fin de tener una experiencia más "realista".

En caso que usted no desee usar o no pueda usar el simulador "drone_iot" junto a su celular, recomendamos utilizar el simulador "drone_mock_iot".

__IMPORTANTE__: Recuerde que estos simuladores los debe lanzar en su VM (VirtualMachine) que es donde se encuentran instaladas las dependencias y el MQTT broker.

Si necesita clonar el repositorio de "drone_iot" utilce:
```sh
$ git clone https://github.com/InoveAlumnos/drone_iot
```

Si necesita clonar el repositorio de "drone_mock_iot" utilce:
```sh
$ git clone https://github.com/InoveAlumnos/drone_mock_iot
```

En el campus podrá encontrar la lista de tópicos que soportan estos simuladores.

# Consultas
alumnos@inove.com.ar

