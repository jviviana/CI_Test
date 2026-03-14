import sqlite3
from app import calcular_prioridad


def testdb_connection_and_ticked_creation():
    """Prueba de conexión a la base de datos."""
    # Conexión a una base de datos en memoria para pruebas
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE tickets (id INTEGER, ubicacion TEXT, prioridad TEXT)"
    )
    
    # logica de negocio ypersistencia
    ubicacion = "Laboratorio de redes"
    prioridad= calcular_prioridad(10)
    cursor.execute(
        "INSERT INTO tickets (id, ubicacion, prioridad) VALUES (?, ?, ?)", 
        (1, ubicacion, prioridad)
    )
    conn.commit()
    # verificacion (assert)
    cursor.execute("SELECT prioridad FROM tickets WHERE id = 1")
    resultado = cursor.fetchone()
    assert resultado[0] == "Alta"
    conn.close()
