import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def optimal_clusters(data, max_clusters=10):
    """
    Determina el número óptimo de clusters usando el método del codo.
    
    Args:
        data (pd.DataFrame): DataFrame con las características fisicoquímicas del vino.
        max_clusters (int, opcional): Máximo número de clusters a evaluar. Por defecto, 10.
    
    Returns:
        int: Número óptimo de clusters.
    """
    features = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                'pH', 'sulphates', 'alcohol']
    X = data[features]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    inertia = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)
    
    plt.figure(figsize=(6,4))
    plt.plot(range(1, max_clusters + 1), inertia, marker='o')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Inercia')
    plt.title('Método del Codo para Determinar el Número Óptimo de Clusters')
    plt.show()


def cluster_wines(data, n_clusters=3):
    """
    Agrupa vinos con características similares utilizando Agglomerative Clustering y visualiza los resultados.
    
    Args:
        data (pd.DataFrame): DataFrame con las características fisicoquímicas del vino.
        n_clusters (int, opcional): Número de clusters a generar. Por defecto, 3.
    
    Returns:
        pd.DataFrame: DataFrame con la asignación de clusters añadida.
    
    Ejemplo:
        df = pd.read_csv('wine_data.csv')
        df_clustered = cluster_wines(df, n_clusters=4)
    """
    # Selección de características y normalizaciónd de datos
    features = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                'pH', 'sulphates', 'alcohol']
    X = data[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Aplicación de Agglomerative Clustering
    clustering = AgglomerativeClustering(n_clusters=n_clusters)
    clusters = clustering.fit_predict(X_scaled)
    
    # Agregar etiquetas de cluster al dataframe
    data['cluster'] = clusters
    
    # Reducción de dimensionalidad para visualización
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
    pca_df['cluster'] = clusters
    pca_df['quality'] = data['quality']
    
    # Graficar resultados
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='PC1', y='PC2', hue=pca_df['cluster'], palette='viridis', data=pca_df, alpha=0.7)
    plt.title('Clusters de Vino Basados en Características Fisicoquímicas')
    plt.show()

    print("Distribución de cada variable en función de los clusters:")

    plot_clusters_by_variable(data)
    
    return data


def plot_clusters_by_variable(data):
    """
    Genera diagramas de cajas para analizar la distribución de cada variable en función de los clusters.

    Args:
        data (pd.DataFrame): DataFrame con las características fisicoquímicas del vino y la columna 'cluster'.
    
    Ejemplo:
        df_clustered = cluster_wines(df, n_clusters=4)
        plot_clusters_by_variable(df_clustered)
    """
    features = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                'pH', 'sulphates', 'alcohol', 'quality']
    
    num_features = len(features)
    num_cols = 3
    num_rows = int(np.ceil(num_features / num_cols)) 

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 4 * num_rows))
    axes = axes.flatten()

    for i, feature in enumerate(features):
        sns.boxplot(x='cluster', y=feature, data=data, palette='viridis', ax=axes[i])
        axes[i].set_title(f'Distribución de {feature} por cluster')
        axes[i].set_xlabel('Cluster')
        axes[i].set_ylabel(feature)

    # Ocultar subplots vacíos
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
