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
 
# FORMATO DE FIGURAS
 
S  = [[ '.....' ,
      '.....' ,
      '..00.' ,
      '.00 ..' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '..00.' ,
      '... 0.' ,
      '.....' ]]
 
Z  = [[ '.....' ,
      '.....' ,
      '.00 ..' ,
      '..00.' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '.00 ..' ,
      '.0 ...' ,
      '.....' ]]
 
I  = [[ '..0 ..' ,
      '..0 ..' ,
      '..0 ..' ,
      '..0 ..' ,
      '.....' ],
     [ '.....' ,
      '0000.' ,
      '.....' ,
      '.....' ,
      '.....' ]]
 
O  = [[ '.....' ,
      '.....' ,
      '.00 ..' ,
      '.00 ..' ,
      '.....' ]]
 
J  = [[ '.....' ,
      '.0 ...' ,
      '.000.' ,
      '.....' ,
      '.....' ],
     [ '.....' ,
      '..00.' ,
      '..0 ..' ,
      '..0 ..' ,
      '.....' ],
     [ '.....' ,
      '.....' ,
      '.000.' ,
      '... 0.' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '..0 ..' ,
      '.00 ..' ,
      '.....' ]]
 
L  = [[ '.....' ,
      '... 0.' ,
      '.000.' ,
      '.....' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '..0 ..' ,
      '..00.' ,
      '.....' ],
     [ '.....' ,
      '.....' ,
      '.000.' ,
      '.0 ...' ,
      '.....' ],
     [ '.....' ,
      '.00 ..' ,
      '..0 ..' ,
      '..0 ..' ,
      '.....' ]]
 
T  = [[ '.....' ,
      '..0 ..' ,
      '.000.' ,
      '.....' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '..00.' ,
      '..0 ..' ,
      '.....' ],
     [ '.....' ,
      '.....' ,
      '.000.' ,
      '..0 ..' ,
      '.....' ],
     [ '.....' ,
      '..0 ..' ,
      '.00 ..' ,
      '..0 ..' ,
      '.....' ]]
 
formas  = [ S , Z , I , O , J , L , T ]
shape_colors  = [( 0 , 255 , 0 ), ( 255 , 0 , 0 ), ( 0 , 255 , 255 ), ( 255 , 255 , 0 ), ( 255 , 165 , 0 ), ( 0 , 0 , 255 ) , ( 128 , 0 , 128 )]
# índice 0 - 6 representan forma
 
 
Clase  Pieza ( objeto ):
    filas  =  20   # y
    columnas  =  10   # x
 
    def  __init__ ( self , columna , fila , forma ):
        auto . x  =  columna
        auto . y  =  fila
        auto . forma  =  forma
        auto . color  =  shape_colors [ formas . índice ( forma )]
        auto . rotación  =  0   # número de 0-3
 
 
def  create_grid ( locked_positions = {}):
    cuadrícula  = [[( 0 , 0 , 0 ) para  x  en el  rango ( 10 )] para  x  en el  rango ( 20 )]
 
    para  i  en  rango ( len ( cuadrícula )):
        para  j  en  rango ( len ( grilla [ i ])):
            if ( j , i ) en  posiciones bloqueadas :
                c  =  posiciones_bloqueadas [( j , i )]
                cuadrícula [ i ] [ j ] =  c
     cuadrícula de retorno
 
 
def  convert_shape_format ( forma ):
    posiciones  = []
    formato  =  forma . forma [ forma . rotación  %  len ( forma . forma )]
 
    para  i , línea  en  enumerate ( formato ):
        fila  =  lista ( línea )
        para  j , columna  en  enumerate ( fila ):
            si  columna  ==  '0' :
                puestos . agregar (( forma . x  +  j , forma . y  +  i ))
 
    para  i , pos  en  enumerate ( posiciones ):
        posiciones [ i ] = ( pos [ 0 ] -  2 , pos [ 1 ] -  4 )
 
     posiciones de retorno
 
 
def  valid_space ( forma , cuadrícula ):
    aceptado_posiciones  = [[( j , i ) para  j  en  rango ( 10 ) si  grilla [ i ] [ j ] == ( 0 , 0 , 0 )] para  i  en  rango ( 20 )]
    aceptado_posiciones  = [ j  para  sub  en  aceptado_posiciones  para  j  en  sub ]
    formateado  =  convert_shape_format ( forma )
 
    para  pos  en  formateado :
        si  pos  no está  en  posiciones aceptadas :
            si  pos [ 1 ] >  - 1 :
                volver  falso
 
    volver  verdadero
 
 
