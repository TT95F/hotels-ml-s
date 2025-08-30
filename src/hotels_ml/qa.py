from __future__ import annotations
import pandas as pd

def basic_profile(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_pct": (df.isna().mean()*100).round(2).sort_values(ascending=False).to_dict(),
        "duplicates": int(df.duplicated().sum()),
    }

def rules_hotels(df: pd.DataFrame) -> dict:
    checks = {}
    if "adr" in df.columns:
        checks["adr_non_negative"] = bool((df["adr"] >= 0).all())
    for col in ["adults","children","babies"]:
        if col in df.columns:
            checks[f"{col}_non_negative"] = bool((df[col] >= 0).all())
    if {"stays_in_weekend_nights","stays_in_week_nights"} <= set(df.columns):
        stays = df["stays_in_weekend_nights"].fillna(0) + df["stays_in_week_nights"].fillna(0)
        checks["total_stays_non_negative"] = bool((stays >= 0).all())
    return checks
