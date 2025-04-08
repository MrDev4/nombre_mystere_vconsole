# nombre_mystere_vconsole
Projet Dev Team

Objectif

Développer un jeu interactif dans lequel l’utilisateur doit deviner un nombre mystère généré aléatoirement par l’ordinateur. Le jeu sera jouable en mode solo et en mode groupe, avec des niveaux de difficulté et un nombre de vies paramétrables. Ce projet est collaboratif, avec une répartition claire des tâches entre les membres du groupe.


---

Fonctionnalités Attendues

1. Menu Principal

Le menu de démarrage doit proposer les options suivantes :

Jouer seul : Lancer une partie solo (choix du pseudo, de la difficulté et du nombre de vies).

Jouer en groupe : Lancer une partie multijoueur avec alternance des tours.

Présentation du jeu : Afficher les règles détaillées du jeu.

Fermer l'application : Quitter proprement le programme.


2. Mode Solo

Saisie d’un pseudo joueur.

Choix du niveau de difficulté :

Facile : pas supérieur à 5 vies et le nombre de doit être sur une limite raisonnable.

Moyen : pas supérieur à 8 vies et le nombre de doit être sur une limite assez élargie.

Difficile : pas supérieur à 10 vies et le nombre de doit être sur une limite élargie.


L’ordinateur génère un nombre aléatoire entre 1 et 100.

Le joueur entre une proposition, le système indique si le nombre mystère est plus grand ou plus petit.

La partie se termine si le joueur trouve le nombre ou épuise ses vies.


3. Mode Groupe

Définition du nombre de joueurs et saisie des pseudos.

Choix collectif du niveau de difficulté (vies identiques pour tous).

Alternance automatique des tours entre joueurs.

Le joueur qui trouve le nombre gagne la partie.

Si tous les joueurs épuisent leurs vies, la partie est terminée.


4. Présentation du Jeu

Cette option affiche :

Les règles du jeu.

Le détail des niveaux de difficulté.

Le fonctionnement général des deux modes (solo/groupe).


5. Fermeture de l’Application

L’option “Fermer l’application” quitte proprement le programme.



Technologies à Utiliser

Langages : Python

Interface : Basée sur le terminal / console.
