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

#Luego definimos nuestra función principal, que será la que haga inicialice el juego.
def main():
    ancho = ancho_terminal()

    print("\n" + "=" * ancho)
    texto_grande("Bienvenido al juego de terror, donde probaremos tus métodos de supervivencia en una situación extrema y desconocida.")
    texto_grande("¿Podras sobrevivir?")
    print("=" * ancho + "\n" )
    
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
    historia = Historia()
    escenario_actual = "inicio"

    while True:
        escenario_actual = historia.mostrar_escenario(escenario_actual)
        if escenario_actual == "salir":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
