import random

palabra =["computadora", "monitor", "mouse", "teclado", "altavoz"]
palabra = random.choice(palabra)
letras_usadas = []
intentos = 0
palabra_oculta = len(palabra) * "_ "

print("Bienvenido al juego del ahorcado!")
dificultad = int(input("Escoja la dificultad con la que quiere jugar\nPrincipiante (1)\nIntermedio (2)\nExperto (3)\nIngrese la dificultado: "))
while dificultad < 1 or dificultad > 3:
   print("ERROR! Ingreso un numero fuera de rango, intentelo de nuevo")
   dificultad = int(input("Escoja la dificultad con la que quiere jugar\nPrincipiante (1)\nIntermedio (2)\nExperto (3)\nIngrese la dificultado: "))


if dificultad == 1:
    print("Ha escogido la dificultad principiante, por lo que tiene 10 intentos.")
    intentos = 10
elif dificultad == 2:
    print("Ha escogido la dificultad intermedio, por lo que tiene 7 intentos.")
    intentos = 7
elif dificultad == 3:
    print("Ha escogido la dificultad experto, por lo que tiene 5 intentos.")
    intentos = 5


while intentos != 0:
    print(palabra_oculta)
    letra = str(input("Ingrese una letra: ")).lower()
    if letra in palabra:
        print("Correcto")
        palabra_oculta = (palabra_oculta.replace(str("_".find(letra), letra)))
        letras_usadas = [letra]
    else:
        print("Incorrecto")
        letras_usadas = [letra]