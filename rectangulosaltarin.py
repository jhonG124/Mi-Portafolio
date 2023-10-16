import pygame             #Importamos pygame que nos permitira realizar el rectangulo y su entorno
pygame.init()             #iniciamos el juego

# Definimos los colores que vamos a usar
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("rectangulo saltarin ")  #Nombre que aparecera en la ventana 
  
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
hecho = False                   #Definimos "hecho" para poder iniciar el bucle del juego
 
reloj = pygame.time.Clock()     #Usamos reloj para establecer cuan rápido se actualiza la pantalla

# Posición de partida del rectángulo
rect_x = 50  #posicion del rectangulo en x
rect_y = 50  #posicion del rectangulo en y

#velocidad y direccion de nuestro rectangulo
rect_cambio_x = 5
rect_cambio_y = 5

#Bucle principal del Programa
while not hecho:
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Avisa de que hemos acabado, por lo que salimos de este bucle
 
    #Desplaza al rectangulo 
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y
    # Rebota al rectángulo si toca algun borde
    if rect_y > 450 or rect_y < 0:
       rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
       rect_cambio_x = rect_cambio_x * -1
    # Establece el fondo de pantalla en negro 
    pantalla.fill(NEGRO)
    # Dibuja un rectángulo rojo dentro del rectangulo blanco
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(pantalla, ROJO, [rect_x + 10, rect_y + 10 , 30, 30])
     # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
pygame.quit()