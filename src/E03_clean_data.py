import pandas as pd


# -------------------------------------------------------
# Outliers separando tipos de vino
# -------------------------------------------------------

def detect_outliers_iqr_separated(df, threshold=1.5):
    """
    Detecta los valores atípicos en un DataFrame utilizando el rango intercuartil (IQR),
    separando los vinos rojos y blancos.
    
    Argumentos:
        df (pd.DataFrame): El DataFrame sobre el que se realizará la detección de atípicos.
        threshold (float): El umbral del IQR para detectar los outliers. El valor predeterminado es 1.5.
    
    Retorna:
        pd.DataFrame: El DataFrame con una columna extra por cada columna numérica, que indica si es un outlier.

    Ejemplo:
        df_with_outliers = detect_outliers_iqr(df_combined)
    """
    # Dividir el DataFrame en vino rojo y blanco
    df_red = df[df['wine_type'] == 'red']
    df_white = df[df['wine_type'] == 'white']
    
    # Función interna para detectar outliers en cada grupo
    def detect_outliers_group(df_group):
        numeric_columns = df_group.select_dtypes(include=['float64', 'int64']).columns
        
        # Calcular Q1 y Q3 para cada columna numérica
        Q1 = df_group[numeric_columns].quantile(0.25)
        Q3 = df_group[numeric_columns].quantile(0.75)
        
        # Calcular el rango intercuartil (IQR)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        # Detectar outliers por columna
        for col in numeric_columns:
            df_group.loc[:, f'{col}_outlier'] = (df_group[col] < lower_bound[col]) | (df_group[col] > upper_bound[col])
        
        return df_group
    
    # Aplicar la función a los vinos rojos y blancos por separado
    df_red_outliers = detect_outliers_group(df_red)
    df_white_outliers = detect_outliers_group(df_white)
    
    # Combinar los dataframes de vino rojo y blanco nuevamente
    df_combined_with_outliers = pd.concat([df_red_outliers, df_white_outliers])
    
    return df_combined_with_outliers

import pandas as pd

# -------------------------------------------------------
# Sin separación de vinos
# -------------------------------------------------------

def detect_outliers_iqr(df, threshold=1.5):
    """
    Detecta los valores atípicos en un DataFrame utilizando el rango intercuartil (IQR).
    
    Argumentos:
        df (pd.DataFrame): El DataFrame sobre el que se realizará la detección de atípicos.
        threshold (float): El umbral del IQR para detectar los outliers. El valor predeterminado es 1.5.
    
    Retorna:
        pd.DataFrame: El DataFrame con una columna extra por cada columna numérica, que indica si es un outlier.

    Ejemplo:
        df_with_outliers = detect_outliers_iqr(df_combined)
    """
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Calcular Q1 y Q3 para cada columna numérica
    Q1 = df[numeric_columns].quantile(0.25)
    Q3 = df[numeric_columns].quantile(0.75)
    
    # Calcular el rango intercuartil (IQR)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    
    # Detectar outliers por columna
    for col in numeric_columns:
        df[f'{col}_outlier'] = (df[col] < lower_bound[col]) | (df[col] > upper_bound[col])
    
    return df

import pandas as pd

def create_outlier_flag(df):
    """
    Crea una columna 'outlier_flag' que sea True si alguna columna '_outlier' es True.
    
    Argumentos:
        df (pd.DataFrame): El DataFrame con las columnas '_outlier'.
    
    Retorna:
        pd.DataFrame: El DataFrame con la nueva columna 'outlier_flag'.

    Ejemplo:
        df_combined_with_outlier_flag = create_outlier_flag(df_with_outliers)
    """
    outlier_columns = [col for col in df.columns if '_outlier' in col]
    df['outlier_flag'] = df[outlier_columns].any(axis=1)
    
    return df

