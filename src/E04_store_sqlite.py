import sqlite3
import os
import pandas as pd

def store_dataframe_to_sqlite(df, db_dir, db_name, table_name):
    """
    Almacena un DataFrame en una base de datos SQLite dentro del directorio especificado.

    Args:
        df (pd.DataFrame): DataFrame a almacenar.
        db_dir (str): Directorio donde se guardará la base de datos.
        db_name (str): Nombre del archivo de la base de datos SQLite.
        table_name (str): Nombre de la tabla en la que almacenar los datos.

    Ejemplo:
        store_dataframe_to_sqlite(df_clean, 'data', 'wine_data.db', 'wine_quality')
    """
    # Asegurar que el directorio existe y crear ruta
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, db_name)

    # Conectar a la base de datos SQLite, almacenar datos, cerrar conn
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
