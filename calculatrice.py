import math

# Ma première calculatrice
print("==================================")
print("    CALCULATRICE SCIENTIFIQUE    ")
print("            ➕ ➖ ✖️ ➗           ")
print("==================================")

# Boucle principale

while True:
    # Afficher le menu
    print("\nChoisissez une opération :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Puissance (^)")
    print("6. Racine carrée (√)")
    print("7. Sinus (sin)")
    print("8. Cosinus (cos)")
    print("0. Quitter")

    # Demander un choix
    choix = input("\nVotre choix de (1-8) : ")

    # Quitter le programme
    if choix == "0":
        print("Au revoir!😉👋")
        break

    # Opération avec un seul nombre
    if choix in ["6", "7", "8"]:
        nombre = float(input("Entrez le nombre : "))

        if choix == "6":
            if nombre < 0:
                print("❌ Erreur : La racine carrée d'un nombre négatif.")
            else:
                resultat = math.sqrt(nombre)
                print(f"==> √{nombre} = {resultat}")
        elif choix == "7":
            angle_deg = nombre
            angle_radian = math.radians(angle_deg)
            resultat = math.sin(angle_radian)
            print(f"==> sin({angle_deg}°) = {resultat}")
        elif choix == "8":
            angle_deg = nombre
            angle_radian = math.radians(angle_deg)
            resultat = math.cos(angle_radian)
            print(f"==> cos({angle_deg}°) = {resultat}")

    # Opération avec deux nombres
    elif choix in ["1", "2", "3", "4", "5"]:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if choix == "1":
            resultat = nombre1 + nombre2
            print(f"==> {nombre1} + {nombre2} = {resultat}")
        elif choix == "2":
            resultat = nombre1 - nombre2
            print(f"==> {nombre1} - {nombre2} = {resultat}")
        elif choix == "3":
            resultat = nombre1 * nombre2
            print(f"==> {nombre1} * {nombre2} = {resultat}")
        elif choix == "4":
            if nombre2 == 0:
                print("❌ Erreur : Division par zéro.")
            else:
                resultat = nombre1 / nombre2
                print(f"==> {nombre1} / {nombre2} = {resultat}")
        elif choix == "5":
            resultat = nombre1 ** nombre2
            print(f"==> {nombre1} ^ {nombre2} = {resultat}")
    else:
        print("❌ Choix invalide !")