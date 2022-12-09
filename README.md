<h1>Documentation BACK Fantazoo</h1>


<!-- Cours
    
    Utilisation de l’environnement virtuel et commandes associées :
        1. Création de l’environnement virtuel: py –m venv path/venv
        2. Utilisation/Activation du venv: source path/venv/Scripts/activate
        3. Installation de librairie: pip install <lib_name>
        4. Installation Django: pip install Django
        5. Copie des librairies dans un fichier: pip freeze> requirements.txt
        6. Installation des librairies depuis un fichier: pip install -r requirements.txt
        7. Fermeture/Désactivation du venv: deactivate -->
<h5>Administration</h5>
    Login Administrateur : admin2
    Mot de passe Administrateur : admin2

Se placer dans le répertoire du projet ProjetFantazoo
# Pour lancer le Projet
       
    1)  ProjetFantazoo/back
    2)  source path/venv/Scripts/activate
    3)  cd back
    4)  pip install -r requirements.txt
    5)  python3 manage.py makemigrations fantazoo
    6)  python3 manage.py migrate
    7)  python3 manage.py runserver
        
<h4>Le projet run sur le port  http://127.0.0.1:8000/ (localhost:8000)</h4>


    api des CRUD:
        Animaux         http://localhost:8000/api/animals/
        Utilisateurs    http://localhost:8000/api/users/
        Paniers         http://localhost:8000/api/shoppingcarts/
        Commandes       http://localhost:8000/api/orders/

