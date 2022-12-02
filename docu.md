Lancement de l'environnement


Cours
    
    Utilisation de l’environnement virtuel et commandes associées :
        1. Création de l’environnement virtuel: py –m venv path/venv
        2. Utilisation/Activation du venv: source path/venv/Scripts/activate
        3. Installation de librairie: pip install <lib_name>
        4. Installation Django: pip install Django
        5. Copie des librairies dans un fichier: pip freeze> requirements.txt
        6. Installation des librairies depuis un fichier: pip install -r requirements.txt
        7. Fermeture/Désactivation du venv: deactivate

Se placer dans le répertoire du projet
source path/venv/Scripts/activate

python3 manage.py makemigrations fantazoo
 python3 manage.py migrate

 python3 manage.py runserver fantazoo