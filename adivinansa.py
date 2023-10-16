#Juego de adivinar la palabra
#Ejercicio 1
import random                                                                 #Importamos el modulo random para obtener la palaba al azar 
def obtener_palabra_aleatoria():                                              #Definimos la funcion, que nos permitira sacar la palabra aleatoria
 palabras=["casa","familia","carros","telefono","edificio","avion","dinero"]  #Creamos una lista con las palabras 
 palabra_aleatoria=random.choice(palabras)                                    #Le pedimos que saque una palabra al azar de la lista creada 
 return palabra_aleatoria                                                     #retornamos la palabra aleatoria 

def mostrar_tablero(palabra_secreta, letras_adivinadas):                      #Esta funcion nos permitira mostrar el estado actual del tablero del juego
    tablero=""                                                                #En tablero puede estar la letra adivinada o el "_" 
    for letra in palabra_secreta:                                             #usamos un for que nos permitira ver si la letra introducida coincide palabra secreta
        if letra in letras_adivinadas:                                        #si la letra introducida coincide 
            tablero+=letra                                                    #se sumara esta letra en los espacion desconocidos "_"
        else:                                                                 #si no coincide
            tablero+="_"                                                      #En el tablero se le agregara un "_"
    print(tablero)                                                            #Escribimos el tablero con las palabras adivinadas o con los espacios desconocidos "_"

def jugar_ahorcado():                                                         #Esta funcion nos permitira ejecutar el juego 
    palabra_secreta=obtener_palabra_aleatoria()                               #Palabra secreta es la palabra aleatoria que deben adivinar
    letras_adivinadas=[]                                                      #Letras adivinadas son las letras que han adivinado de la palabra secreta y empieza vacia
    intentos_restantes=6                                                      #Definimos la cantidad de errores que puede cometer el usuario para perder

    while intentos_restantes>0:                                               #Creamos un bucle que se ejecutara siempre que los intentos restantes sean mayores a 0
        mostrar_tablero(palabra_secreta, letras_adivinadas)                   #Le pedimos que usa la funcion para mostrar el tablero 
        letra=input("Escribe la letra:").lower()                              #Le pedimos al usuario que escriba una letra y con el comando .lower la convertimos a minuscula
        
        if letra in letras_adivinadas:                                        #si la letra que escribio el usuario esta en la lista de letras adivinadas
            print("Ya escribiste esa letra")                                  #Le decimos que la letra esta repetida
            continue                                                          #usamos "continue" para regresar al bucle y no quitarle un intento
        
        if letra in palabra_secreta:                                          #Si la letra introducida coincide con alguna de la palabra secreta
            letras_adivinadas.append(letra)                                   #Usamos el comando .append para agregar la letra introducida a la variable de letras adivinadas
            if set(letras_adivinadas)==set(palabra_secreta):                  #Usamos el comando set para conmparar si el conjunto de letras adivinadas y palabras secreta es igual
                print("Felicidades, adivinaste la palabra")                   #si son iguales significa que el usuario adivino la palabra y con un print lo felicitamos por ganar
                break                                                         #Usamos la instruccion break para terminar el bucle
        else:                                                                 #Si la letra introducida no esta en las letras de la palabra secreta
            intentos_restantes-=1                                             #Restamos un intento
            print(f"Letra erronea. Quedan {intentos_restantes}")              #Escribimos el mensaje de letra erronea y le mostramos los intentos restantes, usamos el parametro f para mostrar la variable
    if intentos_restantes==0:                                                 #si no le quedan mas intentos al usuario
        print(f"Juego terminado, la palabra era: {palabra_secreta}")          #Escribimos el mensaje juego terminado y le mostramos la palabra que no adivino

jugar_ahorcado()                                                              #Usamos la funcion jugar_ahorcado para iniciar el juego