# SIMRO STOCK 01/03/24

## Description
Ceci est un projet de test de compétences

## Prérequis
Installer python sur votre ordinateur, de préference la version `3.9.6`
Clonez le projet et ouvrez un terminal dans le repertoire du dossier

## Etape 1: création de l'environnement virtuel et installation des dépendences
### Créer un environnement virtuel
Windows `python -m venv venv`
Linux ou macos `python3 -m venv venv`

### Activer l'environnement
Windows `.\venv\Scripts\activate`
Linux ou macos `source venv/bin/activate`

### Installer les dépendences
`pip install -r requirements.txt`


## Etape 2: initialisation de la base de données et configuration
### Initialier la base de donnees
Windows
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Linux ou macos
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

### Configuration et lancement du projet
Windows `python manage.py runserver`
Linux ou macos `python3 manage.py runserver`

Ouvrez la page web du [server admin](http://127.0.0.1:8000/admin/), puis connectez-vous avec votre `compte administrateur` créé à l'étape précédente et créez un élément de la table `Marque`


## Etape 3: lancement du projet
Ouvrez la page web du [server api](http://127.0.0.1:8000/), commencez à effectuer des tets sur l'api
Si vous avez postman installé sur votre ordinateur, vous pouvez importer le fichiers `endpoints.json` et avoir accès aux appels preconfigurés