import sqlite3
import pandas as pd

def sqlite_query_to_df(db_path, table_name, query):
    """
    Ejecuta una consulta SQL sobre una base de datos SQLite y devuelve los resultados en un DataFrame.

    Argumentos:
    db_path (str): La ruta al archivo de la base de datos SQLite.
    table_name (str): El nombre de la tabla sobre la que se ejecutará la consulta.
    query (str): La consulta SQL que se quiere ejecutar.

    Retorna:
    pd.DataFrame: Un DataFrame con los resultados de la consulta SQL.
    """
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)

    # Ejecutar la consulta SQL y cargar el resultado en un DataFrame
    df = pd.read_sql_query(query, conn)

    # Cerrar la conexión
    conn.close()

    return df
