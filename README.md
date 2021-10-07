## Installation
	pip install -r requirements.txt

## Script
### Script python
- [quadorender.py](quadorender.py) : script de rendu

### XML
- [report-FR.xml](scripts/fr/report-FR.xml) : rapport XML inspiré du Répertoire Français des Méta-données
- [report-19157.xml](scripts/quadogeo-19157/report-19157.xml) : rapport XML inspiré de la norme ISO 19157
- [fake-dng2.0-iso.xml](scripts/iso-19157/fake-dng2.0-iso.xml) : rapport XML de la norme ISO 19157

### Versions
- [FR (Quadogeo) (première version)](scripts/fr)
- [Inspiré de ISO-19157 (seconde version)](scripts/quadogeo-19157)
- [ISO-19157 (troisième version)](scripts/iso-19157)

### Exécuter le script
Par exemple, pour le script [ISO-19157](scripts/iso-19157)

	python quadorender.py fake-dng2.0-iso.xml

### Sorties
- un rapport : [report.html](scripts/quadogeo-19157/report.html)
- des graphiques à la volée d'extension  `.png` auxquels il est fait référence dans [report.html](report.html) ([seulement pour la version Inspirée de ISO-19157](scripts/quadogeo-19157))

## Réunions
[Utilisation d'un vrai XML ISO-191157 (Réunion du 7 Octobre 2021)](https://docs.google.com/presentation/d/1JLyhtKRqUqeOSJiULc1fYeCldKf3pZDN1cHfCfp-S5M/edit?usp=sharing)  
[Utilisation d'un XML ISO-191157 fictif (Réunion du 20 Mai 2021)](https://docs.google.com/presentation/d/18nhTcNG3yMRsH8U5en4q56BwytKDEycApAB1HOnNDjc/edit?usp=sharing)  
[Utilisation d'un XML inspiré de QuaDoGeo (Réunion du 2 Octobre 2020)](https://docs.google.com/presentation/d/1TCYm14_mcmfzSNTyCeLvuT42KIrhgTr3vMO6HzNbLOg/edit?usp=sharing)