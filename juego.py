#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo principal: orquesta la ejecución del juego.
"""
#Lo primero que hacemos es importar las librerias y los datos de nuestros demás archivos .py
from clases import *
from historia import Historia
from fun_auxiliares import *
from termcolor import *
from pyfiglet import *
import pygame
import time

#Luego definimos nuestra función principal, que será la que haga inicialice el juego.
def main():
    ancho = ancho_terminal()
    limpiar_pantalla()
    Sonido.reproducir("Ambient type beat 2025.mp3", loop=True)

    print("\n")
    Escena("El enigma de la estridencia", formato="bloody",color="red", velocidad=0 )
    print("\n" )

    time.sleep(3)

    Escena("Bienvenido al juego", formato="gothic", velocidad=0) 
    time.sleep(2)
    Escena("¿Estas listo para vivir", formato="gothic", velocidad=0)
    time.sleep(2)
    Escena("esta experiencia de terror", formato="gothic", velocidad=0)
    
    time.sleep(1)

    nombre = input("Ingresa tu nombre: ")
    player = Player(nombre)  # Se crea una única vez
 
    while True:
        confirmar1 =input("\n¿Estás seguro de querer adentrarte en esta pesadilla? (sí/no): ").strip().lower()
        confirmar=normalizar_entrada(confirmar1)

        if confirmar == "si":
            break
        elif confirmar == "no":
            print("Sabia decisión... Tal vez no estabas listo para esto.")
            return  # Sale del juego si el jugador no quiere continuar
        else:
            print("Responde solo 'sí' o 'no'.")

#En esta parte de la función, se llama a la clase historia, que se encuentra en nuestro archivo historia.py, para que empiece a surgir la narrativa de la historia, junto con las decisiones del usuario.
    
    limpiar_pantalla()

    Sonido.reproducir("Sonido del Mar.mp3", volumen=0.08, loop=True)

    historia = Historia()
    escenario_actual = "Reiniciar"

    while True:
        escenario_actual = historia.mostrar_escenario(escenario_actual)
        if escenario_actual == "Terminar":
            print("Las mentes débiles huyen de sus miedos")
            break

if __name__ == "__main__":
    main()
