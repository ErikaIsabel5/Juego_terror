#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Este archivo .py contiene todas las narrativas y decisiones que el usuario puede elegir, así como los diferentes caminos.

#Aquí, la hisotira va a estar contenida dentro de una clase, en esa clase, cada una de las opciones que el usuario elige, junto con su narrativa, va a estar guardada en un diccionario, esto con la finalidad de mejorar y acomodar las decisiones obtenidas.
class Historia:
    def __init__(self):
        self.escenarios = {
            "inicio": {
                "texto": [
                    "Despiertas sin saber dónde te encuentras.",
                    "No puedes ver nada a tu alrededor, pero escuchas las olas del mar a lo lejos, lo que te hace suponer que debes estar en algún lugar cercano al mar.",
                    "Intentas parpadear para que tus ojos se adapten a la oscuridad, pero no tienes éxito.",
                    "Poco a poco, el miedo empieza a invadirte..."
                ],
                "opciones": {
                    "1": "dormir",
                    "2": "sentarse_cama",
                    "3": "gritar",
                    "4": "salir"
                }
            },
            "dormir": {
                "texto": [
                    "Decides dormir un poco más...",
                    "Pero de repente algo toca tu cara."
                ],
                "opciones": {
                    "1": "inicio"
                }
            },
            "sentarse_cama": {
                "texto": [
                    "Decides levantarte con cierto temor, sintiendo cómo el miedo aumenta a cada instante.",
                    "Te sientas en la orilla de la cama, notando una extraña sensación indescriptible."
                ],
                "opciones": {
                    "1": "levantarse",
                    "2": "mover_manos",
                    "3": "hablar",
                    "4": "gritar",
                    "5": "inspeccionarse",
                    "6": "salir"
                }
            },
            "gritar": {
                "texto": [
                    "Has elegido gritar.",
                    "Tu voz resuena en la oscuridad, pero solo logras hacer que el silencio se vuelva aún más aterrador.",
                    "Percibes un pequeño sonido además de las olas del mar, pero no sabes si es tu imaginación o algo real.",
                    "Tu piel se eriza y sientes que algo te observa. Empiezas a hiperventilar con más fuerza."
                ],
                "opciones": {
                    "1": "gritar_mas",
                    "2": "levantarse",
                    "3": "quedarse_quieto"
                }
            },
            "gritar_mas": {
                "texto": [
                    "Vuelves a gritar con desesperación...",
                    "De repente, escuchas pasos corriendo en tu dirección.",
                    "Antes de que puedas hacer algo, unos pasos gigantescos resuenan en la habitación, algo se posiciona frente a ti, con una agitada y fuerte respiración.",
                    "Aún no puedes ver nada, las lágrimas de miedo comienzan a brotar de tus ojos y entonces esa cosa te habla:",
                    '"Parece que necesito callarte yo mismo", dice con una voz tan rasposa y ronca que tiemblas sin control.',
                    "Intentas volver a gritar, pero entonces, un golpe resuena en la habitación.",
                    "No puedes sentir nada, como si toda sensación se hubiera ido.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "reiniciar"
                }
            },
            "quedarse_quieto": {
                "texto": [
                    "Decides quedarte completamente quieto, pero la sensación de que algo te observa es insoportable.",
                    "No puedes soportarlo más. De repente, te levantas corriendo, sin saber hacia dónde vas.",
                    "Chocas contra lo que parece ser una pared, el ruido resuena en todo lugar.",
                    "Te alteras más al escuchar en medio del escándalo unos pasos acercarse a ti, lentamente, como si te estuvieran acechando.",
                    "Con total pánico, te mueves a lo largo de la pared, chocando contra todo a tu paso.",
                    "Llegas a una puerta, resuena tan fuerte que saltas del miedo.",
                    "Sin pensarlo más, corres al otro lado de la puerta sin detenerte.",
                    "Chocas contra lo que parece ser una valla. Al llegarte solo a la cintura, sin poder evitarlo, te precipitas hacia el vacío.",
                    "Sientes el aire recorrer tu cuerpo por unos segundos mientras sigues cayendo.",
                    "De pronto, un dolor agudo te invade en todo tu cuerpo.",
                    "El sonido de algo romperse resuena por todo el lugar.",
                    "Sin poder hablar ni moverte, poco a poco dejas de sentir dolor y miedo.",
                    "Te has roto el cráneo y los huesos. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "reiniciar"
                }
            },
            "levantarse": {
                "texto": [
                    "Te levantas completamente de la cama. Estás desorientado porque no ves nada.",
                    "Aun así, decides comenzar a moverte lentamente de frente.",
                    "De pronto te golpeas contra lo que parece ser una pared. El ruido te asusta.",
                    "Hiperventilando, te quedas parado."
                ],
                "opciones": {
                    "1": "detenerte",
                    "2": "seguir_moviendo"
                }
            },
            "detenerte": {
                "texto": [
                    "Te quedas parado sin moverte. Debido al golpe, decides escuchar a tu alrededor atentamente por unos segundos.",
                    "Al no percibir nada, continúas moviéndote, esta vez a la derecha, dejando tu mano sobre la pared."
                ],
                "opciones": {
                    "1": "seguir_moviendo"
                }
            },
            "seguir_moviendo": {
                "texto": [
                    "Inhalas y exhalas para tranquilizarte.",
                    "Con la mano en la pared, continúas moviéndote hacia la derecha."
                ],
                "opciones": {
                    "1": "explorar_habitacion"
                }
            }
        }

#Cuando los diccionarios de cada decisión se hayan terminado, se procede con la función mostrar_escenario, la cual será la responsable de tomar la elección que el usuario le indique para proseguir con la historia, mostrando los escenarios adecuados y siguiendo con la historia de acuerdo a las decisiones
    def mostrar_escenario(self, nombre_escenario):
        escenario = self.escenarios.get(nombre_escenario)
        if escenario:
            print("\n" + "=" * 50)
            for linea in escenario["texto"]:
                print(linea)
            print("=" * 50 + "\n")

            opciones_legibles = {key: opcion.replace("_", " ") for key, opcion in escenario.get("opciones", {}).items()}

            for key, opcion in opciones_legibles.items():
                print(f"{key}. {opcion.capitalize()}")  

            eleccion = input("\n¿Qué haces? (Ingresa un número): ")
            return escenario["opciones"].get(eleccion, "inicio")  
        else:
            return "inicio"
