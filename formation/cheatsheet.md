<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

<img src=images/antiseche.jfif width=50%>

- [Cheatsheet](#cheatsheet)
   * [EXHAUSTIVITE](#exhaustivite)
   * [FORMAT](#format)
      + [Dates](#dates)
      + [INSEE](#insee)
   * [TOPOLOGIE](#topologie)
      + [Auto-intersections](#auto-intersections)
      + [Doublons et trous](#doublons-et-trous)
      + [Auto-chevauchements](#auto-chevauchements)
      + [Micro-surfaces](#micro-surfaces)
   * [POSITION](#position)
      + [Distance à l'entité la plus proche](#distance-à-lentité-la-plus-proche)
      + [Distances entre 2 couches sur la base d'un champ commun objid](#distances-entre-2-couches-sur-la-base-dun-champ-commun-objid)

<!-- TOC end -->

<!-- TOC --><a name="cheatsheet"></a>
# Cheatsheet
Session ARNIA Idéo BFC - 7 Novembre 2023

<!-- TOC --><a name="exhaustivite"></a>
## EXHAUSTIVITE

- `Style de couche > Transparence`
- `area($geometry)`
- `Vue > Panneaux > Statistiques > Somme des surfaces`
- `Traitements > Supprimer les géométries dupliquées`
- `Traitements > Différence symétrique`
- `Contrôle des couches > Couche > Clic-droit > Voir le décompte des entités`

<!-- TOC --><a name="format"></a>
## FORMAT
<!-- TOC --><a name="dates"></a>
### Dates
	regexp_match(datappro, '^\\d{8}$')
	regexp_match(datappro, '^20\\d{2}\\d{2}\\d{2}$')

<!-- TOC --><a name="insee"></a>
### INSEE

	regexp_match(insee, '^([013-9]\\d|2[AB1-9])\\d{3}$')

<!-- TOC --><a name="topologie"></a>
## TOPOLOGIE

<!-- TOC --><a name="auto-intersections"></a>
### Auto-intersections
- `Traitement > Vérifier la validité géométrique`

<!-- TOC --><a name="doublons-et-trous"></a>
### Doublons et trous
- `Plugins/Extensions > Vérificateur de topolgie > Installer l'extension`
- `Vecteur > Vérificateur de topologie`
	- `Ne doit pas avoir de trou`
	- `Ne doit pas contenir de doublons`

<!-- TOC --><a name="auto-chevauchements"></a>
### Auto-chevauchements
- `Plugins/Extensions > Vérificateur de topolgie > Installer l'extension`
- `Vecteur > Vérificateur de topologie`
	- `Ne doit pas se superposer` (choisir la même couche)

<!-- TOC --><a name="micro-surfaces"></a>
### Micro-surfaces
	area($geometry) < 100

<!-- TOC --><a name="position"></a>
## POSITION
- `Extension > Vecteur > NNJoin`
- `Joindre les attributs par le plus proche`

<!-- TOC --><a name="distance-à-lentité-la-plus-proche"></a>
### Distance à l'entité la plus proche

	distance(
		$geometry,
		aggregate('equipco', 'collect', $geometry)
	)

<!-- TOC --><a name="distances-entre-2-couches-sur-la-base-dun-champ-commun-objid"></a>
### Distances entre 2 couches sur la base d'un champ commun objid
	distance(``
		$geometry, -- géométrie de la couche source
		geometry(
			get_feature(
			'boulodromes', -- couche boulodromes
			'objid', -- colonne dans la couche contrôle cible
			objid -- valeur courante d'objid sur couche source
			)
		)
	)