def  check_lost ( posiciones ):
    para  pos  en  puestos :
        x , y  =  pos
        si  y  <  1 :
            volver  verdadero
    volver  falso
 
 
def  get_shape ():
     formas globales , colores de formas
 
     Pieza devuelta ( 5 , 0 , al azar . elección ( formas ))
 
 
def  draw_text_middle ( texto , tamaño , color , superficie ):
    fuente  =  pygame . la fuente . SysFont ( 'comicsans' , tamaño , negrita = True )
    etiqueta  =  fuente . render ( texto , 1 , color )
 
    superficie . blit ( label , ( top_left_x  +  play_width / 2  - ( label . get_ancho () /  2 ), top_left_y  +  play_height / 2  -  label . get_altura () / 2 ))
 
 
def  draw_grid ( superficie , fila , col ):
    sx  =  top_left_x
    sy  =  top_left_y
    para  i  en  rango ( fila ):
        pygame . dibujar . línea ( superficie , ( 128 , 128 , 128 ), ( sx , sy +  i * 30 ), ( sx  +  play_width , sy  +  i  *  30 ))   # líneas horizontales
        para  j  en  rango ( col ):
            pygame . dibujar . línea ( superficie , ( 128 , 128 , 128 ), ( sx  +  j  *  30 , sy ), ( sx  +  j  *  30 , sy  +  play_height ))   # líneas verticales
 
 
def  clear_rows ( cuadrícula , bloqueado ):
    # necesita ver si la fila está limpia, el cambio cada dos filas arriba abajo
 
    inc  =  0
    para  i  en  rango ( len ( cuadrícula ) - 1 , - 1 , - 1 ):
        fila  =  cuadrícula [ i ]
        si ( 0 , 0 , 0 ) no está  en la  fila :
            inc  + =  1
            # agregar posiciones para eliminar de bloqueado
            ind  =  i
            para  j  en  rango ( len ( fila )):
                prueba :
                    del  bloqueado [( j , i )]
                excepto :
                    Seguir
    si  inc  >  0 :
        para  clave  en  ordenada ( lista ( bloqueada ), clave = lambda  x : x [ 1 ]) [:: - 1 ]:
            x , y  =  clave
            si  y  <  ind :
                newKey  = ( x , y  +  inc )
                bloqueado [ nueva clave ] =  bloqueado . pop ( clave )
 
 
def  draw_next_shape ( forma , superficie ):
    fuente  =  pygame . la fuente . SysFont ( 'comicsans' , 30 )
    etiqueta  =  fuente . render ( 'Siguiente forma' , 1 , ( 255 , 255 , 255 ))
 
    sx  =  top_left_x  +  play_width  +  50
    sy  =  top_left_y  +  play_height / 2  -  100
    formato  =  forma . forma [ forma . rotación  %  len ( forma . forma )]
 
    para  i , línea  en  enumerate ( formato ):
        fila  =  lista ( línea )
        para  j , columna  en  enumerate ( fila ):
            si  columna  ==  '0' :
                pygame . dibujar . rect ( superficie , forma . de color , ( sx  +  j * 30 , sy  +  i * 30 , 30 , 30 ), 0 )
 
    superficie . blit ( etiqueta , ( sx  +  10 , sy -  30 ))
 
 
def  draw_window ( superficie ):
    superficie . llenar (( 0 , 0 , 0 ))
    # Título de Tetris
    fuente  =  pygame . la fuente . SysFont ( 'comicsans' , 60 )
    etiqueta  =  fuente . render ( 'TETRIS' , 1 , ( 255 , 255 , 255 ))
 
    superficie . blit ( etiqueta , ( top_left_x  +  play_width  /  2  - ( etiqueta . get_width () /  2 ), 30 ))
 
    para  i  en  rango ( len ( cuadrícula )):
        para  j  en  rango ( len ( grilla [ i ])):
            pygame . dibujar . rect ( superficie , cuadrícula [ i ] [ j ], ( top_left_x  +  j *  30 , top_left_y  +  i  *  30 , 30 , 30 ), 0 )
 
    # dibujar cuadrícula y borde
    draw_grid ( superficie , 20 , 10 )
    pygame . dibujar . rect ( superficie , ( 255 , 0 , 0 ), ( top_left_x , top_left_y , play_width , play_height ), 5 )
    # pygame.display.update ()
 
 
