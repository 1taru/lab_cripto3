import os
import re

def download_rockyou():
    if not os.path.exists("rockyou.txt"):
        wget("https://github.com/brannondorsey/naive-hashcat/raw/master/rockyou.txt")

def create_modified_dictionary():
    # Abre el diccionario original
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        # Crea un diccionario vacío
        modified_dictionary = []

        # Itera sobre cada contraseña en el diccionario original
        line_count = 0
        for line in f:
            # Elimina espacios en blanco al principio y al final
            line = line.strip()
            
            # Verifica si la contraseña no está vacía y si el primer carácter es una letra
            if line and re.match("^[a-zA-Z]", line[0]):
                # Convierte la primera letra a mayúscula y agrega "0" al final
                modified_password = line[0].upper() + line[1:] + "0"

                # Agrega la contraseña modificada a la lista
                modified_dictionary.append(modified_password)

                # Incrementa el contador de líneas
                line_count += 1

    # Crea el directorio de destino
    if not os.path.exists("destino"):
        os.mkdir("destino")

    # Abre el diccionario modificado
    with open("destino/rockyou_mod.dic", "w", encoding="utf-8") as f2:
        for password in modified_dictionary:
            f2.write(password + "\n")

    # Imprime el número de líneas del diccionario modificado
    print("El diccionario modificado tiene {} líneas.".format(line_count))

def main():
    # Descarga el diccionario original
    download_rockyou()

    # Crea el diccionario modificado
    try:
        create_modified_dictionary()
    except UnicodeDecodeError:
        print("El archivo 'rockyou.txt' puede estar codificado en una codificación diferente a UTF-8. Intenta convertirlo a UTF-8 antes de ejecutar el script nuevamente.")

if __name__ == "__main__":
    main()
