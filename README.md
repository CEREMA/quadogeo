## Installation
	pip install -r requirements.txt


## Eléments
- [quadorender.py](quadorender.py) : script de rendu 
- [report-FR.xml](report-FR.xml) : rapport XML quadogeo
- [report-19157.xml](report-19157.xml) : rapport XML quadogeo

## Exécuter le script
Pour le rapport XML Fr :

	C:\Python36-64\python quadorender.py report-FR.xml

Pour le rapport XML 19157 :

	C:\Python36-64\python quadorender.py report-19157.xml

Cela crée :

- un rapport : [report.html](report.html)
- des graphiques à la volée d'extension  `.png` auxquels il est fait référence dans [report.html](report.html)

> Voir les scripts `quadorender-FR.bat` et `quadorender-19157.bat`
