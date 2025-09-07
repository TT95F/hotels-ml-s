import pandas as pd

def glimpse(df, n=5):
    """
    Aperçu type 'glimpse' (R/tidyverse) pour un DataFrame pandas.
    - Affiche nombre de lignes/colonnes
    - Pour chaque colonne: type, nb de non-null, nb d'unique, et quelques valeurs
    """
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}\n")
    for col in df.columns:
        dtype = df[col].dtype
        non_null = df[col].notna().sum()
        unique = df[col].nunique()
        preview = df[col].dropna().unique()[:n]
        print(f"{col:<25} {str(dtype):<10} non-null: {non_null:<6} "
              f"unique: {unique:<6} preview: {preview}")
 
def matrice_display(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Affiche une matrice (count + proportion) pour une colonne donnée d’un DataFrame.

    Args:
        df : DataFrame pandas
        col : Nom de la colonne à analyser (str)

    Returns:
        DataFrame avec deux colonnes:
            - 'count': nombre d’occurrences
            - 'proportion': fréquence relative (somme = 1)

    Nécessite pandas
    """
    counts = df[col].value_counts(dropna=False).sort_index()
    props = df[col].value_counts(normalize=True, dropna=False).sort_index()

    out = pd.DataFrame({
        "count": counts,
        "proportion": props
    })

    return out

def matrice_cross(df: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    """
    Affiche une matrice croisée de counts et proportions 
    entre deux colonnes catégorielles d’un DataFrame.
    """
    # Tableau croisé brut
    cross_counts = pd.crosstab(df[col1], df[col2], margins=False)

    # Proportions (par rapport au total général)
    cross_props = cross_counts / cross_counts.sum().sum()
    cross_props = cross_props.round(4)
    
    # Fusion counts + proportions en MultiIndex
    cross = pd.concat(
        {"count": cross_counts, "proportion": cross_props},
        axis=1
    )
    return cross