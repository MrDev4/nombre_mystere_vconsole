import random

def mode_groupe(joueurs, niveau_difficulte, vies):
    
    """
    Fonction pour gérer le mode groupe du jeu de devinette.
    
    Paramètres:
    joueurs (list): Liste des pseudos des joueurs.
    niveau_difficulte (str): Niveau de difficulté choisi (Facile, Moyen, Difficile).
    vies (int): Nombre de vies attribuées à chaque joueur.
    
    """
    
    # Générer le nombre mystère entre 1 et 100
    nombre_mystere = random.randint(1, 100)
    print(f"Le nombre mystère a été généré. Il est entre 1 et 100.")

    # Initialiser les vies et les scores pour chaque joueur
    vies_restantes = {joueur: vies for joueur in joueurs}
    scores = {joueur: 0 for joueur in joueurs}
    historique_tentatives = {joueur: [] for joueur in joueurs}
    
    # Initialiser le compteur de tours
    tour = 0
    
    # Boucle principale du jeu
    while True:
        # Déterminer le joueur actuel
        joueur_actuel = joueurs[tour % len(joueurs)]
        print(f"\nC'est au tour de {joueur_actuel}. Il lui reste {vies_restantes[joueur_actuel]} vies.")
        
        # Afficher l'historique des tentatives
        print(f"Historique des tentatives de {joueur_actuel}: {historique_tentatives[joueur_actuel]}")
        
        # Demander une proposition au joueur
        try:
            proposition = int(input(f"{joueur_actuel}, entrez votre proposition (entre 1 et 100): "))
            
            # Valider la proposition
            if proposition < 1 or proposition > 100:
                print("Erreur: Veuillez entrer un nombre entre 1 et 100.")
                continue
            
            # Ajouter la tentative à l'historique
            historique_tentatives[joueur_actuel].append(proposition)
            
            # Vérifier la proposition du joueur
            if proposition == nombre_mystere:
                print(f"Félicitations {joueur_actuel}! Vous avez trouvé le nombre mystère {nombre_mystere}.")
                scores[joueur_actuel] += 1
                break
            elif proposition < nombre_mystere:
                print("Le nombre mystère est plus grand.")
            else:
                print("Le nombre mystère est plus petit.")
            
            # Décrémenter les vies du joueur
            vies_restantes[joueur_actuel] -= 1
            
            # Vérifier si le joueur a épuisé ses vies
            if vies_restantes[joueur_actuel] == 0:
                print(f"{joueur_actuel} a épuisé toutes ses vies.")
                joueurs.remove(joueur_actuel)
        
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")
        
        # Vérifier si tous les joueurs ont épuisé leurs vies
        if not joueurs:
            print("Tous les joueurs ont épuisé leurs vies. La partie est terminée.")
            break
        
        # Passer au joueur suivant
        tour += 1
    
    # Afficher les scores finaux
    print("\nScores finaux:")
    for joueur, score in scores.items():
        print(f"{joueur}: {score} points")

# Exemple d'utilisation
joueurs = ["Alice", "Bob", "Charlie"]
niveau_difficulte = "Moyen"
vies = 8

mode_groupe(joueurs, niveau_difficulte, vies)
