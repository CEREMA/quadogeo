## Le coefficient Kappa peut donc se calculer sur des quantités absolues ou relatives?

Sur quantités absolues et nombre.

Il est utile de préciser que ce coefficient kappa n'est pas toujours un indicateur approprié pour mesurer la justesse d'un classement : en effet, dans certaines situations, son comportement est imprévisible, celui-ci se montrant notamment plus adapté lorsque les classes sont relativement indépendantes les unes des autres (soit avec un risque limité de confusion entre les classes). Par ailleurs, cet indicateur réagit mal quand une (ou plusieurs) classe(s) est(sont) peu représentée(s) dans le lot de données.

## Quand utilise-t-on Student ?
Student pour petit échantillon

## Nombre d'échantillons recommandé pour LAQ (Limite d'Acceptation de la Qualité)
L'effectif donné pour la taille de population globale est un effectif minimum pour l'échantillon 

## => Thématique/nb de valeurs d'attributs incorrectes = Logique/cohérence au domaine de valeurs ?
N/C

## => Ecart de position sur une ligne
On utilise la moyenne des écarts des noeuds de la ligne (après densification de la ligne) ou bien la valeur maximale de l'écart (soit le noeud le plus éloigné de la ligne cible) ?

## => Comment passer des taux aux étoiles
N/C

## => Quelles données pour l'arrêté de 2003, à part PCRS ?
N/C

## Comment calculer incertitude et intervalles de confiances sur données temporelles ?
Voir plus bas

