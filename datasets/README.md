# Datasets basketball — PFA « Analyse des performances des sportifs par IA »

Dossier genere automatiquement. Les chiffres ci-dessous sont ceux du telechargement du 15/11/2026.

## Structure

```
datasets/
├── 01_nba_api/               TELECHARGE  (stats NBA officielles, CSV)
├── 02_tracking_sportvu/      TELECHARGE  (1 match en tracking, echantillon)
├── 03_vision_spacejam/       INDISPONIBLE (lien Drive mort, voir LISEZ_MOI.md)
├── 04_kaggle_a_telecharger/  A TELECHARGER (compte Kaggle requis)
├── 05_shots_2004_2025/       TELECHARGE  (tous les tirs NBA, 22 saisons)
├── 06_raptor_538/            TELECHARGE  (metriques RAPTOR FiveThirtyEight)
├── 07_blessures/             TELECHARGE  (transactions/blessures 2010-2020)
├── 08_combine_physique/      TELECHARGE  (mesures physiques draft combine + draft)
├── 09_calendrier_fatigue/    TELECHARGE  (calendrier, repos, deplacements)
├── 10_shooting_motions/      TELECHARGE  (trajectoires de gestes de tir)
└── scripts/                  scripts de telechargement (reutilisables)
```

## 01_nba_api — stats NBA (source : stats.nba.com via le paquet `nba_api`)

| Fichier | Lignes | Contenu |
|---|---|---|
| `joueurs.csv` | 5198 | Tous les joueurs (id, nom, actif ou non) |
| `equipes.csv` | 30 | Les 30 equipes (id, ville, abreviation) |
| `stats_joueurs_par_match_base.csv` | 3354 | Moyennes par match, saisons 2019-20 a 2024-25 : PTS, REB, AST, STL, BLK, TOV, FG%, 3P%, FT%, MIN... |
| `stats_joueurs_par_match_advanced.csv` | 3354 | Stats avancees memes saisons : OFF_RATING, DEF_RATING, NET_RATING, TS%, USG%, PIE... |
| `game_logs_joueurs.csv` | 150087 | **Une ligne par joueur et par match**, memes saisons. Ideal pour les series temporelles (forme, fatigue). |
| `shotchart_curry_2023-24.csv` | 1445 | Chaque tir de S. Curry : LOC_X, LOC_Y, zone, distance, reussi ou non |
| `shotchart_lebron_2023-24.csv` | 1269 | Idem pour LeBron James |

Colonne cle : `PLAYER_ID` (jointure entre fichiers), `SEASON`, `GAME_ID`.

Idees IA : prediction des points au prochain match (game_logs), clustering de profils de joueurs (stats avancees), modele xFG% (shotcharts), detection de baisse de forme.

Pour d'autres joueurs/saisons : modifier `SEASONS` ou la liste des joueurs dans `scripts/01_download_nba_api.py` et le relancer (`pip install nba_api pandas`).
Note : stats.nba.com limite parfois les requetes ; le script reessaie automatiquement.

## 02_tracking_sportvu — positions des joueurs (echantillon)

Source : GitHub `sealneaward/nba-movement-data` (licence MIT), donnees SportVU saison 2015-16.

- `0021500492.json` (~104 Mo) : match CHA @ TOR du 01/01/2016. Positions x/y de 10 joueurs et du ballon, 25 images/seconde, groupees par evenement.
- `events.csv` : play-by-play de ce match (tirs, fautes, rebonds...) avec `EVENTNUM`, relie aux evenements du JSON.

Le depot complet fait ~3,7 Go (~600 matchs, fichiers .7z). Pour en telecharger d'autres :
`https://raw.githubusercontent.com/sealneaward/nba-movement-data/master/data/<date>.<EQUIPE>.at.<EQUIPE>.7z` (extraction avec 7-Zip ou `py7zr`).
Idees IA : distance parcourue, vitesse, analyse tactique, espacement du terrain.

## 03_vision_spacejam — reconnaissance d'actions (video)

Source : GitHub `simonefrancia/SpaceJam` (licence MIT), ~32 560 exemples (clips 16 images et coordonnees des articulations) pour classer les actions (tir, dribble, passe, defense...).
**Indisponible** : le lien Google Drive du depot renvoie une erreur 404 (verifie le 15/11/2026). Voir `03_vision_spacejam/LISEZ_MOI.md` pour les alternatives.

## 04_kaggle_a_telecharger — datasets Kaggle

Kaggle exige un compte, donc rien n'a ete telecharge. Une fois `kaggle.json` configure : `python scripts/02_download_kaggle.py`.

| Dataset Kaggle | Contenu | Usage |
|---|---|---|
| `wyattowalsh/basketball` | Base SQLite : joueurs, matchs, play-by-play 1946-aujourd'hui (plusieurs Go) | Base historique complete |
| `drgilermo/nba-players-stats` | `Seasons_Stats.csv` depuis 1950 (PER, WS, BPM...) | Prediction de performance, clustering |
| `justinas/nba-players-data` | Taille, poids, draft, stats par saison | Lien profil physique et performance |
| `jonathangmora/nba-shot-locations` | Coordonnees des tirs 1997-2020 | Modele de reussite de tir |
| `loganlauton/nba-injury-stats-1951-2023` | Blessures par joueur | Risque de blessure |

