<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

<img src=../images/PLU.jfif width=50%>

- [Topologie](#topologie)
   * [Données](#données)
   * [Auto-intersections](#auto-intersections)
   * [Doublons, trous, recouvrements](#doublons-trous-recouvrements)
   * [Micro-surfaces](#micro-surfaces)
      + [Formes trop allongées](#formes-trop-allongées)

<!-- TOC end -->

<!-- TOC --><a name="topologie"></a>
# Topologie

<!-- TOC --><a name="données"></a>
## Données

Projet : 61_cohérence-logique-plu-pertuis-INI.qgz  
Donnée : PLU data\PLU-Pertuis\modif\PLU-Pertuis.gpkg

<!-- TOC --><a name="auto-intersections"></a>
## Auto-intersections
Les auto-intersections sont des erreurs de digitalisation en forme de papillons

![](https://i.stack.imgur.com/8D6u0.png)

Pour les voir, aller dans 

	Traitement > Vérifier la validité > PLU

Cela nous donne plusieurs couches, dont les erreurs de sortie

![](images/18.png)

Voyons l'erreur de plus près. C'est une auto-intersection

![](images/19.png)

> Blague : activer l'option `skip feature` ;-)

<!-- TOC --><a name="doublons-trous-recouvrements"></a>
## Doublons, trous, recouvrements
Pour voir les doublons, les trous ou lacunes, les recrouvrements, on utiliser le `Vérificateur de topologie`

Dans un premier temps, il faut l'activer

	Plugins/Extensions > Vérificateur de topolgie > Installer l'extension

![](images/20.png)

Allez dans

	Vecteur > Vérificateur de topologie

![](images/21.png)

Ajoutez les règles :

- `Ne doit pas avoir de trou`
- `Ne doit pas contenir de doublons`
- `Ne doit pas se superposer` (sélectionne la même couche)

![](images/23.png)

Exécutez

![](images/24.png)

Double-cliquez sur chaque erreur pour aller dessus

<!-- TOC --><a name="micro-surfaces"></a>
## Micro-surfaces
Pour repérer les micro-surfaces, c'est très simple, allez dans la sélection par expression et tapez

	area($geometry) < 100

<!-- TOC --><a name="formes-trop-allongées"></a>
### Formes trop allongées
En aparté, certaines géométries non conformes peuvent avoir une forme très allongée. Pour calculer l'élongation d'un objet, entrez l'expression suivante, par exemple dans un champ virtuel avec un champ `elongation`

	4*$pi*area($geometry)/(length(exterior_ring($geometry))^2)

![](images/25.png)

Et sélectionnez par tri celles qui ont le coefficient le plus faible