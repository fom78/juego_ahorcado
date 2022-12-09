import os
from colorama import init, Fore
from random import randint
from gestion import iniciarDB, obtenerPalabras, obtenerUsuario, editarPuntaje, agregarUsuario, obtenerUsuarios

init()

iniciarDB()

listado=obtenerPalabras()

indice = randint(0,len(listado)-1)
palabraSecreta = listado[indice]
letrasIntentadas=[]
vidasRestantes = 5

nombre = input("Su nombre: ")
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
    print(f"{Fore.GREEN} {nombre} GANASTE")
    puntaje = vidasRestantes * len(palabraSecreta)
    break

  # Mostrar letras ya intentadas (Erroneas y las correctas)
  print("######## Letras intentadas ######")
  print(letrasIntentadas) # ['a','t']

  # Mostrar Vidas restantes
  print("######## Vidas Restantes ######")
  print(f"{nombre} te restan {vidasRestantes} intentos")
  
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

  

  if vidasRestantes == 0:
    print(f"{Fore.RED} {nombre} Perdiste, la palabra era {palabraSecreta}")
    puntaje = -1 * len(palabraSecreta)
    break


print(f"{Fore.BLUE} {nombre} tu puntaje fue: {puntaje}, este se actualizara en tu usuario")

# Gestion del usuario
nombre = nombre.lower()
usuario = obtenerUsuario(nombre)

if usuario:
  # Existe, modificar puntaje

  usuario["puntaje"] = usuario["puntaje"] + puntaje
  if usuario["puntaje"] <= 0:
    usuario["puntaje"] = 0
  editarPuntaje(usuario["id"],usuario["puntaje"])
else:
  # No existe, agregarlo con el puntaje
  if puntaje <= 0:
    puntaje = 0
  agregarUsuario(nombre, puntaje)

print("Posiciones Totales:")

usuarios = obtenerUsuarios()

for usu in usuarios:
  print(f"{usu['nombre']} >>>> {usu['puntaje']}")

os.system("pause")