import tkinter as tk
from tkinter import ttk
from random import randint
from gestion import iniciarDB, obtenerPalabras, obtenerUsuario, editarPuntaje, agregarUsuario, obtenerUsuarios

iniciarDB()

listado=obtenerPalabras()

def iniciar_partida():
  global palabraSecreta, letrasIntentadas,vidasRestantes,puntaje, nombre
  indice = randint(0,len(listado)-1)
  palabraSecreta = listado[indice]
  letrasIntentadas=[]
  vidasRestantes = 5
  puntaje = 0
  nombre=input_nombre.get()
  btn_probar.place(x=20 , y=170 )
  input_nombre.config(state=tk.DISABLED)
  btn_jugar.config(state=tk.DISABLED)
  input_letra.config(state=tk.NORMAL)
  btn_probar.config(state=tk.NORMAL)
  palabra_a_adivinar.place(x=20, y=50)
  input_letra.place(x=150,y=120)
  etiqueta_mi_eleccion.place(x=20, y=120)
  # inicio
  mostrar_palabra_secreta()
  posiciones()
  etiqueta_intentadas.config(text='')
  etiqueta_intentadas.place(x=20, y=220)

  etiqueta_vidas.config(text='')
  etiqueta_vidas.place(x=20, y=255)

  input_letra.delete(0)
  input_letra.focus()


def eleccion_letra():
  global vidasRestantes, puntaje
  letraIngresada = input_letra.get()
  # Chequear si esta letra esta en letras intentadas
  if letraIngresada in letrasIntentadas: # ['a']
    etiqueta_resultado.config(text=f'La letra >>> {letraIngresada} <<< ya la elegiste anteriormente', foreground='yellow')
  else:
    letrasIntentadas.append(letraIngresada)
    if letraIngresada not in palabraSecreta:
      etiqueta_resultado.config(text="Letra no esta en la palabra, restaste una vida", foreground='red')
      vidasRestantes = vidasRestantes - 1
    else:
      etiqueta_resultado.config(text="Letra en la palabra !!", foreground='green')
  if vidasRestantes == 0:
    etiqueta_resultado.config(text=f"{nombre} Perdiste, la palabra era {palabraSecreta}")
    puntaje = -1 * len(palabraSecreta)
    finalizar()
  
  mostrar_palabra_secreta()
  input_letra.delete(0)
  input_letra.focus()

def mostrar_palabra_secreta():
  global puntaje
  # Mostrar palabra secreta con *
  encontradas=0
  progresoPalabra=''
  for letra in palabraSecreta: # "casa"
    if letra in letrasIntentadas: # ['a', 'd']
      progresoPalabra = f'{progresoPalabra} {letra}'
      encontradas = encontradas + 1
    else:
      progresoPalabra = f'{progresoPalabra} *'
  palabra_a_adivinar.config(text=f"{progresoPalabra}", font='bold 14')


  if encontradas == len(palabraSecreta):
    puntaje = vidasRestantes * len(palabraSecreta)
    etiqueta_resultado.config(text=f'GANASTE puntos: {puntaje}',foreground='green')
    finalizar()


  # Mostrar letras ya intentadas (Erroneas y las correctas)
  intentadas=''
  for l in letrasIntentadas:
    intentadas = f'{intentadas}  {l}'
  etiqueta_intentadas.config(text=f'{intentadas.upper()}', font='bold 16')
  
  # Mostrar Vidas restantes
  etiqueta_vidas.config(text=f"{nombre} te restan {vidasRestantes} intentos", font='bold 12')

def posiciones():
  usuarios = obtenerUsuarios()
  fila = 70
  ttk.Label(text='Posiciones', font='Bold 20').place(x=350, y=fila)
  fila=fila+30
  for usu in usuarios:
    tk.Label(
      text=f"{usu['nombre']}",
      # width=60,
      justify='right'
    ).place(x=350,y=fila)
    tk.Label(
      text=f"{usu['puntaje']}",
      width=3
    ).place(x=510,y=fila)
    fila = fila + 20
 
def finalizar():
  global nombre, puntaje
  input_letra.config(state=tk.DISABLED)
  btn_probar.config(state=tk.DISABLED)
  # etiqueta_resultado.config(text=f"{nombre} tu puntaje fue: {puntaje}, este se actualizara en tu usuario", foreground='blue', font='bold')

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

  posiciones()
  input_nombre.config(state=tk.NORMAL)
  btn_jugar.config(state=tk.NORMAL)
  etiqueta_resultado = ttk.Label(text="Ingresa Tu nombre para jugar")
  
  
# Ventana
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.config(width=600, height=300)

# controles
input_nombre=ttk.Entry(
  font=('arial',20,'bold'),
  width=12,
  background="blue",
  justify="center"
)
input_nombre.place(x=310,y=20)

btn_jugar = ttk.Button(
  text=f"Jugar",  
  cursor="hand2", 
  command=iniciar_partida,
  # width=5
  )
btn_jugar.place(x=520 , y=20 )



palabra_a_adivinar = ttk.Label(
  text="Elije una opcion!!",
  width=15,
  background="white",
  borderwidth=0
  )
palabra_a_adivinar.place_forget()

etiqueta_mi_eleccion = ttk.Label(text="Elije una letra: ")
etiqueta_mi_eleccion.place_forget()


input_letra=ttk.Entry(
  font=('arial',20,'bold'),
  width=2,
  background="blue",
  justify="center"
)
input_letra.place_forget()

  
btn_probar = ttk.Button(
  text=f"Probar",  
  cursor="hand2", 
  command=eleccion_letra,
  # width=5
  )
btn_probar.place_forget()

etiqueta_resultado = ttk.Label(text="Ingresa Tu nombre para jugar")
etiqueta_resultado.place(x=20, y=200)

etiqueta_intentadas = ttk.Label(text='')
etiqueta_intentadas.place_forget()
etiqueta_vidas = ttk.Label(text='')
etiqueta_vidas.place_forget()

posiciones()


ventana.mainloop()
