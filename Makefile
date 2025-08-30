VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: lab app fetch freeze qa

lab:
	. $(VENV)/bin/activate && jupyter lab

app:
	. $(VENV)/bin/activate && streamlit run app/app.py

fetch:
	. $(VENV)/bin/activate && PYTHONPATH=src $(PY) scripts/fetch_data.py

freeze:
	. $(VENV)/bin/activate && $(PIP) freeze > requirements.txt && git add requirements.txt && git commit -m "Update requirements" && git push

qa:
	. $(VENV)/bin/activate && python - <<'PY'
import sys, pathlib as pl
sys.path.append(str(pl.Path().resolve() / "src"))
from hotels_ml.config import RAW_DIR
from hotels_ml.data_io import load_csv
from hotels_ml.qa import basic_profile, rules_hotels
df = load_csv(RAW_DIR / "hotels.csv")
print(basic_profile(df))
print(rules_hotels(df))
PY