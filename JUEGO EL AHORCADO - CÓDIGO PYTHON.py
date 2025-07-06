import random          #Importamos la libreria random

palabra =["computadora", "monitor", "mouse", "teclado", "altavoz"]
palabra = random.choice(palabra)    
letras_usadas = []
intentos = 0
palabra_oculta = len(palabra) * ["_"]          #La cantidad de letras de la palabra se remplaza por "_" y se guardan en la lsita palabra_oculta

print("Bienvenido al juego del ahorcado!")
dificultad = input("Escoja la dificultad con la que quiere jugar\nPrincipiante[10 VIDAS] (1)\nIntermedio[7 VIDAS] (2)\nExperto[5 VIDAS] (3)\nIngrese la dificultado: ")
while True:
    if not dificultad.isdigit():           #Si el usuario ingresa una letra o un número decimal el programa le vuelve a pedir que ingrese un valor                
        print("ERROR! Debe ingresar un número de los mostrados, intentelo de nuevo\n")
        dificultad = input("Escoja la dificultad con la que quiere jugar\nPrincipiante[10 VIDAS] (1)\nIntermedio[7 VIDAS] (2)\nExperto[5 VIDAS] (3)\nIngrese la dificultado: ")
    else:                                  #Caso contrario el dato ingresado se transforma a un int
        dificultad = int(dificultad)
        if dificultad < 1 or dificultad > 3:
            print("ERROR! Ingresó un numero fuera de rango, intentelo de nuevo\n")
            dificultad = input("Escoja la dificultad con la que quiere jugar\nPrincipiante[10 VIDAS] (1)\nIntermedio[7 VIDAS] (2)\nExperto[5 VIDAS] (3)\nIngrese la dificultado: ")
        else:
            break
    

if dificultad == 1:
    print("Ha escogido la dificultad principiante, por lo que tiene 10 VIDAS.")
    intentos = 10
elif dificultad == 2:
    print("Ha escogido la dificultad intermedio, por lo que tiene 7 VIDAS.")
    intentos = 7
elif dificultad == 3:
    print("Ha escogido la dificultad experto, por lo que tiene 5 VIDAS.")
    intentos = 5


while True:
    if intentos == 0:                        #Si los intentos se acaban el juego termina como perdedor
        print("Has perdido! La palabra era '%s'" % (palabra))
        break
    elif not "_" in palabra_oculta:          #Si no encuentra ningun _ en la lsita de palabra_oculta el juego termina como ganador
        print("Felicidad, ganaste!, la palabra era '%s'" % (palabra))
        break
    else:
        print(" ".join(palabra_oculta))          #Los elementos de la lista palabra_oculta (que son las letras previamente remplazadas) se unen y se deja un espacio entre cada letra
        letra = str(input("Ingrese una letra: ")).lower().strip()
        if len(letra) != 1 or not letra.isalpha():          #Si el usuario ingresa más de una letra o un número, se muestra un mensaje
            print("Por favor ingrese solo una letra, intentelo de nuevo\n")
        elif letra in letras_usadas:          #Se verifica si la letra ingresada se encuentra dentro de la lista letras_usadas, y si lo está se muestra un mensaje
            print("Usted ya ha intentado con esta letra, intente con otra\n")
        elif letra in palabra:          #Se verifica si la letra ingresada se encuentra en la palabra 
            print("Correcto\n")
            for i in range(len(palabra)):          #Se realiza un ciclo en el que se verifica cada una de las letras de la palabra 
                if palabra[i] == letra:          #En cada ciclo se verifica si la letra ingresada es igual a la letra que corresponde al ciclo que se encuentra
                    palabra_oculta[i] = letra          #Si se cumple la letra que corresponde al ciclo es remplazada por la letra ingresada
                    letras_usadas += letra          #La letra ingresada se coloca en la lista de letras_usadas
                else:
                    continue
        else:
            print("Incorrecto")
            intentos -= 1          #Se resta un intento
            print("Te quedan %d intentos\n" % (intentos))
            letras_usadas += letra          #La letra ingresada se coloca en la lista de letras_usadas
    
    
    
            
        
            
