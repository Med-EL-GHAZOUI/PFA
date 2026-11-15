"""Telecharge les datasets Kaggle (necessite un compte Kaggle gratuit).

Fonctionne sans compte pour ces datasets publics. Si Kaggle demande une authentification :
 1. kaggle.com > Settings > API > "Create New Token" -> telecharge kaggle.json
 2. Placez-le dans  ~/.kaggle/kaggle.json
 3. pip install kaggle
 4. python scripts/02_download_kaggle.py
"""
import subprocess, sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "04_kaggle_a_telecharger"
DATASETS = [
    "wyattowalsh/basketball",            # base SQLite NBA 1946-aujourd'hui (grosse)
    "drgilermo/nba-players-stats",       # Seasons_Stats.csv depuis 1950
    "justinas/nba-players-data",         # physique + draft + stats
    # "jonathangmora/nba-shot-locations",  # exige une authentification (non telecharge)
    "loganlauton/nba-injury-stats-1951-2023",  # blessures
]
for ds in DATASETS:
    dest = OUT / ds.split("/")[1]
    dest.mkdir(parents=True, exist_ok=True)
    print("->", ds)
    subprocess.run([sys.executable, "-m", "kaggle", "datasets", "download", "-d", ds,
                    "-p", str(dest), "--unzip"], check=False)
