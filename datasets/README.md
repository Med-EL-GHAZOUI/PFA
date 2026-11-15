# Datasets basketball — PFA « Analyse des performances des sportifs par IA »

Dossier genere automatiquement. Les chiffres ci-dessous sont ceux du telechargement du 15/11/2026.

## Structure

```
datasets/
├── 01_nba_api/               TELECHARGE  (stats NBA officielles, CSV)
├── 02_tracking_sportvu/      TELECHARGE  (1 match en tracking, echantillon)
├── 03_vision_spacejam/       A TELECHARGER MANUELLEMENT (video/poses)
├── 04_kaggle_a_telecharger/  A TELECHARGER (compte Kaggle requis)
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
Le jeu de donnees est heberge sur Google Drive (lien dans `README_source.md`) : **non telecharge automatiquement** (lien Drive, taille non verifiee). Telechargez `dataset.zip` a la main et placez-le dans ce dossier.

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

## Sources et licences

Les stats NBA appartiennent a la NBA : usage pedagogique/recherche, citez la source dans votre rapport. Les depots GitHub sont sous licence MIT. Respectez la licence indiquee sur chaque page Kaggle.
