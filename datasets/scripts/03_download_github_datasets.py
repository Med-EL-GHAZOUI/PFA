"""Telecharge des datasets publics depuis GitHub (sans compte)."""
import urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SJ = "https://raw.githubusercontent.com/josedv82/public_sport_science_datasets/main/"
FILES = {}
for y in range(2004, 2026):
    FILES[f"05_shots_2004_2025/NBA_{y}_Shots.csv.zip"] = f"https://raw.githubusercontent.com/DomSamangy/NBA_Shots_04_25/main/NBA_{y}_Shots.csv.zip"
FILES["05_shots_2004_2025/README_source.md"] = "https://raw.githubusercontent.com/DomSamangy/NBA_Shots_04_25/main/README.md"
for n in ["historical_RAPTOR_by_player", "historical_RAPTOR_by_team", "modern_RAPTOR_by_player", "modern_RAPTOR_by_team", "README"]:
    ext = "md" if n == "README" else "csv"
    FILES[f"06_raptor_538/{n}.{ext}"] = f"https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-raptor/{n}.{ext}"
FILES["07_blessures/injuries_alexmjn.csv"] = "https://raw.githubusercontent.com/alexmjn/NBA-Injuries/master/injuries.csv"
FILES["07_blessures/Injuries_Jecoc907.csv"] = "https://raw.githubusercontent.com/Jecoc907/NBA-Player-Injuries-Analysis/master/Injuries.csv"
FILES["07_blessures/merged_Jecoc907.csv"] = "https://raw.githubusercontent.com/Jecoc907/NBA-Player-Injuries-Analysis/master/merged.csv"
for n in ["NBA_Combine_Anthro (2000-21).csv", "NBA_Combine_Physical (2000-21).csv", "NBA_History (1947-2020).csv"]:
    FILES[f"08_combine_physique/{n}"] = SJ + "NBA%20Combine/" + urllib.parse.quote(n)
FILES["09_calendrier_fatigue/NBA_schedule_metrics.csv"] = SJ + "NBA%20Schedule%20Metrics/NBA_schedule_metrics.csv"
FILES["09_calendrier_fatigue/dictionary.docx"] = SJ + "NBA%20Schedule%20Metrics/dictionary.docx"
SM = SJ + "Basketball%20NBA%20Player%20Shooting%20Motions/"
FILES["10_shooting_motions/player_metrics.feather"] = SM + "player_metrics"  # format Feather : pd.read_feather()
FILES["10_shooting_motions/data_dictionary.docx"] = SM + "data%20dictionary.docx"

for rel, url in FILES.items():
    dest = ROOT / rel
    if dest.exists() and dest.stat().st_size > 0:
        continue
    try:
        urllib.request.urlretrieve(url, dest)
        print("OK ", rel, dest.stat().st_size)
    except Exception as e:
        print("ERR", rel, e)
