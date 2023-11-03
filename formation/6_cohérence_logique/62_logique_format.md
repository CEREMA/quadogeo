<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Cohérence de format](#cohérence-de-format)
   * [Données](#données)
   * [Date](#date)
      + [Longueur](#longueur)
      + [Formatage](#formatage)
      + [Expression régulière](#expression-régulière)
   * [Code Insee](#code-insee)
      + [Expression régulière](#expression-régulière-1)
      + [Formatage conditionnel ](#formatage-conditionnel)
   * [Vue statistiques](#vue-statistiques)

<!-- TOC end -->

<!-- TOC --><a name="cohérence-de-format"></a>
# Cohérence de format

<!-- TOC --><a name="données"></a>
## Données
Projet : 61_cohérence-logique-plu-pertuis-INI.qgz  
Donnée : PLU data\PLU-Pertuis\modif\PLU-Pertuis.gpkg

<!-- TOC --><a name="date"></a>
## Date
<!-- TOC --><a name="longueur"></a>
### Longueur
Une date mal écrite aura une longueur différente de 8.

Par exemple, une date aura comme valeur `20231103`
	
	- Année, ex. 2023 = 4 caractères
	- Mois, ex. 11 = 2 caractères
	- Jour, ex. 03 = 2 caractères

Comme pour l'exo cohérence au domaine de valeurs, allez dans 

	Couche > Ouvrir la table d'attributs > Sélectionner les entités en utilisant une expression

Tapez l'expression suivante :

	length(datappro) != 8

<!-- TOC --><a name="formatage"></a>
### Formatage
Aussi, vous pouvez utiliser le formatage conditionnel, mais sur la **cellule**.

![](images/14.png)

Remplacer @value par l'expression

	length(datappro) != 8

![](images/15.png)

Voilà le résultat

![](images/16.png)

<!-- TOC --><a name="expression-régulière"></a>
### Expression régulière
De manière plus fine, dans la sélection, des expressions régulières peuvent être utilisées :

Seulement des chiffres

	regexp_match(datappro, '^\\d{8}$')

21e siècle (années 2000)
	regexp_match(datappro, '^20\\d{2}\\d{2}\\d{2}$')

<!-- TOC --><a name="code-insee"></a>
## Code Insee
Pour le code INSEE, une sélection peut être opérée de la même façon

	length(insee) != 5

<!-- TOC --><a name="expression-régulière-1"></a>
### Expression régulière
On peut aussi utiliser une expression régulière (elle est assez sophistiquée)

	regexp_match(insee, '^([013-9]\\d|2[AB1-9])\\d{3}$')

<!-- TOC --><a name="formatage-conditionnel"></a>
### Formatage conditionnel 
On peut enfin opérer une sélection de mauvais formats, à la fois pour datappro, insee sur sur la **ligne complète**

	regexp_match(datappro, '^20\\d{2}\\d{2}\\d{2}$') or regexp_match(insee, '^([013-9]\\d|2[AB1-9])\\d{3}$')

<!-- TOC --><a name="vue-statistiques"></a>
## Vue statistiques
A savoir que la vue `Statistiques` peut être utile pour décompter les lignes problématiques

	Vue > Panneaux > Statistiques > PLU > Expression > regexp_match(datappro, '^20\\d{2}\\d{2}\\d{2}$') or regexp_match(insee, '^([013-9]\\d|2[AB1-9])\\d{3}$')

On a 110 lignes qui sont OK

![](images/17.png)


