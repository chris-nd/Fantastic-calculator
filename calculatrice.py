from datetime import datetime
import math
import numpy as np
import matplotlib as plt

# =============== FONCTIONS ===============

# ========= HISTORIQUE DE CALCULS =========

historique = []


def ajouter_historique(operation, resultat):
    """Ajouter un calcul l'historique"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entree = {
        "heure": timestamp,
        "operation": operation,
        "resultat": resultat
    }
    historique.append(entree)


def afficher_historique():
    """Afficher tout l'historique des calculs"""
    if len(historique) == 0:
        print("\n📋 L'historique est vide")
        return

    print("\n" + "="*34)
    print("L'HISTORIQUE DES CALCULS \n")
    for i, calcul in enumerate(historique, 1):
        print(
            f"{i:>2d}. [{calcul["heure"]}] {calcul["operation"]} ==> {calcul["resultat"]}")
    print("="*34)


def sauvegarder_historique(nom_fichier="historique.txt"):
    """Sauvegarder l'historique dans un fichier"""
    try:
        with open(nom_fichier, "w", encoding="utf8") as fichier:
            fichier.write("HISTORIQUE DES CALCULS\n")
            fichier.write("="*34 + "\n\n")

            for i, calcul in enumerate(historique, 1):
                ligne = f"{i:>2d}. [{calcul["heure"]}] {calcul["operation"]} ==> {calcul["resultat"]}\n"
                fichier.write(ligne)

            print(f"\n✅ Historique sauvegardé dans '{nom_fichier}'")
    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde : {e}")


def afficher_menu():
    """Affiche le menu"""
    print("\n" + "="*34)
    print("    CALCULATRICE SCIENTIFIQUE")
    print("  ➕ ➖ ✖️ ➗ 𝔁ª √ Sinus Cosinus")
    print("="*34)
    print("\nChoisissez une opération :\n")
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
    print("\n" + "="*11 + " HISTORIQUE " + "="*11 + "\n")
    print("11. Afficher l'historique")
    print("12. Sauvegarder l'historique")
    print("13. Effacer l'historique")
    print("\n0. Quitter")
    print("\n" + "="*34)


# ========= FONCTIONS MATHÉMATIQUES BASIQUES =========

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


# ========= FONCTIONS TRIGONOMÉTRIQUES =========

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


# ========= FONCTIONS DE CONVERSION =========

def degres_vers_radians(angle_deg):
    """Convertit les degrés en radians"""
    return math.radians(angle_deg)


# =========== SUITES MATHÉMATIQUES ===========

def fibonacci(n: int):
    """Génère les n premiers termes de la suite de fibonacci"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    suite = [0, 1]

    for _ in range(2, n):
        suite.append(suite[-1] + suite[-2])

    return suite


def suite_arithmetique(premier_terme, raison, n):
    """
    Génère une suite arithmétique
    u(n) = u(0) + n * raison
    """
    if not (isinstance(premier_terme, (int, float)) and
            isinstance(raison, (int, float)) and
            isinstance(n, (int, float))):
        raise TypeError("Argument incorrect")

    return [premier_terme + terme * raison for terme in range(n)]


def suite_geometrique(premier_terme, raison, n):
    """
    Génère une suite geométrique
    u(n) = u(0) * raison^n
    """
    if not (isinstance(premier_terme, (int, float)) and
            isinstance(raison, (int, float)) and
            isinstance(n, int)):
        raise TypeError("Argument incorrect")

    return [premier_terme * (raison ** terme) for terme in range(n)]


def somme_suite_arithmetique(premier_terme, dernier_terme, n):
    """
    Calcul la somme d'une suite arithmétique
    S = n * (premier + dernier) / 2
    """
    if not (isinstance(premier_terme, (int, float)) and
            isinstance(dernier_terme, (int, float)) and
            isinstance(n, (int, float))):
        raise TypeError("Argument incorrect")

    return n * (premier_terme + dernier_terme) / 2


def somme_suite_geometrique(premier_terme, raison, n):
    """
    Calcul la somme d'une suite arithmétique
    S = premier_terme * (1 - raine^n) / (1 - raison)
    """
    if not (isinstance(premier_terme, (int, float)) and
            isinstance(raison, (int, float)) and
            isinstance(n, (int, float))):
        raise TypeError("Argument incorrect")

    if raison == 1:
        return premier_terme * n

    return premier_terme * (1 - raison**n) / (1 - raison)


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

        # Gestion de l'historique
        if choix == "11":
            afficher_historique()
            continue

        elif choix == "12":
            sauvegarder_historique()
            continue

        elif choix == "13":
            historique.clear()
            print("\n🗑 Historique effacé")
            continue

        # Opération avec deux nombres
        if choix in ["1", "2", "3", "4", "5"]:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if choix == "1":
                resultat = addition(nombre1, nombre2)
                operation = f"{nombre1} + {nombre2}"
                print(f"\n==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "2":
                resultat = soustraction(nombre1, nombre2)
                operation = f"{nombre1} - {nombre2}"
                print(f"\n==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "3":
                resultat = multiplication(nombre1, nombre2)
                operation = f"{nombre1} * {nombre2}"
                print(f"\n==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "4":
                resultat = division(nombre1, nombre2)
                if resultat is None:
                    print("\n❌ Erreur : Division par zéro impossible")
                else:
                    operation = f"{nombre1} / {nombre2}"
                    print(f"\n==> {operation} = {resultat}")
                    ajouter_historique(operation, resultat)

            elif choix == "5":
                resultat = puissance(nombre1, nombre2)
                operation = f"{nombre1} ^ {nombre2}"
                print(f"\n==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

        # Opération avec un seul nombre
        elif choix in ["6", "7", "8", "9", "10"]:
            nombre = demander_nombre("Entrez le nombre : ")

            if choix == "6":
                resultat = racine_carree(nombre)
                if resultat is None:
                    print("❌ Erreur: La racine carrée d'un nombre négatif")
                else:
                    operation = f"√{nombre}"
                    print(f"==> {operation} = {resultat}")
                    ajouter_historique(operation, resultat)

            elif choix == "7":
                resultat = sinus(nombre)
                operation = f"sin({nombre}°)"
                print(f"==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "8":
                resultat = cosinus(nombre)
                operation = f"cos({nombre}°)"
                print(f"==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "9":
                resultat = tangente(nombre)
                operation = f"tan({nombre}°)"
                print(f"==> {operation} = {resultat}")
                ajouter_historique(operation, resultat)

            elif choix == "10":
                resultat = degres_vers_radians(nombre)
                operation = f"{nombre}°"
                print(f"==> {operation} = {resultat} radians")
                ajouter_historique(operation, resultat)

        else:
            print("❌ Choix invalide ! Choisissez un nombre entre 0 et 13")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
