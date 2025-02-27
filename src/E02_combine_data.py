import pandas as pd

def combine_wine_datasets(df_red_wine, df_white_wine):
    """
    Combina los datasets de vino tinto y blanco en un único DataFrame, 
    añadiendo una columna adicional 'wine_type' que indica si el vino es tinto o blanco.
    
    Argumentos:
        df_red_wine (pd.DataFrame): DataFrame con los datos del vino tinto.
        df_white_wine (pd.DataFrame): DataFrame con los datos del vino blanco.
    
    Return:
        pd.DataFrame: DataFrame combinado con una columna adicional 'wine_type'.
    
    Ejemplo:
        df_combined = combine_wine_datasets(df_red_wine, df_white_wine)

    """
    # Añadir la columna 'wine_type' a cada DataFrame
    df_red_wine['wine_type'] = 'red'
    df_white_wine['wine_type'] = 'white'
    
    # Concatenar los dos DataFrames
    combined_df = pd.concat([df_red_wine, df_white_wine], ignore_index=True)
    
    return combined_df
