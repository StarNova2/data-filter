# Data Filter - Projet Python
Petit programme en Python qui permet de **charger**, **afficher**, **sauvegarder**, **trier**, **filtrer**, **stater** des données au format **CSV** ou **JSON**.

## 1. Prérequis
- Python installer sur la machine (vérif dans le terminal avec: python --version)

## 2. Structure du projet

data-filter/
    code files/
        main.py
        save_load.py
        filter.py
        sorting.py
        stats.py
    data/
        XXX.json
        XXX.csv
    README.md
    Sujet.pdf

## 3. Lancement du programme

être dans le bon dossier, dans notre cas

cd data-filter/code files/

et executer le programme avec :

python main.py

## 4. Utilisation du menu

Choix 1 : Load Data, bien penser à mettre le nom et l'extension du fichier (le chemin de data/ est déjà gérer avec la fonciton add_path)

Choix 2 : Affiche le nombre d’éléments dans la liste

choix 3 : Affiche toutes les lignes (j'ai pas eu de json à 10k lignes pour test de tout casser)

choix 4 : il va sauvegarder ta liste (si t'en as une, sinon t'auras un message d'erreur) dans le format que tu veux, tu lui donnes un nom et tu choisis l'extension,
          ça va rajouter l'extension directement après le nom choisi et enregistrer le fichier dans le dossier data

choix 5 : Finito pipo on quitte le programme

## 5. Fonctionnement global du code

- Le programme lit les fichiers CSV et JSON avec les fonctions de save_load.py
- Les données sont converties et manipulées en python sous la forme d'une liste de dictionnaire qui s'appellera data_list
- main.py c'est le menu utilisateur avec les inputs et les prints, il appelle les fonctions en fonction de tes choix.