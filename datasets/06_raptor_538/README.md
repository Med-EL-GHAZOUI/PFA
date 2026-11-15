# 06_raptor_538

**Description** : Metriques RAPTOR d'impact joueur et equipe (offense, defense, WAR), version moderne et historique.

**Source** : FiveThirtyEight - nba-raptor

**Lien(s)** : https://github.com/fivethirtyeight/data/tree/master/nba-raptor

**Licence / usage** : Voir le README du depot ; citer FiveThirtyEight.

**Comment le retelecharger** : scripts/03_download_github_datasets.py

## Fichiers

- `historical_RAPTOR_by_player.csv` - 19159 lignes, 15 colonnes, 3.1 Mo
- `historical_RAPTOR_by_team.csv` - 29976 lignes, 17 colonnes, 4.8 Mo
- `modern_RAPTOR_by_player.csv` - 4685 lignes, 21 colonnes, 1.2 Mo
- `modern_RAPTOR_by_team.csv` - 7289 lignes, 23 colonnes, 1.9 Mo

## Colonnes (exemple : `historical_RAPTOR_by_player.csv`)

`player_name`, `player_id`, `season`, `poss`, `mp`, `raptor_offense`, `raptor_defense`, `raptor_total`, `war_total`, `war_reg_season`, `war_playoffs`, `predator_offense`, `predator_defense`, `predator_total`, `pace_impact`
