import qrcode
import os
import time

os.system('cls & title "QR Code Generator | discord.gg/moonlygg"')

# Función para limpiar la consola
def limpiar_consola():
    """Limpia la consola en función del sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

# Función para generar el código QR
def generar_codigo_qr(data, carpeta_salida, imagen_nombre="codigo_qr.png", box_size=10, border=4):
    """Genera un código QR y lo guarda como imagen en la carpeta especificada."""
    # Crear la carpeta con la fecha y hora si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Crear el objeto QR
    qr = qrcode.QRCode(
        version=1,  # Tamaño del QR (1 es el más pequeño)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Corrección de errores
        box_size=box_size,  # Tamaño de cada cuadro
        border=border,  # Tamaño del borde
    )
    qr.add_data(data)  # Agregar los datos (URL, texto, correo, etc.)
    qr.make(fit=True)  # Ajustar el tamaño

    # Crear una imagen del código QR
    imagen = qr.make_image(fill='black', back_color='white')

    # Guardar la imagen en la carpeta 'output' dentro de la carpeta con la hora
    archivo_imagen = f"{carpeta_salida}/{imagen_nombre}"
    imagen.save(archivo_imagen)
    print(f"\n¡El código QR ha sido generado y guardado como '{archivo_imagen}'!")

# Función para la interfaz de usuario
def interfaz_usuario():
    """Interfaz de usuario para ingresar datos y generar el código QR."""
    print("¡Bienvenido al Generador de Códigos QR!\n")
    
    print("¿Qué tipo de código QR deseas generar?")
    print("1. URL")
    print("2. Correo electrónico")
    print("3. vCard (contacto)")
    print("4. Texto personalizado")
    
    opcion = input("Selecciona el tipo de QR (1/2/3/4): ")
    
    if opcion == "1":
        data = input("Por favor, ingresa la URL para generar el código QR:\n")
        imagen_nombre = "codigo_qr_url.png"
    elif opcion == "2":
        data = input("Por favor, ingresa la dirección de correo electrónico:\n")
        imagen_nombre = "codigo_qr_email.png"
    elif opcion == "3":
        nombre = input("Por favor, ingresa el nombre del contacto:\n")
        telefono = input("Por favor, ingresa el número de teléfono del contacto:\n")
        correo = input("Por favor, ingresa el correo electrónico del contacto:\n")
        data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{nombre}\nTEL:{telefono}\nEMAIL:{correo}\nEND:VCARD"
        imagen_nombre = "codigo_qr_vcard.png"
    elif opcion == "4":
        data = input("Por favor, ingresa el texto personalizado para generar el código QR:\n")
        imagen_nombre = "codigo_qr_texto.png"
    else:
        print("Opción no válida. Saliendo del programa.")
        return
    
    # Obtener la fecha y hora actual para crear una carpeta única
    current_time = time.strftime("%Y-%m-%d %H-%M-%S")
    carpeta_salida = f"output/{current_time}"

    # Llamar a la función para generar el código QR
    generar_codigo_qr(data, carpeta_salida, imagen_nombre)  # Generar el código QR

    # Regresar al menú principal después de generar el QR
    input("\nPresiona Enter para regresar al menú principal...")
    limpiar_consola()  # Limpiar la consola antes de regresar al menú principal

# Función principal que ejecuta el programa
def main():
    """Función principal que ejecuta el programa."""
    while True:
        try:
            limpiar_consola()  # Limpiar la consola al inicio del programa
            interfaz_usuario()
        except KeyboardInterrupt:
            print("\nPrograma detenido. ¡Adiós!")
            break

if __name__ == "__main__":
    main()
