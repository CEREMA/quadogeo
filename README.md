# Quadogeo
Répertoire d'outils associé au groupe [QuaDoGeo du CNIG](http://cnig.gouv.fr/?page_id=18183)

## Script Quadorender

![](files/thumbnail.png)

Le script `quadorender.py` est une preuve de concept de restitution de la qualité d'une donnée géographique d'après un fichier XML produit selon la norme ISO-19157.

### Installation
	pip install -r requirements.txt

### Script python
- [quadorender.py](quadorender.py) : script de rendu

### XML
Le XML a été produit selon plusieurs versions, selon le niveau d'avancement, et les fichiers réceptionnés

- [report-FR.xml](quadorender/fr/report-FR.xml) : rapport XML inspiré du Répertoire Français des Méta-données
- [report-19157.xml](quadorender/quadogeo-19157/report-19157.xml) : rapport XML inspiré de la norme ISO 19157
- [fake-dng2.0-iso.xml](quadorender/iso-19157/fake-dng2.0-iso.xml) : rapport XML de la norme ISO 19157

### Versions
Les scripts s'appuient sur différentes versions de XML

- [FR (Quadogeo) (première version)](quadorender/fr)
- [Inspiré de ISO-19157 (seconde version)](quadorender/quadogeo-19157)
- [ISO-19157 (troisième version)](quadorender/iso-19157)

### Exécuter le script
Par exemple, pour le script [ISO-19157](quadorender/iso-19157)

	python quadorender.py fake-dng2.0-iso.xml

### Sorties
- un rapport : [report.html](quadorender/quadogeo-19157/report.html)
- des graphiques à la volée d'extension  `.png` auxquels il est fait référence dans [report.html](report.html) ([seulement pour la version Inspirée de ISO-19157](quadorender/quadogeo-19157))

## Présentation
- [Quadorender sur un vrai XML ISO-191157 (Réunion du 7 Octobre 2021)](https://docs.google.com/presentation/d/1JLyhtKRqUqeOSJiULc1fYeCldKf3pZDN1cHfCfp-S5M/edit?usp=sharing)  
- [Quadorender sur un XML ISO-191157 fictif (Réunion du 20 Mai 2021)](https://docs.google.com/presentation/d/18nhTcNG3yMRsH8U5en4q56BwytKDEycApAB1HOnNDjc/edit?usp=sharing)  
- [Quadorender sur un XML inspiré de QuaDoGeo (Réunion du 2 Octobre 2020)](https://docs.google.com/presentation/d/1TCYm14_mcmfzSNTyCeLvuT42KIrhgTr3vMO6HzNbLOg/edit?usp=sharing)

## TODO
- Récupérer un corpus plus important de XML 19157 
- Récupérer les fiches uri associées : PACC, etc...
- Calcul de la note pour le radar en fonction des valeurs : à définir