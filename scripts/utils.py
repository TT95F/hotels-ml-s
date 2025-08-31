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