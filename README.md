# Nom du Projet Django

## Description
 Django-app-analyzer permet d'importer un fichier CSV, d'afficher un aperçu des données, d'analyser statistiquement les données, et de les visualiser sous forme de graphiques.

## Fonctionnalités
- **Importer un fichier CSV** : Permet de télécharger un fichier CSV pour l'analyser.
- **Aperçu des données** : Affiche un aperçu des données du fichier CSV.
- **Analyse statistique** : Calcule les statistiques (moyenne, médiane, etc.) pour une colonne sélectionnée.
- **Visualisation** : Permet de visualiser les données sous forme de graphiques(histogram and heatmap).

## Prérequis
- **pip** : Gestionnaire de paquets Python (installé avec Python).
- Python 3.x
- Django 3.x
- Toutes les dépendances sont listées dans le fichier `requirements.txt`.

## Installation

1. Clonez le repository sur votre machine locale :
    ```bash
    git clone https://github.com/99683/Django-app-analyzer.git
    ```

2. Accédez au dossier du projet :
    ```bash
    cd Django-app-analyzer
    ```

3. Créez un environnement virtuel (recommandé) :
    ```bash
    python3 -m venv venv
    ```

4. Activez l'environnement virtuel :
    - Sur Windows :
      ```bash
      venv\Scripts\activate
  
5. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

6. Effectuez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

7. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

8. Accédez à l'application en ouvrant un navigateur et en allant à l'adresse suivante :
    ```
    http://127.0.0.1:8000/
    ```

## Utilisation

1. **Importer un fichier CSV** : Accédez à la page "Importer un fichier CSV", téléchargez un fichier CSV.
2. **Aperçu des données** : Après l'importation, un aperçu des premières lignes et des colonnes du fichier sera affiché. (overview)
3. **Analyse statistique** : Sélectionnez une colonne pour voir ses statistiques (moyenne, écart-type, etc.).
4. **Visualisation** : Visualisez les données sous forme de graphiques et de heatmaps.

## Contributions
Si vous souhaitez contribuer à ce projet, vous pouvez faire un fork du repository et soumettre des pull requests.

## License
Ce projet est sous licence MIT.


### Explications des sections :
- **Description** : Donne une brève introduction sur l'objectif du projet.
- **Fonctionnalités** : Liste les fonctionnalités principales de l'application.
- **Prérequis** : Indique les outils nécessaires pour exécuter le projet.
- **Installation** : Explique comment cloner le projet, installer les dépendances et appliquer les migrations.
- **Utilisation** : Détaille les étapes pour lancer l'application localement.
- **Contribuer** : Décrit comment d'autres développeurs peuvent contribuer à l'application.
- **Licence** : Mentionne sous quelle licence le projet est distribué.



