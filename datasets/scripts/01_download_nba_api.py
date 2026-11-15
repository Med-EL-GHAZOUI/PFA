"""Telecharge des stats NBA via nba_api (stats.nba.com) en CSV."""
import time, sys
from pathlib import Path
import pandas as pd
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import leaguedashplayerstats, leaguegamelog, shotchartdetail

OUT = Path(__file__).resolve().parent.parent / "01_nba_api"
OUT.mkdir(exist_ok=True)
SEASONS = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
KW = dict(timeout=60)

def save(df, name):
    df.to_csv(OUT / name, index=False)
    print(f"OK {name}: {len(df)} lignes")

def retry(fn, n=3):
    for i in range(n):
        try:
            return fn()
        except Exception as e:
            print("  erreur", type(e).__name__, "retry", i + 1)
            time.sleep(3)
    return None

save(pd.DataFrame(players.get_players()), "joueurs.csv")
save(pd.DataFrame(teams.get_teams()), "equipes.csv")

frames = {"Base": [], "Advanced": []}
for s in SEASONS:
    for mt in frames:
        r = retry(lambda: leaguedashplayerstats.LeagueDashPlayerStats(
            season=s, per_mode_detailed="PerGame", measure_type_detailed_defense=mt, **KW).get_data_frames()[0])
        if r is not None:
            r["SEASON"] = s
            frames[mt].append(r)
        time.sleep(1)
for mt, lst in frames.items():
    if lst:
        save(pd.concat(lst), f"stats_joueurs_par_match_{mt.lower()}.csv")

logs = []
for s in SEASONS:
    r = retry(lambda: leaguegamelog.LeagueGameLog(season=s, player_or_team_abbreviation="P", **KW).get_data_frames()[0])
    if r is not None:
        r["SEASON"] = s
        logs.append(r)
    time.sleep(1)
if logs:
    save(pd.concat(logs), "game_logs_joueurs.csv")

# Shot chart (tirs avec coordonnees) : Stephen Curry et LeBron James, saison 2023-24
for pid, nom in [(201939, "curry"), (2544, "lebron")]:
    r = retry(lambda: shotchartdetail.ShotChartDetail(
        team_id=0, player_id=pid, season_nullable="2023-24",
        season_type_all_star="Regular Season", context_measure_simple="FGA", **KW).get_data_frames()[0])
    if r is not None:
        save(r, f"shotchart_{nom}_2023-24.csv")
    time.sleep(1)
