# Position

Donnée : PCRS (lignes) 

Contrôle : `data\pcrs\modif\ligne-controle.gpkg`  
Référence : `data\pcrs\modif\ligne_source.gpkg`

Le PCRS est téléchargé depuis cette adresse :https://www.pigma.org/geonetwork/srv/eng/catalog.search#/metadata/d3089407-5201-46f4-8c4f-cf8234301e19

## PCRS (lignes)
### Points interpolés : `points`
- `Points le long de la géométrie > Points interpolés`
- Renommer en Points interpolés (source)
- `Champs > Champ virtuel > Expression` :

		distance($geometry, 
		geometry(get_feature('ligne-cible', 'fid', fid)))

- Statistiques > Moyenne
- Statistiques > Max

### Distance moyenne : `ligne_source.distance_moyenne`
> Sans utiliser les points interpolés

- Installer le plugin `Array plus`
- ligne-source > Champs > Ajout de champ virtuel `distance_moyenne`

		array_mean(
			array_foreach(
				generate_series(0, length($geometry), 1),
		
				distance(
					-- point de la couche à contrôler
					line_interpolate_point($geometry, @element),

					-- ligne de la couche de référence
					geometry(get_feature('ligne-cible', 'fid', fid))
				)
			)
		)

### Distance maximale : `ligne_source.distance_max`
- Ajout de champ `distance_max`

		array_avg(
			array_foreach(
				generate_series(0, length($geometry), 1),
		
				distance(
					line_interpolate_point($geometry, @element),
					geometry(get_feature('ligne-cible', 'fid', fid))
				)
			)
		)

## TODO
- `hausdorff_distance`
- `IoU`

## Remarques
A la place de `NNJoin`, on aurait pu aussi utiliser l'algo `Joindre les attributs par le plus proche`