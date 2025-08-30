#!/usr/bin/env python
from pathlib import Path
from hotels_ml.config import HOTELS_URL, RAW_DIR
from hotels_ml.data_io import fetch_hotels, sha256_of_file

def main():
    out = fetch_hotels(HOTELS_URL, RAW_DIR / "hotels.csv")
    print(f"✅ Fichier téléchargé: {out}")
    print(f"   SHA256: {sha256_of_file(out)}")

if __name__ == "__main__":
    main()