def  main ():
     grilla global
 
    posiciones_bloqueadas  = {}   # (x, y) :( 255,0,0)
    grid  =  create_grid ( posición_bloqueada )
 
    change_piece  =  False
    run  =  True
    current_piece  =  get_shape ()
    next_piece  =  get_shape ()
    reloj  =  pygame . tiempo . Reloj ()
    fall_time  =  0
 
    mientras  corre :
        fall_speed  =  0.27
 
        grid  =  create_grid ( posición_bloqueada )
        fall_time  + =  reloj . get_rawtime ()
        reloj . marca ()
 
        # CÓDIGO DE CAÍDA DE PIEZAS
        if  fall_time / 1000  > =  fall_speed :
            fall_time  =  0
            current_piece . y  + =  1
            si  no es ( valid_space ( current_piece , grid )) y  current_piece . y  >  0 :
                current_piece . y  - =  1
                change_piece  =  True
 
        para  evento  en  pygame . evento . obtener ():
            si  evento . tipo  ==  pygame . QUIT :
                ejecutar  =  falso
                pygame . mostrar . salir ()
                salir ()
 
            si  evento . tipo  ==  pygame . CLAVE :
                si  evento . clave  ==  pygame . K_LEFT :
                    current_piece . x  - =  1
                    si  no es  valid_space ( current_piece , grid ):
                        current_piece . x  + =  1
 
                 evento elif . clave  ==  pygame . K_RIGHT :
                    current_piece . x  + =  1
                    si  no es  valid_space ( current_piece , grid ):
                        current_piece . x  - =  1
                 evento elif . clave  ==  pygame . K_UP :
                    # rotar forma
                    current_piece . rotación  =  pieza_actual . rotación  +  1  %  len ( pieza_corriente . forma )
                    si  no es  valid_space ( current_piece , grid ):
                        current_piece . rotación  =  pieza_actual . rotación  -  1  %  len ( pieza_corriente . forma )
 
                si  evento . clave  ==  pygame . K_DOWN :
                    # mover hacia abajo
                    current_piece . y  + =  1
                    si  no es  valid_space ( current_piece , grid ):
                        current_piece . y  - =  1
 
                '' 'si event.key == pygame.K_SPACE:
                   while valid_space (current_piece, grid):
                       current_piece.y + = 1
                   current_piece.y - = 1
                   print (convert_shape_format (current_piece)) '' '   # todo arreglar
 
        shape_pos  =  convert_shape_format ( current_piece )
 
        # agregar pieza a la cuadrícula para dibujar
        para  i  en  rango ( len ( shape_pos )):
            x , y  =  shape_pos [ i ]
            si  y  >  - 1 :
                cuadrícula [ y ] [ x ] =  pieza_actual . color
 
        # SI LA PIEZA LLEGÓ A TIERRA
        si  change_piece :
            para  pos  en  shape_pos :
                p  = ( pos [ 0 ], pos [ 1 ])
                posiciones_bloqueadas [ p ] =  pieza_actual . color
            current_piece  =  next_piece
            next_piece  =  get_shape ()
            change_piece  =  False
 
            # llame cuatro veces para verificar si hay varias filas claras
            clear_rows ( cuadrícula , posiciones_bloqueadas )
 
        draw_window ( ganar )
        draw_next_shape ( next_piece , win )
        pygame . mostrar . actualizar ()
 
        # Comprobar si el usuario perdió
        if  check_lost ( posición_bloqueada ):
            ejecutar  =  falso
 
    draw_text_middle ( "Perdiste" , 40 , ( 255 , 255 , 255 ), ganar )
    pygame . mostrar . actualizar ()
    pygame . tiempo . retraso ( 2000 )
 
 
def  main_menu ():
    run  =  True
    mientras  corre :
        ganar . llenar (( 0 , 0 , 0 ))
        draw_text_middle ( 'Presione cualquier tecla para comenzar' , 60 , ( 255 , 255 , 255 ), win )
        pygame . mostrar . actualizar ()
        para  evento  en  pygame . evento . obtener ():
            si  evento . tipo  ==  pygame . QUIT :
                ejecutar  =  falso
 
            si  evento . tipo  ==  pygame . CLAVE :
                main ()
    pygame . salir ()
 
 
Win  =  pygame . mostrar . set_mode (( s_ancho , s_altura ))
pygame . mostrar . set_caption ( 'Tetris' )
 
main_menu ()   # iniciar juego
