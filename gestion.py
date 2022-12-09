import sqlite3

def iniciarDB():
  listado=["casa","argentina","mundial","fabrica","casita"]
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS palabras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT
  )
  ''')

  cursor.execute("SELECT * FROM palabras")
  if len(cursor.fetchall()) == 0:
    for p in listado:
      cursor.execute(f"INSERT INTO palabras (palabra) VALUES ('{p}')")   
    conexion.commit()
  
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    puntaje INTEGER
  )
  ''')

  conexion.close()


def obtenerPalabras():
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute("SELECT palabra FROM palabras")
  resultados=[]
  for fila in cursor:
    resultados.append(fila[0])
    

  conexion.close()

  return resultados

def obtenerUsuario(usu):
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute(f"SELECT * FROM usuarios WHERE nombre = '{usu}'") 
  usuario = cursor.fetchone()
  if usuario == None:
    return False
  
  dic = {
    "id": usuario[0],
    "nombre": usuario[1],
    "puntaje": usuario[2]
  }
  return dic
 
def editarPuntaje(id, puntaje):
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute(f"UPDATE usuarios SET puntaje = {puntaje} WHERE id = {id} ")
  conexion.commit()

def agregarUsuario(nombre, puntaje):
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute(f"INSERT INTO usuarios (nombre,puntaje) VALUES ('{nombre}', {puntaje})")
  conexion.commit()

def obtenerUsuarios():
  conexion= sqlite3.connect("ahorcado.db")
  cursor=conexion.cursor()

  cursor.execute(f"SELECT * FROM usuarios ORDER BY puntaje DESC")
  
  registros=[]
  for fila in cursor:
    dic = {
    "id": fila[0],
    "nombre": fila[1],
    "puntaje": fila[2]
    }
    registros.append(dic)
  
  return registros