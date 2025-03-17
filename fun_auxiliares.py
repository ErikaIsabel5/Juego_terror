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



def sonido_mar():
    sonido_mar=pygame.mixer.Sound("Sonido del Mar.mp3")
    sonido_mar.set_volume(0.08)
    sonido_mar.play(-1)

def sonido_fondo():
    sonido_fondo=pygame.mixer.Sound("Ambient type beat 2025.mp3")
    sonido_fondo.set_volume(0.1)
    sonido_fondo.play(-1)



#Esta función va a ayudar para generar un texto más grande en la terminal, que sea visual, que le agregue además un color, por defecto color rojo, y que mantenga al texto centrado.
def texto_bloody(texto, color="red"):
    ancho = ancho_terminal()
    mensaje_grande = figlet_format(texto, font="bloody", width=ancho)
    texto_centrado = "\n".join([centrar_texto(linea) for linea in mensaje_grande.splitlines()])
    mensaje_coloreado = colored(texto_centrado, color) 
    print(mensaje_coloreado)

def texto_mediano(texto):
    ancho = ancho_terminal()
    mensaje_mediano = figlet_format(texto, font="gothic", width=ancho)
    texto_centrado = "\n".join([centrar_texto(linea) for linea in mensaje_mediano.splitlines()])
    print(texto_centrado)


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
    os.system('cls' if os.name == 'nt' else 'clear')
