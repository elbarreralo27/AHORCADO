#EL JUEGO DEL AHORCADO

#Explicación del juego:
El juego de "EL AHORCADO" consiste en adivinar una palabra letra por letra hasta adivinarla por completo, además el usuario podrá escoger entre una dificultad principiante[10 VIDAS], intermedio[7 VIDAS] y experto[5 VIDAS], las vidas representan el número de intentos que tiene el jugador de equivocarse, si sus vidas se acaban automáticamente pierde, y si el jugador adivina la palabra antes de que se acaben sus vidas ganará.

#Como se juega:
El juego comienza preguntándole al usuario que dificultad es con la que quiere jugar, luego de esto se muestra los espacios de las letras que pertenecen a la palabra, en donde se solicita al jugador que ingrese una letra. Si la letra pertenece a la palabra, se indicará que es correcta y será colocada en el lugar que corresponda de la palabra. Y si la letra no pertenece a la palabra, se indicará que es incorrecta y se restará una vida. El juego termina cuando se acaben las vidas o la palabra sea completada.

#Como se ejecuta:
El programa descarga la librería Random, después una palabra de la lista "palabra" es aleatoriamente escogida, Se define una variable "intentos" y se designa el valor de 0, luego se define una lista "palabra_oculta" y se designarán un "_" por cada letra de la palabra. Se solicita al usuario ingresar la dificultad a escoger y en un bucle se verifica la dificultad escogida. Se genera un bucle en el que constantemente se verifique el valor de intentos y si la palabra fue adivinada completamente, si esta no fue completada se solicita al usuario que ingrese una letra, luego se verifican distintas condicionales: Si la letra ya fue usada; La letra ingresada no es una letra; Si la letra no pertenece a la palabra se disminuye una vida; Si la letra si pertenece a la palabra se genera un bucle que se repite según la cantidad de letras ,que tenga la palabra, Si la letra pertenece al número de bucle en el que se encuentra, se remplaza. Caso contrario el bucle continua. Si al verificar el número de intentos es igual a 0, el ciclo se rompe y el juego termina como perdedor. Y si al verificar si la palabra fue completada es verdadero, el juego termina como ganador.

#Ambiente de desarrollo
- Python 3.13
- Spyder 6
- GIT
- GITHUB
- Librería RANDOM
- Visio
- Notepad

#Estructura del pryecto
- Funcionamiento JUEGO DEL AHORCADO.pdf
- Ingreso de dificultad EL AHORCADO.pdf
- EL AHORCADO - CÓDIGO PYTHON.py
- README.md

#Video explicativo
DRIVE: https://drive.google.com/drive/folders/1_IrtixvL_N2qzur27w8K4BTdtfgWp3Cw?usp=sharing

