#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Este archivo contiene las definiciones de clases diferentes a la clase Historia, las clases encontradas aquí serán utilizadas principalmente para describir objetos, el jugador o NPC que se puedan implementar.

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



