- sommer les taux de conformité entre champs
- micro surfaces = entités en trop
- passer des taux aux étoiles
- différence justesse et conformité au domaine de valeurs

## Taux ou nombre ?
Une question de C. Hoareau sur l'utilisation du taux (relatif) plutôt que le nombre (absolu).
Il semble que le taux soit à privilégier dans la plupart des cas. Dans quel cas utiliser un nombre d'éléments non conformes plutôt qu'un taux ? (Nombre d'auto-intersection, par exemple,...)

## Taux de nombre, envisager le taux de surface ?
Aussi, quand on parle de taux, dans certains cas, ne devrait-on pas considérer un taux de surface plutôt qu'un taux relatif à un dénombrement ? Par exemple, si je prends le critère d'exhaustivité, pour deux parcelles de grande taille, une en plus et une en moins, le taux relatif au nombre sera sous-estimé par rapport à l'impact carto mesuré par le taux de surface

## Micro surface et excédent ?
Aussi, il y a d'autres questions soulevées lors de la formation :
- une micro-surface qui apparaît en plus du lot théorique d'entités est-elle un élément en excès ?

## Doublons
Doit-on considérer les doublons au travers d'une mesure spécifique ? Taux de doublons ?

## Mesure de la cohérence de format globalement sur une couche
Soit une couche avec deux colonnes typezone et datappro, avec 4 entités :
- Soit les entités 1 et 2 qui sont non conformes par rapport à typezone
- Soit les entités 3 et 4 non conformes sur le format par rapport à datappro. 

On a un taux de conformité pour typezone de 50% et pour datappro de 50%, mais si on assemble les 4 entités, on repère une non conformités sur les 4 entités, soit 100 % du jeu de données.


## Remarque de Benoît Segala, le 6 Décembre, sur l'exhaustivité vs précision thématique, suite au webinaire exhaustivité et cohérence logique

Bonsoir,

Voici un petit retour relatif au second module de la formation « Qualité des données géographiques » de ce jour, et au critère d'exhaustivité.


Suite à la question de ce matin au sujet de « la différence entre taux d’accord et taux d’exhaustivité ? », il me semble que plane pour certains une incompréhension dans les définitions des deux critères “exhaustivité“ et “précision thématique“...

Comme dit dans la fiche n°8 à propos du critère d’exhaustivité, il s’agit bien d’évaluer par rapport à l’ensemble des éléments qui auraient dû figurer dans le jeu de données (dans un premier temps sans distinction de classes) :

- **l’excédent** : données excédentaires présentes dans le jeu de données
- **l’omission** : données absentes d’un jeu de données

La mesure de l’exhaustivité permet donc - en premier lieu - **d’apprécier “globalement“** la bonne représentation de l’ensemble des objets dans le jeu de données, en rapport avec le terrain nominal.

Par rapport à la remarque ajoutée page 1 de cette fiche n°8, « Remarque : ce critère ou ses deux sous-critères peuvent se mesurer pour chaque classe d’objets, attribut ou relation que l’on désire évaluer. », il apparaît que dans la pratique la première mesure de l’exhaustivité est en effet le plus souvent effectuée “globalement“, sur l’ensemble des objets du jeu de données, et donc des classes d'objets. Cette étape permet de qualifier un jeu de données en éliminant le risque d’une part de la présence d’**anomalies** **topologiques** (notamment **trou**, **recouvrement**, **doublon**, …), et d’autre part de couverture spatiale du jeu de données non conforme (**manque** à l’intérieur du **périmètre** d’étude, ou **excédent** en dehors).

Ensuite, à mon avis, deux cas peuvent se présenter, ce qui conditionnent la méthodologie de mesure à mettre en œuvre.

1. **les classes d’objets du jeu de données peuvent être considérées comme “indépendantes“**, dans le sens où il n’existe pas de risque de confusion entre ces classes : une mesure des deux sous-critères (excédent et omission) et du critère d’exhaustivité peut être réalisée indépendamment sur chaque classe.

2. le jeu de données est structuré **selon un ensemble de classes d’objets pouvant entrer en confusion entre elles** : dans ce cas, les deux sous-critères “excédent“ et “omission“ sont alors mesurés, sur chacune des classes mais globalement, au travers de la matrice de classement erroné (MCM) ou matrice de confusion : cf. fiche n°9 sur le critère de précision thématique, et la mesure de la justesse d’un classement.

Certes, la terminologie de "classes" peut vouloir dire plusieurs choses et, comme dit dans la fiche, les méthodes employées pour les deux critères (exhaustivité et précision thématique) sont proches... Alors, peut-être faudrait-il prévoir pour une future formation de présenter les liens entre les deux critères, et leur usage spécifique.

### Exemple objets ponctuels,

les pylônes des lignes électriques et les transformateurs = cas n°1

les pylônes des lignes électriques en distinguant basse, moyenne, et haute tension = cas n°2

### Exemple objets linéaires,

un réseau de pistes cyclables et bandes cyclables : cas n°1

un réseau de pistes cyclables en distinguant les mono-directionnelles et les bi-directionnelles = cas n°2

### Objets surfaciques,

une base de données d’occupation du sol = cas n°2
