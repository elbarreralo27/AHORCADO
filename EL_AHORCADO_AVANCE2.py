import random

palabra =["computadora", "monitor", "mouse", "teclado", "altavoz"]
palabra = random.choice(palabra)
letras_usadas = []
intentos = 0
palabra_oculta = len(palabra) * "_ "

print("Bienvenido al juego del ahorcado!")
dificultad = input("Escoja la dificultad con la que quiere jugar\nPrincipiante[10 VIDAS] (1)\nIntermedio[7 VIDAS] (2)\nExperto[5 VIDAS] (3)\nIngrese la dificultado: ")
while True:
    if not dificultad.isdigit():
        print("ERROR! Debe ingresar un número de los mostrados, intentelo de nuevo\n")
        dificultad = input("Escoja la dificultad con la que quiere jugar\nPrincipiante[10 VIDAS] (1)\nIntermedio[7 VIDAS] (2)\nExperto[5 VIDAS] (3)\nIngrese la dificultado: ")
    else:
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
    if intentos == 0:
        print("Has perdido! La palabra era", palabra)
        break
    else:
        print(palabra_oculta)
        letra = str(input("Ingrese una letra: ")).lower().strip()
        if palabra_oculta == palabra:
            print("Ganaste")
            break
        elif len(letra) != 1 or not letra.isalpha():
            print("Por favor ingrese solo una letra, intentelo de nuevo\n")
        elif letra in letras_usadas:
            print("Usted ya ha intentado con esta letra, intente con otra\n")
        elif letra in palabra:
            print("Correcto\n")
            palabra_oculta = (palabra_oculta.replace("_", letra))
            letras_usadas += letra
        elif letra not in palabra:
            print("Incorrecto\n")
            intentos -= 1
            letras_usadas += letra
    
    
    
            
        
            