Les identifiants Kaggle sont indiques de memoire : verifiez-les sur le site si un telechargement echoue.

## 05_shots_2004_2025 — tous les tirs NBA (saison reguliere)

Source : GitHub `DomSamangy/NBA_Shots_04_25`. 22 fichiers `NBA_<annee>_Shots.csv.zip` (78 Mo, chacun contient un CSV). Environ 200 000+ tirs par saison (ex. 2024 : 218 701 lignes, 26 colonnes).
Colonnes : `PLAYER_ID`, `PLAYER_NAME`, `TEAM_NAME`, `POSITION`, `GAME_DATE`, `GAME_ID`, `EVENT_TYPE`, `SHOT_MADE`, `ACTION_TYPE`, `SHOT_TYPE`, `BASIC_ZONE`, `LOC_X`, `LOC_Y`, `SHOT_DISTANCE`, `QUARTER`, `MINS_LEFT`, `SECS_LEFT`.
Lecture : `pd.read_csv("NBA_2024_Shots.csv.zip")` (pandas ouvre le zip directement).
Usage IA : modele de probabilite de tir (xFG%), cartes de chaleur, effet de la fatigue/fin de quart-temps. Cible : `SHOT_MADE`.

## 06_raptor_538 — metriques RAPTOR

Source : FiveThirtyEight (`fivethirtyeight/data`, licence a verifier sur le depot, citer la source). `modern_*` = 1977 a aujourd'hui, `historical_*` = 1976 et avant. Par joueur (4685 lignes pour modern) et par equipe : `raptor_offense`, `raptor_defense`, `raptor_total`, `war_total`, `predator_total`, `poss`, `mp`.
Usage IA : variable cible ou feature d'impact joueur, classement, comparaison de profils.

## 07_blessures — blessures / absences

Fichiers : `injuries_alexmjn.csv` (9 783 lignes), `Injuries_Jecoc907.csv` (27 105 lignes), `merged_Jecoc907.csv` (5 578 lignes, 32 colonnes : age, taille, poids, minutes, USG%, drives... fusionne avec les blessures).
Colonnes des deux premiers : `Date`, `Team`, `Acquired` (joueur qui revient), `Relinquished`/`Relinquised` (joueur ecarte ; faute de frappe dans le 1er fichier), `Notes` (nature de la blessure).
Limites : periode 2010-2020 environ ; texte libre dans `Notes` a nettoyer. Sources : GitHub `alexmjn/NBA-Injuries` et `Jecoc907/NBA-Player-Injuries-Analysis` (donnees d'origine Kaggle).
Usage IA : classification du risque de blessure (`merged_Jecoc907.csv` est pret pour ca).

## 08_combine_physique — draft combine

Source : GitHub `josedv82/public_sport_science_datasets`. 
- `NBA_Combine_Anthro (2000-21).csv` (1 395 lignes) : taille, envergure, poids, % masse grasse, mains.
- `NBA_Combine_Physical (2000-21).csv` (1 395 lignes) : saut vertical, sprint, agilite, developpe-couche.
- `NBA_History (1947-2020).csv` (8 083 lignes) : tous les choix de draft.
Encodage `latin-1` (noms de colonnes avec espaces insecables) : `pd.read_csv(f, encoding="latin-1")`.
Usage IA : lien entre profil physique et reussite en NBA, prediction du potentiel.

## 09_calendrier_fatigue — calendrier et charge

`NBA_schedule_metrics.csv` (132 292 lignes, 52 colonnes, 24 Mo) : par equipe et par match, distance de deplacement, jours de repos (`Rest`), changement de fuseau (`Zone`, `Shift*`), series de matchs rapproches (`G3`...`G21`), serie en cours (`Streak`), resultat. Dictionnaire des colonnes dans `dictionary.docx`.
Usage IA : effet de la fatigue et des deplacements sur la performance, a joindre avec `01_nba_api/game_logs_joueurs.csv` (dates et equipes).

## 10_shooting_motions — gestes de tir

`player_metrics.feather` / `.csv` (189 joueurs, 61 colonnes) : metriques du geste de tir (positions x/y/z du ballon et vitesses a differents instants du mouvement). Colonnes abregees (`bx`, `rv`, `mxv`...), expliquees dans `data_dictionary.docx`. Les fichiers `path_detail*` (trajectoires detaillees, ~12 Mo chacun) sont dans le depot source mais non telecharges.
Le fichier source est au format Feather : `pd.read_feather("player_metrics.feather")` (`pip install pyarrow`).
Usage IA : analyse biomecanique, clustering de styles de tir.

## Autres sources utiles (non telechargees)

- `shufinskiy/nba_data` (GitHub) : play-by-play complet 1996-2025, archives compressees avec loader Python.
- `ramirobentes/nba_data` (GitHub) : play-by-play, possessions, lineups en Parquet.
- `josedv82/public_sport_science_datasets` : dossier `NBA Tracking` (tracking SportVU, fichiers decoupes en parties).

## Sources et licences

Les stats NBA appartiennent a la NBA : usage pedagogique/recherche, citez la source dans votre rapport. Les depots GitHub sont sous licence MIT. Respectez la licence indiquee sur chaque page Kaggle.
