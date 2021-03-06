# Webinaire Quadogeo
![](https://www.crige-paca.org/wp-content/uploads/2021/11/banner_quality.png)

## Evènement
- https://www.crige-paca.org/formations-qualite-des-donnees-geographiques/ (Evènement animé par Stéphane Rolle du CRIGE PACA et Mathieu Rajerison du Cerema)
- Rubrique : https://www.crige-paca.org/projets/quadogeo/

## Supports

- [Généralités](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_1cc.pdf)
- [Eléments de contexte](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_2cc.pdf)
- [Exhaustivité](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_3cc.pdf)
- [Cohérence logique](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_4cc.pdf)
- [Position](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_5cc.pdf)
- [Temporel](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_6cc.pdf)
- [Précision thématique](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_7cc.pdf)
- [Outils statistiques](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_8cc.pdf)
- [Echantillonnage](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_9cc.pdf)
- [Ressentir la qualité](https://www.crige-paca.org/wp-content/uploads/2021/12/vf_qualite_10mr_cc.pdf)

# Fiches Quadogeo ISO-19157
- [La norme ISO-19157, en français, et simplifiée, déclinée en fiches](https://www.cerema.fr/fr/actualites/serie-fiches-cerema-qualifier-donnees-geographiques)

# Toronto Data Quality Score
- https://medium.com/open-data-toronto/towards-a-data-quality-score-in-open-data-part-1-525e59f729e9

> "Today, however, catalogue size is less relevant primarily because it fails to measure progress towards the program’s vision of enabling anyone, anywhere, to improve life in Toronto with open data."

> from “how many?” to “how good?” “emphasizing quality over quantity” 

> High-quality data enables high-quality impact

1. Usability (38%): how easy is it to work with the data? Measured by 3 metrics:

- Proportion of columns with meaningful names
- Proportion of columns with a constant value
- Proportion of valid features (for geospatial datasets)

2. Metadata (25%): is the data well described? Measured by percent of metadata fields that have been filled out by the publisher.
3. Freshness (18%): how close to creation is publication? Measured by the time gap between published refresh rate v. actual (e.g. expected daily but it has been a week), and gap between last refreshed and today.
4. Completeness (12%): how much data is missing? Measured by proportion of empty cells in the dataset.
5. Accessibility (7%): is the data easy to access? Measured by whether the data can be accessed via the DataStore API — a freebie for the MVP, as it contains data from the DataStore only.

> Instead of reporting the score as a percentage we opted for medals because, at this stage, getting the overall concept right is more important than the specific number.

> Is not a measure for how accurate data is — that’s for publishers. 

Contact : https://twitter.com/CareduzTweets , opendata@toronto.ca

- https://medium.com/open-data-toronto/towards-a-data-quality-score-in-open-data-part-2-3f193eb9e21d
- https://open.toronto.ca/dataset/catalogue-quality-scores/

> C. Create an automatic scoring and delivery mechanism

> At the end of this, 4 goals were met. Goal C, automatic scoring, is halfway there: the scoring is done automatically via a script but, for the beta, it has to be run manually.

> We brought together a Data Quality Working Group to aid us with the ambiguous meaning of quality and validate our approach. It was composed of a diverse membership: multiple teams, users with a range of comfort around data, both data producers and consumers, and an array of wide-ranging perspectives including from outside our organization altogether.

> It quickly became evident that quality depends on the degree to which data fits its intended purpose 

![](https://miro.medium.com/max/1050/1*jPxnU2YdDqamiSWnLPoq-A.png)

![](https://miro.medium.com/max/1050/1*IhlOrx9MC2kREW5fg28P5A.png)

![](https://miro.medium.com/max/1050/1*z159zofS4aSnjFih-J2Lhw.png)

> If interested, the algorithms tested were outlined in a paper comparing trade-offs in rank weighting methods: rank sum, rank reciprocal, sum and reciprocal, rank exponent, rank order centroid.

![](https://miro.medium.com/max/1050/1*OiDbEc7T-_ef8Q82gG_z7w.png)

Script quality score : https://github.com/open-data-toronto/framework-data-quality/blob/master/data_quality_score.ipynb

# Mesures
## Norme ISO-19157
[Norme ISO-19157 en XML](https://github.com/ISO-TC211/XML/tree/master/standards.iso.org.annotated/iso/19157)  
[Site ICA](https://wiki.icaci.org/index.php?title=ISO_19157:2013_Geographic_information_-_Data_quality)
Modèle :
![](files/modele.jpg)

## Géocatalogue
[Catalogue des mesures de qualité QuaDoGeo
](https://data.geocatalogue.fr/ncl/_mesuresQuaDoGeo)

### Caractéristiques de chaque mesure

- Nom
- Alias
- Critère / sous-critère
- Mesure de base
- Définition
- Description
- Paramètre
- Type de valeur
- Structure de la valeur
- Référence de la source
- Exemple
- Identifiant

# Quadorender
- [Quadorender sur un vrai XML ISO-191157 (Réunion du 7 Octobre 2021)](https://docs.google.com/presentation/d/1JLyhtKRqUqeOSJiULc1fYeCldKf3pZDN1cHfCfp-S5M/edit?usp=sharing)  
- [Quadorender sur un XML ISO-191157 fictif (Réunion du 20 Mai 2021)](https://docs.google.com/presentation/d/18nhTcNG3yMRsH8U5en4q56BwytKDEycApAB1HOnNDjc/edit?usp=sharing)  
- [Quadorender sur un XML inspiré de QuaDoGeo (Réunion du 2 Octobre 2020)](https://docs.google.com/presentation/d/1TCYm14_mcmfzSNTyCeLvuT42KIrhgTr3vMO6HzNbLOg/edit?usp=sharing)

# Remontée qualité
- [La remontée qualité utilisateurs (4 Juin 2020)](https://docs.google.com/presentation/d/1QCJtAPdPrcjRj9KQZuyjjTQt4q-ZrH4tGYIh3JNODAc/edit?usp=sharing)
- [Qualité, usages et usagers, est-ce usant ? (21 Novembre 2019)](https://drive.google.com/file/d/1Lx3LKOPJJZOkxrm-kApcTmUiupYhQ5kD/view)

# Expressions régulières
https://github.com/datagistips/memos/blob/main/regexes.md

# Méthodes QGIS
https://hfcqgis.opendatasicilia.it/gr_funzioni/gruppo_funzioni/  

http://www.geoinformations.developpement-durable.gouv.fr/fichier/pdf/verification_et_correction_de_geometrie_v3_0_cle5fcd75.pdf?arg=177834719&cle=830634f7888fc808498f0c41704664611af04021&file=pdf%2Fverification_et_correction_de_geometrie_v3_0_cle5fcd75.pdf

# Statistiques
Statistiques pour statophobes : https://perso.univ-rennes1.fr/denis.poinsot/Statistiques_%20pour_statophobes/STATISTIQUES%20POUR%20STATOPHOBES.pdf  
https://fr.wikipedia.org/wiki/Loi_de_Fisher

# Plugins QGIS
- iso : https://plugins.qgis.org/search/?q=iso
- prepair : https://plugins.qgis.org/plugins/prepair/
- dataset quality assurance : https://plugins.qgis.org/plugins/dataset_qa_workbench/
- acceptable quality limit : https://plugins.qgis.org/plugins/SampleByFeatures/
- iso 19157 : https://plugins.qgis.org/plugins/iso_19157/
- thematic accuracy : https://plugins.qgis.org/plugins/thematic_accuracy/
- quality : https://plugins.qgis.org/search/?q=quality
- check : https://plugins.qgis.org/search/?q=check
- valid : https://plugins.qgis.org/search/?q=valid
- control : https://plugins.qgis.org/search/?q=control
- repair : https://plugins.qgis.org/search/?q=repair

# Méthodes
- https://medium.com/epfl-extension-school/advanced-exploratory-data-analysis-eda-with-python-536fa83c578a
- https://blog.cleverelephant.ca/2018/06/polygon-splitting.html
