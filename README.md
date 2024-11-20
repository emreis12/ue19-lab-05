# Application de Citations - UE19 Lab 05

## Description
Cette application Python interroge l'API ZenQuotes pour récupérer une citation aléatoire et l'afficher dans la console. L'application utilise la bibliothèque `requests` pour effectuer des requêtes HTTP.

Le projet inclut également un `Dockerfile` pour exécuter l'application dans un conteneur Docker, ainsi qu'un fichier `README.md` pour expliquer comment installer et utiliser l'application.

## Fonctionnalités
- Récupère une citation aléatoire avec son auteur depuis l'API ZenQuotes.
- Affiche la citation dans la console.

## Prérequis
- Python 3.x
- `pip` pour installer les dépendances

## Installation
1. Clonez le repository sur votre machine : ```git clone https://github.com/emreis12/ue19-lab-05.git ```
2. Installez les dépendances avec `pip` ```pip install -r requirements.txt```

## Lancer l'application
Pour exécuter l'application, utilisez la commande suivante : ```python app.py```


## Utilisation avec Docker

- Construire l'image Docker : ```docker build -t ue19-lab-05 .```
- Lancer l'application dans un conteneur Docker : ```docker run --rm ue19-lab-05```

## Licence
Ce projet n'est soumis à aucune licence. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer à votre convenance.
