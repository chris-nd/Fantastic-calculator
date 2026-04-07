import math

# =============== FONCTIONS ===============


def afficher_menu():
    """Affiche le menu"""
    print("\n" + "="*34)
    print("    CALCULATRICE SCIENTIFIQUE")
    print("  ➕ ➖ ✖️ ➗ 𝔁ª √ Sinus Cosinus")
    print("="*34)
    print("\nChoisissez une opération :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Puissance (^)")
    print("6. Racine carrée (√)")
    print("7. Sinus (sin)")
    print("8. Cosinus (cos)")
    print("9. Tangente (tan)")
    print("10. Convertir degrés -> radians")
    print("0. Quitter")
    print("="*34)


def addition(a, b):
    """Additionne deux nombres"""
    return a + b


def soustraction(a, b):
    """Soustrait b de a"""
    return a - b


def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b


def division(a, b):
    """Divise a par b"""
    if b == 0:
        return None
    return a / b


def puissance(a, b):
    """Calcule a puissance b"""
    return a ** b


def racine_carree(a):
    """Calcule la racine carrée de a"""
    if a < 0:
        return None
    return math.sqrt(a)


def sinus(angle_deg):
    """Calcule le sinus d'un angle en degrés"""
    angle_rad = math.radians(angle_deg)
    return math.sin(angle_rad)


def cosinus(angle_deg):
    """Calcule le cosinus d'un angle en degrés"""
    angle_rad = math.radians(angle_deg)
    return math.cos(angle_rad)


def tangente(angle_deg):
    """Calcule la tangente d'un angle en degrés"""
    angle_rad = math.radians(angle_deg)
    return math.tan(angle_rad)


def degres_vers_radians(angle_deg):
    """Convertit les degrés en radians"""
    return math.radians(angle_deg)


def demander_nombre(message):
    """Demande un nombre à l'utilisateur"""
    while True:
        try:
            return float(input(message))
        except ValueError:
            return "❌ Erreur: Veuillez entrer un nombre valide"


# ============= PROGRAMME PRINCIPAL ===============

def main():
    """Fonction principale du programme"""

    # Boucle principale
    while True:
        afficher_menu()

        choix = input("\nVotre choix : ")

        # Quitter le programme
        if choix == "0":
            print("\n👋 Au revoir 😉 !")
            break

        # Opération avec deux nombres
        if choix in ["1", "2", "3", "4", "5"]:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if choix == "1":
                resultat = addition(nombre1, nombre2)
                print(f"\n==> {nombre1} + {nombre2} = {resultat}")

            elif choix == "2":
                resultat = soustraction(nombre1, nombre2)
                print(f"\n==> {nombre1} - {nombre2} = {resultat}")

            elif choix == "3":
                resultat = multiplication(nombre1, nombre2)
                print(f"\n==> {nombre1} * {nombre2} = {resultat}")

            elif choix == "4":
                resultat = division(nombre1, nombre2)
                if resultat is None:
                    print("\n❌ Erreur : Division par zéro impossible")
                else:
                    print(f"\n==> {nombre1} / {nombre2} = {resultat}")

            elif choix == "5":
                resultat = puissance(nombre1, nombre2)
                print(f"\n==> {nombre1} ^ {nombre2} = {resultat}")

        # Opération avec un seul nombre
        elif choix in ["6", "7", "8", "9", "10"]:
            nombre = demander_nombre("Entrez le nombre : ")

            if choix == "6":
                resultat = racine_carree(nombre)
                if resultat is None:
                    print("❌ Erreur: La racine carrée d'un nombre négatif")
                else:
                    print(f"==> √{nombre} = {resultat}")

            elif choix == "7":
                resultat = sinus(nombre)
                print(f"==> sin({nombre}°) = {resultat}")

            elif choix == "8":
                resultat = cosinus(nombre)
                print(f"==> cos({nombre}°) = {resultat}")

            elif choix == "9":
                resultat = tangente(nombre)
                print(f"==> tan({nombre}°) = {resultat}")

            elif choix == "10":
                resultat = degres_vers_radians(nombre)
                print(f"==> {nombre}° = {resultat} radians")

        else:
            print("❌ Choix invalide ! Choisissez un nombre entre 0 et 10")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
