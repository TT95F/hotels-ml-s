from __future__ import annotations
from pathlib import Path
from typing import Optional
import hashlib
import requests
import pandas as pd
from .config import RAW_DIR

def sha256_of_file(path: Path, chunk: int = 1<<20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()

def download_file(url: str, dest: Path, overwrite: bool = False) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and not overwrite:
        return dest
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    dest.write_bytes(r.content)
    return dest

def load_csv(path: Path, **read_csv_kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **read_csv_kwargs)

def save_csv(df: pd.DataFrame, path: Path, index: bool = False) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
    return path

def fetch_hotels(url: str, out: Optional[Path] = None, overwrite: bool = False) -> Path:
    out = out or (RAW_DIR / "hotels.csv")
    return download_file(url, out, overwrite=overwrite)
