"""Genere un README.md dans chaque dossier (source, description, colonnes reelles)."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INFO = {
"01_nba_api": ("NBA API (stats.nba.com) via le paquet Python nba_api", "https://github.com/swar/nba_api  |  https://www.nba.com/stats", "Donnees officielles NBA, usage pedagogique/recherche ; citer la NBA comme source.", "Statistiques officielles NBA saisons 2019-20 a 2024-25 : joueurs, equipes, moyennes par match (base et avancees), historique match par match de chaque joueur, tirs de Curry et LeBron.", "scripts/01_download_nba_api.py"),
"02_tracking_sportvu": ("GitHub sealneaward/nba-movement-data (donnees SportVU 2015-16)", "https://github.com/sealneaward/nba-movement-data", "MIT (depot) ; donnees d'origine NBA.", "Un match echantillon (CHA @ TOR, 01/01/2016) : play-by-play en CSV. Le JSON de tracking (positions 25 images/s, 104 Mo) est en local mais non versionne sur Git.", "telechargement manuel (voir README racine)"),
"03_vision_spacejam": ("GitHub simonefrancia/SpaceJam", "https://github.com/simonefrancia/SpaceJam", "MIT (depot).", "Dataset de reconnaissance d'actions de basket (clips + poses). Le lien de donnees est mort : seul le README source est present.", "-"),
"04_kaggle_a_telecharger": ("Kaggle (compte requis)", "https://www.kaggle.com/datasets/wyattowalsh/basketball ; https://www.kaggle.com/datasets/drgilermo/nba-players-stats ; https://www.kaggle.com/datasets/justinas/nba-players-data ; https://www.kaggle.com/datasets/jonathangmora/nba-shot-locations ; https://www.kaggle.com/datasets/loganlauton/nba-injury-stats-1951-2023", "Voir la page de chaque dataset.", "Dossier vide : datasets a recuperer avec un compte Kaggle (identifiants non verifies).", "scripts/02_download_kaggle.py"),
"05_shots_2004_2025": ("GitHub DomSamangy/NBA_Shots_04_25 (donnees NBA)", "https://github.com/DomSamangy/NBA_Shots_04_25", "Voir le depot ; donnees d'origine NBA.", "Tous les tirs de saison reguliere NBA, un fichier CSV par saison (2004 a 2025) : position x/y, zone, distance, type de tir, minute, reussi ou non.", "scripts/03_download_github_datasets.py  (extrait aussi les zip en CSV ; les CSV restent en local, seuls les zip sont sur Git)"),
"06_raptor_538": ("FiveThirtyEight - nba-raptor", "https://github.com/fivethirtyeight/data/tree/master/nba-raptor", "Voir le README du depot ; citer FiveThirtyEight.", "Metriques RAPTOR d'impact joueur et equipe (offense, defense, WAR), version moderne et historique.", "scripts/03_download_github_datasets.py"),
"07_blessures": ("GitHub alexmjn/NBA-Injuries et Jecoc907/NBA-Player-Injuries-Analysis", "https://github.com/alexmjn/NBA-Injuries ; https://github.com/Jecoc907/NBA-Player-Injuries-Analysis", "Voir les depots.", "Blessures et absences de joueurs NBA (~2010-2020) avec date, equipe, joueur et nature de la blessure ; un fichier fusionne avec des stats de jeu.", "scripts/03_download_github_datasets.py"),
"08_combine_physique": ("GitHub josedv82/public_sport_science_datasets - dossier NBA Combine", "https://github.com/josedv82/public_sport_science_datasets/tree/main/NBA%20Combine", "Voir le depot ; donnees d'origine NBA draft combine.", "Mesures anthropometriques et physiques du draft combine (2000-2021) et liste de tous les choix de draft (1947-2020).", "scripts/03_download_github_datasets.py"),
"09_calendrier_fatigue": ("GitHub josedv82/public_sport_science_datasets - dossier NBA Schedule Metrics", "https://github.com/josedv82/public_sport_science_datasets/tree/main/NBA%20Schedule%20Metrics", "Voir le depot.", "Calendrier NBA par equipe et par match avec distances de deplacement, jours de repos, changements de fuseau et series de matchs rapproches.", "scripts/03_download_github_datasets.py"),
"10_shooting_motions": ("GitHub josedv82/public_sport_science_datasets - dossier Basketball NBA Player Shooting Motions", "https://github.com/josedv82/public_sport_science_datasets/tree/main/Basketball%20NBA%20Player%20Shooting%20Motions", "Voir le depot.", "Metriques du geste de tir de 189 joueurs (positions et vitesses du ballon). Dictionnaire des colonnes dans data_dictionary.docx.", "scripts/03_download_github_datasets.py"),
}
def read(p):
    for enc in ("utf-8", "latin-1"):
        try:
            return pd.read_csv(p, low_memory=False, encoding=enc)
        except Exception:
            pass
for folder, (src, url, lic, desc, how) in INFO.items():
    d = ROOT / folder
    lines = [f"# {folder}", "", f"**Description** : {desc}", "", f"**Source** : {src}", "", f"**Lien(s)** : {url}", "", f"**Licence / usage** : {lic}", "", f"**Comment le retelecharger** : {how}", "", "## Fichiers", ""]
    cols = None
    for f in sorted(d.iterdir()):
        if f.name == "README.md" or f.name.startswith("~$"):
            continue
        size = f"{f.stat().st_size/1e6:.1f} Mo"
        if f.suffix == ".csv":
            df = read(f)
            if df is not None:
                lines.append(f"- `{f.name}` - {len(df)} lignes, {df.shape[1]} colonnes, {size}")
                if cols is None or "Shots" in f.name and cols is None:
                    cols = (f.name, list(df.columns))
                continue
        lines.append(f"- `{f.name}` - {size}")
    if cols:
        lines += ["", f"## Colonnes (exemple : `{cols[0]}`)", "", ", ".join(f"`{c}`" for c in cols[1])]
    (d / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("README", folder)
