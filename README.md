# UE19-Lab-05 : GAFAM Stock Viewer

## Description

Ce projet est une application en Python 3 qui interroge l’API Alpha Vantage pour afficher le dernier cours des 5 actions GAFAM :  
Microsoft [finance:Microsoft Corporation], Apple [finance:Apple Inc.], Alphabet (Google) [finance:Alphabet Inc.], Amazon [finance:Amazon.com, Inc.] et Meta (Facebook) [finance:Meta Platforms, Inc.].  
Le script `app.py` utilise la librairie `requests` et peut être exécuté directement ou via un conteneur Docker.

## Fonctionnalités

- Appelle l’endpoint `GLOBAL_QUOTE` de l’API Alpha Vantage pour plusieurs symboles boursiers.
- Affiche dans le terminal les 5 valeurs GAFAM avec leur dernier prix en USD.
- Gère les erreurs simples (clé manquante, pas de données, problèmes réseau).

## Prérequis

- Python 3 installé  
- Ou Docker installé (pour l’exécution dans un conteneur)  
- Une clé API Alpha Vantage gratuite

## Installation sans Docker

1. Cloner le dépôt :

git clone https://github.com/<ton-user>/ue19-lab-05.git
cd ue19-lab-05

text

2. (Optionnel) Créer un environnement virtuel :

python -m venv .venv
source .venv/bin/activate # sous Windows : .venv\Scripts\activate

text

3. Installer les dépendances :

pip install -r requirements.txt

text

## Lancement sans Docker

python app.py

text

Le programme demande d'encoder la clé d'API pour Alpha Vantage.

Le programme affiche les 5 symboles GAFAM et leur dernier cours, par exemple :

Cours des 5 valeurs GAFAM (Alpha Vantage) :

    MSFT : xxx.xx USD

    AAPL : xxx.xx USD

    GOOGL : xxx.xx USD

    AMZN : xxx.xx USD

    META : xxx.xx USD

text

## Utilisation avec Docker

1. Construire l’image :

docker build -t ue19-lab-05 .

text

2. Lancer le conteneur avec la clé API :

docker run --rm -e ue19-lab-05

text

Le conteneur exécute `python app.py` et affiche les mêmes informations dans la sortie standard.

## Structure du projet

ue19-lab-05/
├── app.py # Script Python qui interroge l’API et affiche les cours GAFAM
├── requirements.txt # Dépendances (requests)
├── Dockerfile # Image Docker qui exécute app.py
└── README.md # Documentation du projet

text

## Remarques

- Le plan gratuit Alpha Vantage limite le nombre d’appels à 5 appels/min.
- Les données sont fournies à titre pédagogique et ne constituent pas un conseil en investissement.
