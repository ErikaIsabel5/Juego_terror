#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Archivo de clases para el juego de terror.
Contiene las definiciones de clases como Player y Game.
"""

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



