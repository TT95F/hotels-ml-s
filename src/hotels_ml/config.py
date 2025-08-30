from pathlib import Path
import os
ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = ROOT / "reports"
MODELS_DIR = ROOT / "models"
HOTELS_URL = os.getenv(
    "HOTELS_URL",
    "https://tidymodels.org/start/case-study/hotels.csv"
)
