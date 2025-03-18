#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Este archivo .py contiene todas las narrativas y decisiones que el usuario puede elegir, así como los diferentes caminos.

from fun_auxiliares import *


#Aquí, la hisotira va a estar contenida dentro de una clase, en esa clase, cada una de las opciones que el usuario elige, junto con su narrativa, va a estar guardada en un diccionario, esto con la finalidad de mejorar y acomodar las decisiones obtenidas.
class Historia:
    def __init__(self):
        self.escenarios = {
            "Reiniciar": {
                "texto": [
                    "Despiertas sin saber dónde te encuentras.",
                    "No puedes ver nada a tu alrededor, pero escuchas las olas del mar a lo lejos, lo que te hace suponer que debes estar en algún lugar cercano al mar.",
                    "Intentas parpadear para que tus ojos se adapten a la oscuridad, pero no tienes éxito.",
                    "Poco a poco, el miedo empieza a invadirte..."
                ],
                "opciones": {
                    "1": "Dormir",
                    "2": "Sentarse_en_la_cama",
                    "3": "Gritar",
                    "4": "Terminar"
                }
            },
            "Dormir": {
                "texto": [
                    "Inhalas y exhalas tratando de tranquilizarte, decides que lo mejor es volver a dormir.",
                    "Cierras los ojos e intentas regresar a tu descando, pero entonces la sensación de estar siendo observado te persigue."
                ],
                "opciones": {
                    "1": "Sentarse_en_la_cama",
                    "2": "Gritar",
                    "3": "Quedarse_quieto"
                }
            },
            "Gritar": {
                "texto": [
                    "Tu voz resuena en la oscuridad, pero solo logras hacer que el silencio se vuelva aún más aterrador.",
                    "Percibes un pequeño sonido además de las olas del mar, pero no sabes si es tu imaginación o algo real.",
                    "Tu piel se eriza y sientes que algo te observa. Empiezas a hiperventilar con más fuerza."
                ],
                "opciones": {
                    "1": "Gritar_mas",
                    "2": "Levantarte",
                    "3": "Quedarse_quieto"
                }
            },
            "Gritar_mas": {
                "texto": [
                    "Vuelves a gritar con desesperación...",
                    "De repente, escuchas pasos corriendo en tu dirección.",
                    "Antes de que puedas hacer algo, unos pasos gigantescos resuenan en la habitación, algo se posiciona frente a ti, con una agitada y fuerte respiración.",
                    "Aún no puedes ver nada, las lágrimas de miedo comienzan a brotar de tus ojos y entonces esa cosa te habla:",
                    '"Parece que necesito callarte yo mismo", dice con una voz tan rasposa y ronca que tiemblas sin control.',
                    "Intentas volver a gritar, pero entonces, un golpe resuena en la habitación.",
                    "Tu mundo parece dar vueltas a tu alrededor, dejas de sentir cualquier cosa y de escuchar, poco a poco toda sensación se va, el miedo se va.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Quedarse_quieto": {
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
                    "1": "Reiniciar"
                }
            },
            "Sentarse_en_la_cama": {
                "texto": [
                    "Decides levantarte con cierto temor, sintiendo cómo el miedo aumenta a cada instante.",
                    "Te sientas en la orilla de la cama, notando una extraña sensación indescriptible."
                ],
                "opciones": {
                    "1": "Levantarte",
                    "2": "Mover_las_manos_a_tu_alrededor",
                    "3": "Hablar",
                    "4": "Gritar",
                }
            },
            "Hablar": {
                "texto": [
                    "¿Hola?",
                    "Esperas unos segundos a ver si alguien te responde, no logras escuchar nada a tu alrededor, sigues parpadeando, pero aún no puedes ver nada",
                    "Tu respiración se hace más fuerte, pero intentas no caer ante el miedo"
                ],
                "opciones": {
                    "1": "Levantarte",
                    "2": "Gritar",
                    "3": "Mover_las_manos_a_tu_alrededor"
                }
            },
            "Levantarte": {
                "texto": [
                    "Te levantas completamente de la cama. Estás desorientado porque no ves nada.",
                    "Aun así, decides comenzar a moverte lentamente de frente.",
                    "De pronto te golpeas contra lo que parece ser una pared. El ruido te asusta.",
                    "Hiperventilando, te quedas parado."
                ],
                "opciones": {
                    "1": "Detenerte",
                    "2": "Seguir_moviendote"
                }
            },
            "Detenerte": {
                "texto": [
                    "Te quedas parado sin moverte. Debido al golpe, decides escuchar a tu alrededor atentamente por unos segundos.",
                    "Al no percibir nada, continúas moviéndote, esta vez a la derecha, dejando tu mano sobre la pared."
                ],
                "opciones": {
                    "1": "Explorar_la_habitación",
                }
            },
            "seguir_moviendote": {
                "texto": [
                    "Inhalas y exhalas para tranquilizarte.",
                    "Con la mano en la pared, continúas moviéndote hacia la derecha."
                ],
                "opciones": {
                    "1": "Explorar_la_habitación"
                }
            },
            "Explorar_la_habitación": {
                "texto": [
                    "Caminas unos cuantos pasos más, entonces chocas contra algo duro, el golpe vuelve a resonar por toda la habitación",
                    "Mueves las manos alrededor del objeto, parece ser un armario, tiene 2 puertas con una llave en una de ellas, un poco más a la derecha hay una puerta con lo que parece un espejo, debajo de ésta hay 3 cajones",
                   "Un ruido afuera de la habitación te mantiene alerta, no sabes qué fue, pero comienzas a asustarte más",
                   "Miedo al 70%" 
                ],
                "opciones": {
                    "1": "Continuar_caminando_a_la_derecha",
                    "2": "Inspeccionar_el_armario"
                }
            },
            "Inspeccionar_el_armario": {
                "texto": [
                    "Tus manos, temblorosas, comienzan a buscar primero en los cajones en busca de algo que pueda ayudarte a observar a tu alrededor.",
                    "Sientes algunas cosas dentro de los cajones, no sabes qué son exactamente, parecen ser cables muy gruesos, ninguno parece ser una lámpara, además de que no puedes levantarlos, como si estuvieran pegados al cajón.",
                    "Pasos subiendo unas escaleras te alteran más, algo parece caminar lentamente hacia donde estás"
                    "Miedo al 80%"
                ],
                "opciones": {
                    "1": "Mantenerte_en_silencio",
                    "2": "Seguir_inspeccionando_el_armario"
                },
            },
            "Mantenerte_en_silencio": {
                "texto": [
                    "Mantienes la respiración, intentas quedarte completamente en silencio, no sabes que hay afuera, no sabes quién está en la casa, podría ser tu padre o tu madre, pero por alguna razón, tu miedo no te permite moverte",
                    "Los pasos dejan de escucharse de pronto, no sabes si la persona de afuera se ha ido, pero después de unos minutos dejas de escuchar cualquier sonido",
                    "Miedo al 70%"
                ],
                "opciones": {
                    "1": "Seguir_inspeccionando_el_armario",
                    "2": "Continuar_caminando_a_la_derecha"
                }
            },
            "Seguir_inspeccionando_el_armario": {
                "texto": [
                    "Con cautela vuelves a tocar el armario, esta vez encuentras la puerta de arriba de los cajones, pero te das cuenta que no tiene ninguna llave.",
                    "Mueves tus manos hasta encontrar las 2 puertas grandes del armario, recorres con manos temblorosas hasta encontrar la llave que se encuentra pegada",
                    "Intentas girarla, pero no se mueve, entonces, escuchas a alguien correr rápidamente a tu dirección",
                    "Miedo al 100%",
                    "Antes de que puedas hacer algo, unos pasos gigantescos resuenan en la habitación, algo se posiciona frente a ti, con una agitada y fuerte respiración."
                    "Que humano tan predecible",
                    "Dejame mostrarte, por qué la curiosidad mató al gato",
                    "Tu mundo parece dar vueltas a tu alrededor, dejas de sentir cualquier cosa y de escuchar, poco a poco toda sensación se va, el miedo se va.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Continuar_caminando_a_la_derecha": {
                "texto": [
                    "Sigues caminando hacia la derecha con la mano aún en la pared",
                    "Unos segundos después, con tu otra mano levantada, logras tocar algo, lo recorres y te das cuenta que es una puerta"
                ],
                "opciones":{
                    "1": "Salir_de_la_habitación",
                    "2": "Quedarse_en_la_habitación"
                }
            },
            "Quedarse_en_la_habitación":{
                "texto": [
                    "Recordando los pasos que escuchaste hace unos minutos, decides quedarte en la habitación",
                    "Tu miedo aumenta, cada vez inhalas con más fuerza, continuas recorriendo la pared.",
                    "De pronto, tus piernas chocan contra algo y caes, es la cama, has vuelto al lugar donde despertaste."
                ],
                "opciones": {
                    "1": "Regresar_a_la_puerta",
                    "2": "Sentarse_devuelta_en_la_cama"
                }
            },
            "Sentarse_devuelta_en_la_cama": {
                "texto": [
                    "Miedo al 90%",
                    "No sabes qué hacer ahora, salir no es una opción, tienes demasiado miedo de lo que pueda estar allá afuera esperandote",
                    "Comienzas a llorar, sólo quieres que esta pesadilla se acabe",
                    "Los pasos vuelven a resonar, te tensas completamente, escuchando como alguien llega hasta la puerta y la abre, el resonido de la puerta te pone la piel de gallina",
                    "Miedo al 100%",
                    "Contienes la respiración, puedes escuchar a esa otra cosa jadear, las lágrimas no paran de salir",
                    "Deberías de haberte quedado dentro de tu sueño",
                    "Descuida, me encargare de regresarte a él",
                    "No tienes tiempo de pensar en nada, de pronto, las sensaciones se han ido, el miedo se ha ido, por fin la pesadilla parece haber terminado",
                    "Has muerto",
                ],
                "opciones": {
                "1": "Reiniciar"
                }
            },
            "Regresar_a_la_puerta": {
                "texto": [
                    "Aún con el miedo en tus venas, decides que lo mejor es intentar salir de la habitación, quiza si estás en silencio, esa cosa no te encuentre",
                    "Caminas de vuelta a la puerta"
                ],
                "opciones": {
                    "1": "Salir_de_la_habitación"
                }
            },
            "Salir_de_la_habitación": {
                "texto": [
                    "Sales intentando hacer el menor ruido posible, no sabes si lo que caminaba hace un rato sigue ahí",
                    "Con cuidado te quedas quieto intentando escuchar a tu alrededor",
                    "Los pasos resuenan al lado derecho de donde te encuentras, parecen acercarte a ti",
                    "Miedo al 100%"
                ],
                "opciones": {
                    "1": "Correr_hacia_adelante",
                    "2": "Correr_a_la_izquierda"
                }
            },
            "Correr_hacia_adelante": {
                "texto": [
                    "Sin pensar en nada, corres hacia adelante, intentando huir de esa cosa",
                    "Chocas contra lo que parece ser una valla. Al llegarte solo a la cintura, sin poder evitarlo, te precipitas hacia el vacío.",
                    "Sientes el aire recorrer tu cuerpo por unos segundos mientras sigues cayendo.",
                    "De pronto, un dolor agudo te invade en todo tu cuerpo.",
                    "El sonido de algo romperse resuena por todo el lugar.",
                    "Sin poder hablar ni moverte, poco a poco dejas de sentir dolor y miedo.",
                    "Te has roto el cráneo y los huesos. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Correr_a_la_izquierda": {
                "texto": [
                    "Sin pensar en nada, corres hacia la izquierda, intentando huir de esa cosa",
                    "Escuchas tus pasos resonar en el suelo, no puedes pensar en nada cuando escuchas pasos gigantescos correr hacia ti, el miedo recorre todo tu cuerpo",
                    "Miedo al 100%",
                    "De pronto, tu cabeza choca contra una pared, caes al suelo, tu cabeza da vueltas y sientes algo caliente recorrerte la sien hasta tu barbilla, los pasos gigantescos se paran atrás de ti",
                    "Creo que te has hecho daño",
                    "Dejame quitarte el dolor"
                    "Tu mundo parece dar vueltas a tu alrededor, dejas de sentir cualquier cosa y de escuchar, poco a poco toda sensación se va, el miedo se va.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Mover_las_manos_a_tu_alrededor": {
                "texto": [
                    "Decides comenzar a mover tus manos a tu alrededor, buscando algún celular o lampara que te ayude a observar",
                    "Tu mano choca contra una mesita de noche, rápidamente buscas en ésta por algo de utilidad",
                    "Tomas un celular, lo enciendes con rapidez, te emociona el tener un poco de luz para observar",
                    "La luz te ciega los ojos por unos segundos en lo que te acostumbras.",
                    "Miras la pantalla del celular, la hora marca la 1:04 am, por lo que te relajas un poco, es de noche, por eso no hay luz.",
                    "La fecha marca el 02 de enero del año 4567",
                    "Por un momento te confundes, pero pronto asumes que debe ser un error",
                    "Notas que el celular sólo tiene 5% de bateria"
                ],
                "opciones": {
                    "1": "Dejar_el_celular",
                    "3": "Encender_la_lámpara_del_celular"
                }
            },
            "Dejar_el_celular": {
                "texto": [
                    "Asumes que la bateria no te servira de mucho, por lo que dejas el celular en la mesita de noche una vez más"
                ],
                "opciones": {
                    "1": "Levantarte"
                }
            },
            "Encender_la_lámpara_del_celular": {
                "texto": [
                    "Enciendes la lámpara del celular para observar mejor a tu alrededor, no reconoces el lugar en el que te encuentras, pero es sólo una habitación.",
                    "Eso es lo que piensas al principio, pero entonces, notas que el cuarto no tiene ventanas",
                    "Las paredes son de color verde claro, no es un color que te guste mucho, la cama es individual y el cuarto no es muy grande",
                    "Un armario grande se encuentra frente a la cama, la mesa de noche donde conseguiste el celular y la cama, es todo lo que adornan el cuarto",
                    "Una sensación extraña te recorre, algo no parece correcto en la habitación, pero no sabes qué exactamente",
                    "La bateria del celular marca el 4%"
                ],
                "opciones": {
                    "2": "Ir_a_la_puerta",
                    "3": "Buscar_un_cargador"
                }
            },
            "Buscar_un_cargador": {
                "texto": [
                    "Te levantas de la cama y miras detenidamente la mesita de noche, hay una lámpara, pero al intentar encenderla no tienes éxito, parece no tener baterias",
                    "Buscas alrededor de ésta para ver si hay algún cargador que te ayude, no encuentras nada",
                    "Bateria al 3%"
                ],
                "opciones": {
                    "1": "Ir_a_la_puerta",
                    "2": "Inspeccionar_la_habitación"
                }
            },
            "Inspeccionar_la_habitación": {
                "texto": [
                    "Miras alrededor, buscas debajo de la cama, pero no encuentras ningún cargador y, extrañamente, tampoco hay enchufes",
                    "Bateria al 2%",
                    "Caminas hacia el armario, notas que hay dos puertas grandes, donde se suele colgar la ropa, una de las puertas tiene una llave en la chapa, alado, hay una puerta pequeña, la cual en lugar de tener un espejo tiene una ventana de color negro, intentas miras hacia adentro, pero ni con la luz de la lámpara distingues nada",
                    "Finalmente, debajo de la pequeña puerta hay 3 cajones",
                    "Empiezas a abrir el primer cajón, pensando que es más probable que un cargador se encuentre ahí que donde se guarda la ropa.",
                    "Dentro del primer cajón hay una especie de mangueras color negro, muy gruesas que parecen pegadas a la madera, intentas jalas alguna, pero parecen pegadas, intentas sacar completamente el cajón para ver de donde vienen, pero algo parece detenerlo.",
                    "Rápidamente abres el segundo cajón, ahí hay más mangueras negras, no sabes qué es lo que ocurre"
                    "Antes de poder ver nada, el celular se apaga, te quedas nuevamente en la oscuridad",
                    "Miedo al 70%"
                ],
                "opciones": {
                    "1": "Caminar_a_la_puerta",
                    "2": "Seguir_inspeccionando_el_armario"
                }
            },   
            "Caminar_a_la_puerta": {
                "texto": [
                    "Decides que lo mejor es dirigirte a la puerta de la habitación y salir, caminas en la dirección donde recuerdas que estaba la puerta, te golpeas torpemente con algunas cosas, pero finalmente logras llegar a ésta, finalmente, cruzas la puerta, el miedo te recorre al no saber lo que encontraras.",
                    "Con cuidado te quedas quieto intentando escuchar a tu alrededor",
                    "Unos pasos resuenan al lado derecho de donde te encuentras, parecen acercarte a ti",
                    "Miedo al 100%"
                ],
                "opciones": {
                    "1": "Correr_hacia_adelante",
                    "2": "Correr_a_la_izquierda"
                }
            },
            "Ir_a_la_puerta": {
                "texto": [
                    "Caminas en dirección a donde está la puerta de la habitación, afuera encuentras un pasillo, del lado derecho caminas un poco y llegas a una puerta, se encuentra cerrada, por lo que no sabes qué hay dentro.",
                    "Del lado izquierdo hay un pasillo un poco más largo, al final de éste hay una pared cerrada, sin ventanas, y en las paredes del pasillo hay 2 puertas una frente a la otra, parecen ser habitaciones",
                    "Frente a la puerta de tu habitación, hay un barandal que llega hasta unas escaleras, parecen ir a un piso bajo",
                    "Bateria al 3%"
                ],
                "opciones": {
                    "1": "Ir_a_la_derecha",
                    "2": "Ir_a_la_izquierda",
                    "3": "Bajar_las_escaleras"
                }
            },
            "Ir_a_la_derecha": {
                "texto": [
                    "Caminas hacia la derecha hacia la puerta cerrada, tus pasos resuenan en toda la casa ya que el suelo es de madera.",
                    "Al llegar a la puerta tomas el pomo y lo giras, la puerta se abre",
                    "Dentro de ésta, encuentras un baño, todo parece ser normal a simple vista, hay una inodoro, un lavamanos y una ducha que tiene la cortina cerrada",
                    "Incluso aunque todo parezca normal, la sensación es inquieta",
                    "Miedo al 70%",
                    "Bateria al 2%"
                ],
                "opciones": {
                    "1": "Volver_a_las_escaleras",
                    "2": "Seguir_investigando_dentro_del_baño"
                }
            },
            "Volver_a_las_escaleras":{
                "texto": [
                    "Al ver que no hay nada dentro del baño, regresas con pasos apresurados hasta donde estaban las escaleras"
                ],
                "opciones": {
                    "1": "Bajar_las_escaleras",
                    "2": "Ir_a_la_izquierda"
                }
            },
            "Seguir_investigando_dentro_del_baño": {
                "texto":[
                    "Decides entrar en el baño, tiene baldosas blancas en las paredes y el suelo, el techo parece ser de color blanco también",
                    "El inodoro y el lavamanos también son color blanco",
                    "Sin poder evitarlo más, te acercas a la ducha, con las manos temblando, abres la cortina que tapaba la bañera",
                    "No hay nada ahí",
                    "Suspiras con una pequeña risa, tu miedo disminuye",
                    "La luz del celular se apaga entonces, vuelves a quedar en la oscuridad",
                    "Escuchas unos pasos gigantescos correr a tu dirección, el miedo te paraliza y no sabes qué hacer",
                    "Miedo al 100%",
                    "La puerta del baño se abre con un estrepito, algo entra jadeando y se queda frente a ti",
                    "Parece que tienes ganas de un baño, dejame ayudarte con eso",
                    "Una voz rasposa te habla, intentas gritar, pero antes de lograrlo te toma con sus enormes manos del cuello, sus garras son tan largas y te lastiman, no puedes respirar",
                    "Dejas de sentir el suelo en tus pies, intentas patear o golpear, pero nada funciona, entonces un dolor agudo surge en tu cabeza, el crujudo de algo quebrandose resuena en el baño, sientes la frialdad de la bañera en tu espalda, empiezas a sentir tu cuerpo adormecerse",
                    "Dejas de sentir miedo, de sentir dolor, todo desaparece",
                    "Te han abierto la cabeza. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Ir_a_la_izquierda":{
                "texto":[
                    "Caminas hacia la izquierda, lentamente intentando que tus pasos no resuenen tanto en el suelo de madera de la casa",
                    "Al llegar a las puertas, no sabes en cuál entrar",
                    "Bateria al 2%"
                ],
                "opciones": {
                    "1": "Abrir_la_puerta_de_la_izquierda",
                    "2": "Abrir_la_puerta_de_la_derecha"
                }
            },
            "Abrir_la_puerta_de_la_izquierda":{
                "texto":[
                    "Caminas a la puerta de la izquierda, con miedo, tomas el pomo de la puerta y lo intentas girar",
                    "No tienes éxito, la puerta está cerrada",
                    "Decides entonces ir a la puerta derecha, intentas abrirla también, sin ningín éxito, ambas puertas se encuentran cerradas",
                    "Entonces, el celular se apaga, la bateria se ha terminado, nuevamente te quedas en la oscuridad",
                    "Decides que lo mejor es volver a las escaleras, colocas una de tus manos en la pared, no sabes exactamente en qué dirección vas",
                    "Al chocar contra la pared, te das cuenta que caminaste al lado equivocado, el ruido resuena en la casa",
                    "Entonces, escuchas a alguien correr en tu dirección, empiezas a hiperventilar, el miedo te consume",
                    "Miedo al 100%",
                    "Unos pasos gigantescos se paran frente a de ti",
                    "Creo que te has hecho daño",
                    "Dejame quitarte el dolor"
                    "Tu mundo parece dar vueltas a tu alrededor, dejas de sentir cualquier cosa y de escuchar, poco a poco toda sensación se va, el miedo se va.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Abrir_la_puerta_de_la_derecha":{
                "texto":[
                    "Caminas a la puerta de la derecha, con miedo, tomas el pomo de la puerta y lo intentas girar",
                    "No tienes éxito, la puerta está cerrada",
                    "Decides entonces ir a la puerta izquierda, intentas abrirla también, sin ningín éxito, ambas puertas se encuentran cerradas",
                    "Entonces, el celular se apaga, la bateria se ha terminado, nuevamente te quedas en la oscuridad",
                    "Decides que lo mejor es volver a las escaleras, colocas una de tus manos en la pared, no sabes exactamente en qué dirección vas",
                    "Al chocar contra la pared, te das cuenta que caminaste al lado equivocado, el ruido resuena en la casa",
                    "Entonces, escuchas a alguien correr en tu dirección, empiezas a hiperventilar, el miedo te consume",
                    "Miedo al 100%",
                    "Unos pasos gigantescos se paran frente a de ti",
                    "Creo que te has hecho daño",
                    "Dejame quitarte el dolor"
                    "Tu mundo parece dar vueltas a tu alrededor, dejas de sentir cualquier cosa y de escuchar, poco a poco toda sensación se va, el miedo se va.",
                    "Has sido decapitado. Has muerto en el juego."
                ],
                "opciones": {
                    "1": "Reiniciar"
                }
            },
            "Bajar_las_escaleras": {
                "texto": [
                    "Comienzas a bajar las escaleras, los peldaños crujen ruidosamente, hacen que tus nervios aumenten, sigues iluminando todo a tu alrededor, parece que llegaste al lobby de la casa, justo la puerta de entrada",
                    "Sin pensarlo, corres hacia la puerta, con manos temblorosas y algunas lágrimas ya recorriendo tu rostro, intentas girar el pomo",
                    "Lentamente, la puerta se abre",
                    "Sin poder creerlo del todo, sales completamente de la casa, la luz de la luna te reconforma",
                    "La arena en tus pies te devuelve a la realidad",
                    "Una sensación vertiginosa te recorre, sientes un pequeño mareo, de pronto, las estrellas se ven más brillantes, la luna llena ilumina todo a tu alrededor, frente a ti, las olas del mar chocan con la arena",
                    "Miras tu celular, marca la 1:34 am del año 2015",
                    "¿Cómo pudiste olvidarlo?, estás en un viaje familiar con tu familia",
                    "Regresas la mirada a la casa, sólo encuentras una casa de dos pisos, común y corriente, con grandes ventanales en ella",
                    "Entonces, una figura sale de la casa",
                    "Una figura pequeña que se acerca a ti rápidamente",
                    "¿Cariño? ¿Te encuentras bien? Deberías entrar a la casa, podrías enfermarte por estar aquí afuera sin suéter",
                    "Sonries, mientras más lágrimas caen de tu rostro",
                    "Estoy bien mamá, tuve una pesadilla horrible, creo que caminé dormido",
                    "Oh cariño, aquí está mamá, no te preocupes, volvamos a la casa antes de que te enfermes",
                    "Sí, mamá, gracias",
                    "Caminas con la mano de tu madre entre las tuyas, la casa es una casa común y tú sólo estabas teniendo una pesadilla, todo ha pasado",
                    "La luna brilla intensamente en el cielo nocturno y las olas del mar chocan contra la arena",
                    "Ya puedes volver a dormir",
                    "Felicidades, has completado el juego",
                    "Final falso",
                ]
            }
        } 
#Cuando los diccionarios de cada decisión se hayan terminado, se procede con la función mostrar_escenario, la cual será la responsable de tomar la elección que el usuario le indique para proseguir con la historia, mostrando los escenarios adecuados y siguiendo con la historia de acuerdo a las decisiones
    def mostrar_escenario(self, nombre_escenario):
        ancho = ancho_terminal()
        escenario = self.escenarios.get(nombre_escenario)
        if escenario:
            print("\n" + "=" * ancho)
            for linea in escenario["texto"]:
                print(linea)
            print("=" * ancho + "\n")

            opciones_legibles = {key: opcion.replace("_", " ") for key, opcion in escenario.get("opciones", {}).items()}

            for key, opcion in opciones_legibles.items():
                print(f"{key}. {opcion.capitalize()}")  

            eleccion = input("\n¿Qué deseas hacer? (Ingresa un número): ")
            return escenario["opciones"].get(eleccion, "Reiniciar")  
        else:
            return "Reiniciar"
