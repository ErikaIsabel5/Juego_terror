#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Este archivo, contiene funciones auxiliares que se van a usar a lo largo de los otros 3 archivos .py, las cuales pueden servir para modificar el juego visualmente o para auxiliar en algun punto a las demás funciones.

#Estas funciones son globales y se pueden llamar desde cualquiera de los otros 3 archivos .py

#Lo primero que hacemos es importar las librerias que se usarán para que funcionen correctamente
from unidecode import *
import os
from termcolor import *
from pyfiglet import *
import pygame
import time
import sys


# Esta función ayuda a que la entrada de los usuarios, cuando se les solicita una palabra, sea aceptada siempre que la palabra tenga las mismas letras, sin importar si son acentos, mayusculas, minusculas, etc, haciendo que la computadora las normalice para que quite las comas y las mayusculas y al final el resultado final sea sólo la palabra con minusculas.
def normalizar_entrada(entrada):
    # Convertir a minúsculas y eliminar acentos
    return unidecode(entrada.strip().lower())

#Esta función sirve para centrar el texto en la terminal, en este caso se usa la función ancho_terminal, para determinar el ancho de la terminal en cualquier computadora que se ejecute y en base a eso centrar el texto que se le indique.
def centrar_texto(texto):
    ancho = ancho_terminal()  
    return texto.center(ancho) 

def ancho_terminal():
    return os.get_terminal_size().columns

#Definimos una función para limpiar la pantalla en la terminal.

def limpiar_pantalla():
    if os.name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")
