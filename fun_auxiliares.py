from unidecode import *
import os
from termcolor import *
from pyfiglet import *

def texto_grande(texto, color="red"):
    ancho = ancho_terminal()
    mensaje_grande = figlet_format(texto, width=ancho)  # Convertir el texto en grande
    texto_centrado = "\n".join([centrar_texto(linea) for linea in mensaje_grande.splitlines()])
    mensaje_coloreado = colored(texto_centrado, color)  # Aplicar color al texto
    print(mensaje_coloreado)

# Función para normalizar cualquier entrada del usuario
def normalizar_entrada(entrada):
    # Convertir a minúsculas y eliminar acentos
    return unidecode(entrada.strip().lower())

def centrar_texto(texto):
    ancho = ancho_terminal()  # Obtener el ancho de la terminal
    return texto.center(ancho) 

def ancho_terminal():
    return os.get_terminal_size().columns

