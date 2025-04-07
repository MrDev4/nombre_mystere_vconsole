import random

def mode_solo():
    print("Bienvenue dans le mode solo !")
    pseudo = input("Entrez votre pseudo joueur : ")

    # Choix du niveau de difficulté
    print("\nChoisissez un niveau de difficulté :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    choix = int(input("Votre choix (1, 2 ou 3) : "))

    if choix == 1:
        vies = 5
        limite = 50  # Limite raisonnable
        print("\nMode Facile sélectionné. Vous avez 5 vies et la limite est 50.")
    elif choix == 2:
        vies = 8
        limite = 75  # Limite élargie
        print("\nMode Moyen sélectionné. Vous avez 8 vies et la limite est 75.")
    elif choix == 3:
        vies = 10
        limite = 100  # Limite large
        print("\nMode Difficile sélectionné. Vous avez 10 vies et la limite est 100.")
    else:
        print("Choix invalide. Par défaut, le mode Facile est sélectionné.")
        vies = 5
        limite = 50

    # Générer un nombre aléatoire
    nombre_mystere = random.randint(1, limite)
    print("\nUn nombre mystère a été généré entre 1 et", limite)

    # Lancer le jeu
    while vies > 0:
        try:
            proposition = int(input(f"\n{pseudo}, entrez votre proposition : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if proposition == nombre_mystere:
            print(f"Félicitations, {pseudo} ! Vous avez trouvé le nombre mystère : {nombre_mystere} 🎉")
            break
        elif proposition < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")

        vies -= 1
        print(f"Il vous reste {vies} vies.")

    if vies == 0:
        print(f"Dommage, {pseudo}. Vous avez épuisé toutes vos vies. Le nombre mystère était {nombre_mystere}. 😢")
        print("tu peux toute fois essayer une prochaine fois")

if __name__ == "__main__":
    mode_solo()