## => Taux ou nombre ?
Une question de C. Hoareau sur l'utilisation du taux (relatif) plutôt que le nombre (absolu).
Il semble que le taux soit à privilégier dans la plupart des cas. Dans quel cas utiliser un nombre d'éléments non conformes plutôt qu'un taux ? (Nombre d'auto-intersection, par exemple,...)

## => Taux de nombre ou taux de surface ?
Aussi, quand on parle de taux, dans certains cas, ne devrait-on pas considérer un taux de surface plutôt qu'un taux relatif à un dénombrement ? Par exemple, si je prends le critère d'exhaustivité, pour deux parcelles de grande taille, une en plus et une en moins, le taux relatif au nombre sera sous-estimé par rapport à l'impact carto mesuré par le taux de surface

## => Micro surface et excédent ?
Aussi, il y a d'autres questions soulevées lors de la formation :

- une micro-surface qui apparaît en plus du lot théorique d'entités est-elle un élément en excès ?

## => Doublons
Doit-on considérer les doublons au travers d'une mesure spécifique ? Taux de doublons ? Ou ce sont des excédents ?

## => Mesure de la cohérence de format globalement sur une couche
> Comment combiner les taux de conformité entre champs ?

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

Exemple objets ponctuels,

les pylônes des lignes électriques et les transformateurs = cas n°1

les pylônes des lignes électriques en distinguant basse, moyenne, et haute tension = cas n°2

Exemple objets linéaires,

un réseau de pistes cyclables et bandes cyclables : cas n°1

un réseau de pistes cyclables en distinguant les mono-directionnelles et les bi-directionnelles = cas n°2

Objets surfaciques,

une base de données d’occupation du sol = cas n°2

### Centroïde de surface pour rond point ok mais pas pour le reste
N/C
Le centroïde n'est pas forcément le bon objet à contrôler pour la cohérence de position de surface.

Voir IoU, hausdorff_distance

### A quoi correspond C ?
C n'est pas une constante c'est le rapport entre la classe de précision attendue et la précision de la référence retenue et celui-ci doit être au minimum de 2 ou plus.
dans le texte "C étant le coefficient de sécurité des mesures de contrôle", grosso modo les mesures de référence doivent être au moins 2 fois plus précises que les mesures diagnostiquées

### Précision relative 1
Pour un exemple de mesures relatives, nous faisons à IGN Toulouse des contrôles inter chantier, nous avons donc des mesures d’écarts entre des points issus de différents lots de données en recouvrement. Cela nous permet de qualifier la position relative des chantiers entre eux.

dans le texte "C étant le coefficient de sécurité des mesures de contrôle", grosso modo les mesures de référence doivent être au moins 2 fois plus précises que les mesures diagnostiquées

### Précision relative 2
soit une couche à contrôler

    id | X | Y
    1 | 0 | 1
    2 | 0 | 0
 

et une couche de contrôle

    id | X | Y
    1' | 0 | 2
    2' | 1 | 0
    3' | 0 | 3
 

Pour la précision relative, il faut que je calcule les écarts entre toutes les combinaisons de paires de points possibles entre les deux couches ?

> Nope pour moi, entre paires de points, donc entre points appariés, aka qui représentent la même position. L'idée est là simplement de débiaiser : on enlève à chaque delta de paires de points le delta moyen. Cf page 5 de https://doi.org/10.3390/ijgi10110761. Cf l'image classique https://wikiagile.cesi.fr/index.php?title=Juste_vs_Pr%C3%A9cis . On cherche par exemple à rendre compte que la donnée est bien dessinée (le dessin est juste) mais systématiquement 5m à l'est (son biais).

![](https://wikiagile.cesi.fr/images/6/64/Accurate-vs-precise_fr.png)

### => Souci écart en 3 dimensions
=> Corriger la diapo

### coefficient k pour l'arrêté de précision 2003
y'a des explications sur le fondement de l'arrêté dans XYZ n°108 et géométre 112

toutes ces notions reposent les calculs statistiques

Ce sera par rapport à ce qui est dans les spécifications des données et par rapport au mode de production utilisé ?

## Exactitude et incertitude
Concernant l'incertitude sur des valeurs numériques, si je prends cette série de valeurs

    1, 2, 4, 10, 20

j'ai un écart type d'environ 8. Et une probabilité de 95% équivaut, je
crois, à 2 écart types, soit 16. 16 est donc la demi longueur de mon
intervalle de confiance
 

Ma question est tout d'abord la suivante : en quoi ce demi-intervalle donne des indications sur la qualité de ma donnée ? Elle indique seulement une dispersion de valeurs de mon jeu de données, et ne donne pas d'indication sur la qualité, et donc d'exactitude, non ?
 

Par contre, il serait sensé selon de moi calculer la dispersion des écarts de valeurs entre une référence et une couche à contrôler, soit d'appliquer ce calcul aux écarts de position, de valeurs, de dates...?

> Exactement, la série de valeur en elle-même n'est pas à analyser.

> Par contre on s'intérressera à [ (1 au lieu de 1.1) ; (2 au lieu de 1.9) ; (4 au lieu de 3.5) ; ...] et on sera capable de dire que la valeur en base est précise à +/- tant de %.

## Exactitude sur la mesure temporelle
Une fois mentionné l'exactitude des valeurs numériques, revenons à l'exactitude de la mesure temporelle. Comment calculer concrètement cette incertitude sur la base de l'exemple suivant :

    1 | 16h10
    2 | 17h30
    3 | 10h45
    4 | 22h15
 

Quelle est la valeur de l'exactitude de la mesure temporelle, et comment la calculer ? Conversion des heures en secondes ? => Mais 23h59 n'est-il pas plus proche de 00h00 que 23h00 ?

> Même chose, la valeur 16h10 est en base, au lieu par exemple de la valeur réelle 16h13. On privilégiera me semble t il l'unité dans laquelle la valeur s'exprime (ici, 16h10 est exprimé en h, donc l'incertitude devra être en h).

> La question de la proximité 23h59 / 00h00 se règle d'elle-même : que devrait être la valeur réelle (versus la valeur mesurée et enregistrée 23h59), et donc quel est l'écart absolu ?

## Exactitude et source de contrôle
Encore une fois, une exactitude ne devrait-elle pas s'entendre comme une exactitude par rapport à une valeur véritable (issue de la source de contrôle) ?

> Ben si pour moi.
