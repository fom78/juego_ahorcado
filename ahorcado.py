import os
from random import randint
from gestion import iniciarDB, obtenerPalabras


iniciarDB()

listado=obtenerPalabras()

indice = randint(0,len(listado)-1)
palabraSecreta = listado[indice]
letrasIntentadas=[]
vidasRestantes = 5


while True:
  os.system("cls")
  
  # Mostrar palabra secreta con *
  encontradas=0
  print("Juego del Ahorcado con Python")
  print("-"*50)
  for letra in palabraSecreta: # "casa"
    if letra in letrasIntentadas: # ['a', 'd']
      print(letra, end=" ")
      encontradas = encontradas + 1
    else:
      print("*", end=" ")
  print()
  print("-"*50)

  if encontradas == len(palabraSecreta):
    print("GANASTE")
    break

  # Mostrar letras ya intentadas (Erroneas y las correctas)
  print("######## Letras intentadas ######")
  print(letrasIntentadas) # ['a','t']

  # Mostrar Vidas restantes
  print("######## Vidas Restantes ######")
  print(f"Che te restan {vidasRestantes} intentos")
  
  # Pedir ingreso de una letra
  letraIngresada = input("Letra ? ")

  # Chequear si esta letra esta en letras intentadas
  if letraIngresada in letrasIntentadas: # ['a']
    print(f"La letra >>> {letraIngresada} <<< ya la elegiste anteriormente")
    os.system("pause")
    continue
  else:
    letrasIntentadas.append(letraIngresada)
    if letraIngresada not in palabraSecreta:
      print("Letra no esta en la palabra, restaste una vida")
      vidasRestantes = vidasRestantes - 1

      os.system("pause")



  # # Vidas
  # if letraIngresada not in palabraSecreta:
  #   vidasRestantes = vidasRestantes - 1
    
  

  if vidasRestantes == 0:
    print(f"Perdiste, la palabra era {palabraSecreta}")
    break

