# 04_kaggle_a_telecharger

**Description** : datasets Kaggle telecharges par `scripts/02_download_kaggle.py` (le telechargement a fonctionne sans token pour ces 4 datasets ; certaines versions du CLI Kaggle peuvent en demander un : voir `LISEZ_MOI.md`).

## 1. basketball - wyattowalsh/basketball (4,4 Go, NON versionne sur Git)
Source : https://www.kaggle.com/datasets/wyattowalsh/basketball - base NBA complete depuis 1946 : joueurs, equipes, matchs, play-by-play, draft combine, officiels, blessures/inactifs.
Formats : `nba.sqlite`, `nba.duckdb`, et `csv/` :
  - `common_player_info.csv` (1 Mo)
  - `draft_combine_stats.csv` (0 Mo)
  - `draft_history.csv` (1 Mo)
  - `game.csv` (20 Mo)
  - `game_info.csv` (2 Mo)
  - `game_summary.csv` (6 Mo)
  - `inactive_players.csv` (7 Mo)
  - `line_score.csv` (11 Mo)
  - `officials.csv` (2 Mo)
  - `other_stats.csv` (3 Mo)
  - `play_by_play.csv` (2256 Mo)
  - `player.csv` (0 Mo)
  - `team.csv` (0 Mo)
  - `team_details.csv` (0 Mo)
  - `team_history.csv` (0 Mo)
  - `team_info_common.csv` (0 Mo)

## 2. nba-players-stats - drgilermo/nba-players-stats
Source : https://www.kaggle.com/datasets/drgilermo/nba-players-stats - statistiques par saison depuis 1950 (PER, WS, BPM...).
- `nba-players-stats/Seasons_Stats.csv` - 24691 lignes, 53 colonnes (5.1 Mo) : Unnamed: 0, Year, Player, Pos, Age, Tm, G, GS, MP, PER...
- `nba-players-stats/Players.csv` - 3922 lignes, 8 colonnes (0.3 Mo) : Unnamed: 0, Player, height, weight, collage, born, birth_city, birth_state...
- `nba-players-stats/player_data.csv` - 4550 lignes, 8 colonnes (0.3 Mo) : name, year_start, year_end, position, height, weight, birth_date, college...

## 3. nba-players-data - justinas/nba-players-data
Source : https://www.kaggle.com/datasets/justinas/nba-players-data - profil (age, taille, poids, draft, pays) et stats par saison.
- `nba-players-data/all_seasons.csv` - 12844 lignes, 22 colonnes (1.9 Mo) : Unnamed: 0, player_name, team_abbreviation, age, player_height, player_weight, college, country, draft_year, draft_round...

## 4. nba-injury-stats-1951-2023 - loganlauton/nba-injury-stats-1951-2023
Source : https://www.kaggle.com/datasets/loganlauton/nba-injury-stats-1951-2023 - blessures de joueurs NBA.
- `nba-injury-stats-1951-2023/NBA Player Injury Stats(1951 - 2023).csv` - 37667 lignes, 6 colonnes (2.5 Mo) : Unnamed: 0, Date, Team, Acquired, Relinquished, Notes...

## Non telecharge
`jonathangmora/nba-shot-locations` : le telechargement exige une authentification (identifiant peut-etre errone ou dataset retire). Les tirs sont couverts par `05_shots_2004_2025`.

Licences : voir la page Kaggle de chaque dataset.
