# Ejemplos de clase

En esta práctica continuaremos explorando técnicas de visión por computadora.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Detector de texto (OCR)
Comenzaremos por explorar el archivo ocr.py

__NOTA__: No es necesario entrar en el detalle de la clase armada en el archivo, pero si en el código dentro del bloque __main__.

Explorar como la imagen es transformada cuando pasa por las etapas del detector. Observar los archivos:
- texto_output.jpg


### 2 - Ensayo punta a punta del detector
Abrir el archivo de configuración ".env" y modificar el tipo detector a emplear:
```
TIPO_DETECTOR=texto
```

Lanzar la aplicación (si es que no está lanzada) de visión:
```
python3 vision.py
```

Observar en la aplicación de "camera capture" como se comporta este filtro (debe configurar el tipo de filtro deseado a observar).

