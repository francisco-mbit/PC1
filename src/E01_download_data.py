import pandas as pd

# -------------------------------------------------------
# EJERCICIO 1) Descarga de datos
# -------------------------------------------------------

def load_csv_to_dataframe(
        file_path: str, 
        separator: str = ';'
) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame de pandas.

    Args:
        file_path (str): The path o URL al archivo CSV.
        separator (str, optional): Delimitador del archivo CSV. Default: ';'.

    Returns:
        pd.DataFrame: DataFrame de pandas con los datos del CSV.
    
    Ejemplo:
        df = load_csv_to_dataframe('winequality-red.csv')
    """
    try:
        df = pd.read_csv(file_path, sep=separator)
        return df
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")
        return None