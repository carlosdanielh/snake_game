#! python 3
'''
snakeultimo.py UN JUEGO DIVERTIDO DE SNAKE!!

segun mision tenemos:
Misión del Curso Python

En la misión del Curso Python se solicita agregar elementos al juego Snake.
Las modificaciones y elementos a agregar son los siguientes:

########################### Aspectos multimedia ###############################

-          Cambio de fondos (inicio, juego principal, pausa y game over).

-          Cambio de la música de fondo.

########################## Aspectos de programación ###########################

-          Se deben crear 2 nuevas manzanas, una verde y otra lila.

-          Se debe cambiar la dimensión en que funciona el juego (ancho y alto)
 de modo que las manzanas puedan incluso aparecer al borde de esta nueva área.

-          Si la serpiente toca manzana verde, la rapidez aumenta en 1 (se debe
 crear variable rapidez y mostrarla en pantalla del juego).

-          Si la serpiente toca manzana lila, la serpiente se alarga 10
cuadrados.

-          Si la serpiente toca manzana roja, además de crecer 1 cuadro,
aumenta puntaje en 1, y cada 3 puntos la rapidez aumenta en 1.

-          Programar 2 teclas en la pantalla de “Game over”, una para volver a
jugar y otra para salir.

Aspectos instruccionales

-          Cambio en instrucciones de inicio: Se debe explicar qué ocurre al
tocar las nuevas manzanas.

-          Cambio en instrucciones de “Game over”

############################  Aspectos de entrega  ############################

-          Se debe entregar una carpeta comprimida con el programa y todos los
recursos utilizados.

################################ FE DE ERRATAS ################################
En el vídeo de ejemplo, segundo 0, líneas 6 y 7.

Dice: Al tocar la manzana verde la serpiente se movera mas rapido y se
descontara un punto.

Debería decir: Al tocar la manzana verde la serpiente se movera mas rapido.

Aclaración ortográfica: No se utilizó tildes para evitar errores de
reconocimiento de codificación.
'''
import random
import os
import pygame
import sys
# #################################funciones###################################


def message_to_screen(msg, color, position_y):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho / 2), position_y
    superficie.blit(textSur, textRect)


def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()


def salir():
    pygame.quit()
    sys.exit()


def intro_juego():
    global ancho
    global altura

    intro = True
    pygame.mixer.music.load('intro.ogg')
    pygame.mixer.music.play(20)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    salir()
        # se explica el cambio de las instruncciones al comer manzana y juego.
        linea_y = 40
        background = load_image('inicio.jpg') #cambio fondo inicio.
        background = pygame.transform.scale(background, (ancho, altura))
        superficie.blit(background, [0, 0])
        message_to_screen('¡Bienvenidos al Juego Snake!', negro, linea_y)
        linea_y += 20
        message_to_screen('El objetivo del juego es controlar una serpiente usando', negro, linea_y)
        linea_y += 20
        message_to_screen('teclas flechas de movimiento para comer manzanas.', negro, linea_y)
        linea_y += 20
        message_to_screen('Si la serpiente toca el borde,pierdes.', negro, linea_y)
        linea_y += 20
        message_to_screen('Al tocar la manzana lila la serpiente crecerá.', negro, linea_y)
        linea_y += 20
        message_to_screen('Si tocas la manzana verde la serpiente se movera mas rapido.', negro, linea_y)
        message_to_screen('¡MUCHA SUERTE!', negro, 500)
        message_to_screen('P - pausar', negro, 200)
        message_to_screen('C - continuar', negro, 250)
        message_to_screen('Q - salir', negro, 300)
        pygame.display.update()
        reloj.tick(5)


def sonido(titulo):
    pygame.mixer.music.load(titulo)
    pygame.mixer.music.play(0)


def comer_sound(titulo):
    comer = pygame.mixer.Sound(titulo)
    comer.play()


def serpiente(tamano_sep, listaSerpiente):

    for i in listaSerpiente:
        pygame.draw.rect(superficie, negro,
                         [i[0], i[1], tamano_sep, tamano_sep])


def message(msg, valor, x, y):
    if valor == None:
        valor = ''
    text = font.render(msg + str(valor), True, negro)
    superficie.blit(text, [x, y])
    pygame.display.update()


def pausa():
    global anchura
    global altura
    sonido('pausa.ogg')
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                elif event.key == pygame.K_q:
                    salir()

        background = load_image('pausar.png')  # cambio imagen PAUSA.
        background = pygame.transform.scale(background, (ancho, altura))
        superficie.blit(background, [0, 0])
        message_to_screen('para continuar presione - C', negro, 100)
        message_to_screen('para terminar presione - Q', negro, 120)
        pygame.display.update()


