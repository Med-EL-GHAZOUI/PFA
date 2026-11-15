# 01_nba_api

**Description** : Statistiques officielles NBA saisons 2019-20 a 2024-25 : joueurs, equipes, moyennes par match (base et avancees), historique match par match de chaque joueur, tirs de Curry et LeBron.

**Source** : NBA API (stats.nba.com) via le paquet Python nba_api

**Lien(s)** : https://github.com/swar/nba_api  |  https://www.nba.com/stats

**Licence / usage** : Donnees officielles NBA, usage pedagogique/recherche ; citer la NBA comme source.

**Comment le retelecharger** : scripts/01_download_nba_api.py

## Fichiers

- `equipes.csv` - 30 lignes, 7 colonnes, 0.0 Mo
- `game_logs_joueurs.csv` - 150087 lignes, 33 colonnes, 23.9 Mo
- `joueurs.csv` - 5198 lignes, 5 colonnes, 0.2 Mo
- `shotchart_curry_2023-24.csv` - 1445 lignes, 24 colonnes, 0.3 Mo
- `shotchart_lebron_2023-24.csv` - 1269 lignes, 24 colonnes, 0.3 Mo
- `stats_joueurs_par_match_advanced.csv` - 3354 lignes, 80 colonnes, 1.3 Mo
- `stats_joueurs_par_match_base.csv` - 3354 lignes, 68 colonnes, 1.0 Mo

## Colonnes (exemple : `equipes.csv`)

`id`, `full_name`, `abbreviation`, `nickname`, `city`, `state`, `year_founded`
