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
