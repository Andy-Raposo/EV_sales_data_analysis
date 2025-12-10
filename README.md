# Analysis de ventes des voitures VE (2010-2024) – Europe

## Description
Ce projet analyse les ventes de véhicules électriques (EV) entre 2010 et 2024 dans plusieurs pays européens (Espagne, France, Allemagne) et l'UE27. L'objectif est de comprendre les tendances du marché, comparer la croissance par pays et tirer des insights pour les stratégies futures de mobilité durable.

Le projet montre : 
- Nettoyage et préparation d’un dataset réel.
- Analyse descriptive des ventes et du stock d’EV.
- Comparaison entre pays et par type de motorisation (BEV, PHEV, FCEV).
- Visualisations claires avec Seaborn et Matplotlib.
- Création d’une fonction Python réutilisable pour calculer l’évolution annuelle en pourcentage.

## Dataset
Le dataset contient les colonnes suivantes :  
- `region` : Pays ou zone géographique.  
- `category` : Historique ou projection (ici uniquement Historical).  
- `parameter` : Type de métrique (EV sales, EV stock, EV sales share, EV stock share, etc.).  
- `powertrain` : Type de motorisation EV (BEV, PHEV, FCEV, EV).  
- `year` : Année.  
- `unit` : Unité de mesure (Vehicles ou percent).  
- `value` : Valeur correspondante.

Le dataset complet peut être trouvé dans le fichier `EV_sales.csv`.

## Technologies et outils
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook

## Fonctions principales
`per_evo(df, powertrain, region, start_year, end_year, verbose=False)`  
Calcule la variation en pourcentage des ventes d’EV pour un pays et type de motorisation donnés entre deux années.

## Résultats clés
- En 2023, la France a connu une croissance de 47,6 % pour les BEV.  
- L’Allemagne a progressé de 10,6 %, tandis que l’Espagne a enregistré une croissance impressionnante de 72,7 %.  
- L’UE27 a une croissance moyenne de 33,3 %.  
- Les tendances montrent une adoption plus rapide des BEV en France et Espagne récemment, alors que l’Allemagne stagne légèrement.  

## Conclusions
- Les marchés français et espagnol se développent rapidement, mais l’Allemagne reste leader en nombre absolu de véhicules.  
- Les insights peuvent aider les acteurs de l’industrie à orienter les politiques de mobilité électrique et les prévisions de marché.  

## Améliorations futures
- Ajouter des projections pour 2030 en utilisant une méthode de prédiction simple (CAGR, modèle linéaire ou ML).  
- Ajouter une analyse des parts de marché par type de motorisation pour mieux visualiser les tendances.  
- Ajouter une version SQL du nettoyage et de l’agrégation pour montrer la maîtrise des bases de données relationnelles.

## Lien GitHub
(https://github.com/Andy-Raposo)
