import os
import hashlib
import re

def download_rockyou():
    if not os.path.exists("rockyou.txt"):
        wget("https://github.com/brannondorsey/naive-hashcat/raw/master/rockyou.txt")

def create_modified_dictionary():
    # Abre el diccionario original
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        # Crea un diccionario vacío
        modified_dictionary = {}

        # Itera sobre cada contraseña en el diccionario original
        line_count = 0
        for line in f:
            # Verifica si el primer caracter es una letra
            if re.match("^[a-zA-Z]", line[0]):
                # Crea un hash de la contraseña
                password_hash = hashlib.sha256(line.encode("utf-8")).hexdigest()

                # Agrega el hash a la contraseña modificada
                modified_dictionary[password_hash] = line

                # Incrementa el contador de líneas
                line_count += 1

    # Crea el directorio de destino
    if not os.path.exists("destino"):
        os.mkdir("destino")

    # Abre el diccionario modificado
    with open("destino/rockyou_mod.dic", "w", encoding="utf-8") as f2:
        for password in modified_dictionary.keys():
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
