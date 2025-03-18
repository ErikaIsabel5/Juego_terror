#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Este archivo contiene las definiciones de clases diferentes a la clase Historia.

from pyfiglet import *
from termcolor import *
import time
import sys
import os
from fun_auxiliares import *
import pygame


#Definimos una clase la cual va a ser la encargada de colocar el sonido en el juego, de esta forma, cualquier sonido ingresado, puede colocarse con esta clase.
class Sonido:
    pygame.mixer.init()  

    def reproducir(archivo, volumen=0.1, loop=False):
        sonido = pygame.mixer.Sound(archivo)
        sonido.set_volume(volumen)
        if loop:
            sonido.play(-1)  
        else:
            sonido.play()

    def detener_todos():
        pygame.mixer.stop()


#Definimos ahora la clase escena, la cual va a ser la encargada de darle formato a una línea de texto o del diccionario en una parte de la narrativa, dandole formato, estilo, velocidad, ingresando sonido, etc.
class Escena:
    def __init__(self, texto, formato=None, velocidad=0.3, color=None, sonido=None, limpiar=False):
        self.texto = texto
        self.formato = formato 
        self.velocidad = velocidad
        self.color = color  
        self.sonido = sonido
        self.limpiar = limpiar

        self.mostrar() 

    def mostrar(self):
        if self.limpiar:
            limpiar_pantalla()

        if self.sonido:
            from sonido import Sonido  
            Sonido.reproducir(self.sonido, volumen=0.3)

        if self.formato:
            texto_formateado = figlet_format(self.texto, font=self.formato, width=ancho_terminal())
        else:
            texto_formateado = self.texto  

        if self.color:
            texto_final = colored(texto_formateado, self.color)
        else:
            texto_final = texto_formateado  

        texto_centrado = "\n".join([centrar_texto(linea) for linea in texto_final.splitlines()])

        if self.velocidad == 0:
            print(texto_centrado)
        else:
            for linea in texto_centrado.splitlines():
                for letra in linea:
                    sys.stdout.write(letra)
                    sys.stdout.flush()
                    time.sleep(self.velocidad)
                print()


#Esta clase implemente los atributos que puede llegar a tener el jugador, primero sus atributos iniciales y después funciones que puedan subir esos atributos, como aún no se define alguna otra clase que use los atributos, de momento el jugador es el unico que tiene éstos y se colocaron dentro de su clase.

class Player:
    def __init__(self, name):
        self.name = name
        self.hambre = 50     # Valor entre 0 y 100.
        self.sed = 50        # Valor entre 0 y 100.
        self.energia = 50    # Valor entre 0 y 100.

    def comer(self):
        incremento = 20
        self.hambre = min(100, self.hambre + incremento)
        print("\nDecides comer algo que encuentras en la cocina improvisada. Tu hambre aumenta.")
        print(f"[Nivel de hambre: {self.hambre}/100]")

    def beber(self):
        incremento = 20
        self.sed = min(100, self.sed + incremento)
        print("\nBuscas agua en la despensa y te hidratas. Tu sed disminuye.")
        print(f"[Nivel de sed: {self.sed}/100]")

    def dormir(self):
        incremento = 30
        self.energia = min(100, self.energia + incremento)
        print("\nTe recuestas en un viejo sofá y logras descansar. Tu energía aumenta.")
        print(f"[Nivel de energía: {self.energia}/100]")



