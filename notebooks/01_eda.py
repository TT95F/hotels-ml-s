# %% [markdown]
# # 01 — EDA & Data Assurance (Hotels)
# - Charge le CSV depuis data/raw (le script `scripts/fetch_data.py` peut le télécharger)
# - Fait un profil rapide + règles de cohérence
# - Sauvegarde éventuellement un extrait nettoyé en data/interim

# %%
import sys, pathlib as pl
ROOT = pl.Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

import pandas as pd
from hotels_ml.config import RAW_DIR, INTERIM_DIR
from hotels_ml.data_io import load_csv
from hotels_ml.qa import basic_profile, rules_hotels

CSV = RAW_DIR / "hotels.csv"
df = load_csv(CSV)
print(df.shape)
df.head()

# %% Profil de base
profile = basic_profile(df)
profile

# %% Règles métiers simples
checks = rules_hotels(df)
checks

# %% (exemple) Nettoyage minimal puis sauvegarde
# df_clean = df.drop_duplicates()
# INTERIM_DIR.mkdir(parents=True, exist_ok=True)
# df_clean.to_csv(INTERIM_DIR / "hotels_clean.csv", index=False)
