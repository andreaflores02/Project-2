import pygame
import random

"""
10 x 20 rejilla cuadrada
Formas: S, Z, I, O, J, L, T
representado en orden por 0 - 6
"""

pygame.font.init()

# VARIABLES GLOBALES
s_ancho = 800
s_altura = 700
bloque_ancho = 300  # quiere decir 300 // 10 = 30 ancho por bloque
bloque_altura = 600  # quiere decir 600 // 20 = 20 altura por bloque
tamano_bloque = 30

superior_izquierda_x = (s_ancho - bloque_ancho) // 2
superior_izquierda_y = s_altura - bloque_altura
