import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("Monedas.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Monedas (Id INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Pais TEXT NOT NULL, Codigo_ISO TEXT NOT NULL, U_Fraccionaria TEXT NOT NULL, Division decimal(5,0));")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()

    c.execute('INSERT INTO Monedas(Id, Nombre, Pais, Codigo_ISO, U_Fraccionaria, Division) VALUES(?, ?, ?, ?, ?, ?)', entities)
    conn.commit()
    entities = (1, 'Dolar', 'Estados Unidos de America', 'USD', 'Centavo', 100)
    sql_insert(con, entities)