def gameLoop():
    global speed
    global speed_contador
    global ancho, altura
    sonido('dragons.ogg')  # cambio musica de fondo
    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1
    # las manzanas aparecen al azar incluso en los bordes.
    azary = random.randrange(0, altura - 20, 20)
    azarx = random.randrange(0, ancho - 20, 20)

    azaryl = random.randrange(0, altura - 20, 20)
    azarxl = random.randrange(0, ancho - 20, 20)

    azaryv = random.randrange(0, altura - 20, 20)
    azarxv = random.randrange(0, ancho - 20, 20)

    gameOver = False
    gameExit = False

    point = 0

    while not gameExit:
        game = load_image('backgroundsnake.jpg')  # cambio fondo Principal
        game = pygame.transform.scale(game, (ancho, altura))
        superficie.blit(game, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_y_cambio = 0
                    mover_x_cambio = -tamano_sep
                elif event.key == pygame.K_RIGHT:
                    mover_y_cambio = 0
                    mover_x_cambio = tamano_sep
                elif event.key == pygame.K_UP:
                    mover_x_cambio = 0
                    mover_y_cambio = -tamano_sep
                elif event.key == pygame.K_DOWN:
                    mover_x_cambio = 0
                    mover_y_cambio = tamano_sep
                elif event.key == pygame.K_p:
                    pausa()
                    sonido('dragons.ogg')

        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            speed = 15
            speed_contador = 0
            gameOver = True
            sonido('gameover.ogg')

        mover_y += mover_y_cambio
        mover_x += mover_x_cambio

        # manzana roja
        pygame.draw.rect(superficie, rojo, [azarx, azary, 20, 20])
        # manzana lila
        pygame.draw.rect(superficie, lila, [azarxl, azaryl, 20, 20])
        # manzana verde
        pygame.draw.rect(superficie, verde, [azarxv, azaryv, 20, 20])

        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)

        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        serpiente(tamano_sep, listaSerpiente)

        message('Velocidad: ', speed_contador, 800, 500)
        message('Puntos: ', point, 800, 530)
        message('Pausa - p', None, 800, 560)

        # al tocar manzana roja.
        if mover_x == azarx and mover_y == azary:
            azary = random.randrange(0, altura - 20, 20)
            azarx = random.randrange(0, ancho - 20, 20)
            largoSerpiente += 1  # snake crece un cuadro.
            point += 1  # snake gana un punto por cada comida.

            if point % 3 == 0:  # por cada 3 comidas la velocidad aumenta 1.
                speed += 1
                speed_contador += 1
            comer_sound('comer.ogg')

        # manzana lila.
        if mover_x == azarxl and mover_y == azaryl:
            azaryl = random.randrange(0, altura - 20, 20)
            azarxl = random.randrange(0, ancho - 20, 20)
            largoSerpiente += 10  # snake se alarga 10 veces.
            comer_sound('comer.ogg')

        # manzana verde.
        if mover_x == azarxv and mover_y == azaryv:
            azaryv = random.randrange(0, altura - 20, 20)
            azarxv = random.randrange(0, ancho - 20, 20)
            speed += 1  # aumenta la velocidad en 1
            speed_contador += 1  # muestra la velocidad en pantalla.
            comer_sound('comer.ogg')

        reloj.tick(speed)

        while gameOver:
            # Se explica instruccion para seguir jugando y salir.
            game = load_image('gameoverfinal.jpg')  # cambio imagen gameover
            game = pygame.transform.scale(game, (ancho, altura))
            superficie.blit(game, [0, 0])
            message('Nueva partida presione', None, 720, 200)
            message('V', None, 760, 220)
            message('Salir presione', None, 720, 250)
            message('S', None, 760, 270)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # boton salir
                        salir()
                    if event.key == pygame.K_v:  # boton seguir jugando
                        gameLoop()


def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()
# #################################fin funciones###############################


pygame.init()
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (200, 10, 0)
lila = (182, 149, 192)
verde = (0, 128, 0)
tamano_sep = 20
ancho = 1000  # se cambia el ancho de la pantalla.
altura = 600  # se cambia el alto de la pantalla.
speed = 15
speed_contador = 0
reloj = pygame.time.Clock()
superficie = pygame.display.set_mode((ancho, altura))
icono = pygame.image.load('iconos.png')
pygame.display.set_icon(icono)
font = pygame.font.SysFont('arial.ttf', 35)
pygame.display.set_caption('Serpiente')
intro_juego()
gameLoop()
