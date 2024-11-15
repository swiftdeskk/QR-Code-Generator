# QR Code Generator 🔑📱

Este programa permite generar códigos QR de manera sencilla. Puedes ingresar un enlace o un texto, y automáticamente se creará un código QR. Además, los códigos QR generados se guardan en una carpeta con la fecha y hora de la ejecución, asegurando que puedas organizar y acceder fácilmente a todos tus códigos generados. 🎉

## Características ✨

- Genera códigos QR a partir de un texto o enlace 🔗.
- Los códigos QR se guardan automáticamente en una carpeta de salida con la hora y fecha exacta de generación 🗓️.
- El tamaño del código QR es preestablecido para una mejor visualización 📏.
- Los códigos QR se almacenan en imágenes PNG 🖼️.
- La aplicación limpia la consola antes de cada nueva ejecución para mayor comodidad 🧹.

## Cómo usarlo 🚀

1. **Ejecuta el programa**: Ejecuta el script de Python.
2. **Ingresa el enlace o texto**: Se te pedirá que ingreses el enlace o texto que deseas convertir en un código QR.
3. **Generación y guardado**: El código QR se generará y guardará automáticamente en la carpeta `output` con un nombre basado en la fecha y hora exacta de la ejecución.
4. **Ubicación de los archivos**: Los códigos QR generados estarán dentro de una subcarpeta con la hora y fecha de la ejecución para su organización.

## Requisitos 📋

Para ejecutar este programa, necesitas tener instalado Python 3 y la librería `qrcode`. Puedes instalarla utilizando pip:

```bash
pip install qrcode[pil]
```

## Ejemplo de uso 💻

Al ejecutar el programa, te pedirá que ingreses un texto o enlace. Por ejemplo:
```bash
Ingresa el enlace o texto para generar el QR: https://www.ejemplo.com
```
Luego, el programa generará un archivo PNG con el código QR y lo guardará en la carpeta `output`.

## Licencia 📝

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🤝 **Contacto**
Creado con ❤️ por [SwiftDesk](https://github.com/swiftdeskk).  
Si tienes dudas o sugerencias, no dudes en escribirme.
