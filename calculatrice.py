from datetime import datetime
import math
import numpy as np
import matplotlib.pyplot as plt

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
    print("\n" + "="*13 + " SUITES " + "="*13 + "\n")
    print("14. Suite de Fibonacci")
    print("15. Suite arithmétique")
    print("16. Suite géométrique")
    print("17. Comparer plusieurs suites")
    print("\n" + "="*10 + " COMBINATOIRES " + "="*10 + "\n")
    print("18. Factorielle")
    print("19. Arrangements A(n,k)")
    print("20. Combinaisons C(n,k)")
    print("21. Triangle de Pascal")
    print("\n" + "="*11 + " ENSEMBLES " + "="*11 + "\n")
    print("22. Opérations sur les ensembles")
    print("\n" + "="*12 + " ANALYSES " + "="*12 + "\n")
    print("23. Analyser une suite personnalisée")
    print("\n" + "="*11 + " HISTORIQUE " + "="*11 + "\n")
    print("24. Afficher l'historique")
    print("25. Sauvegarder l'historique")
    print("26. Effacer l'historique")
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


# ============= COMBINATOIRE ===============

def factorielle(n):
    """Calcule de n!"""
    if n < 0:
        return None
    return math.factorial(n)


def arrangement(n, k):
    """
    Calcule A(n,k) = n! / (n-k)!
    Nombre d'arrangement de k éléments parmi n
    """
    if k > n or n < 0 or k < 0:
        return None
    return math.factorial(n) // math.factorial(n - k)


def combinaison(n, k):
    """
    calcule C(n,k) = n! / (k! * (n-k)!)
    Nombre de combinaison de k éléments parmi n
    """
    if k > n or n < 0 or k < 0:
        return None
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def triangle_pascal(n):
    """
    Génère les n premières lignes du triangle de Pascal
    """
    triangle = []
    for ligne in range(n):
        ligne_actuelle = [combinaison(ligne, k) for k in range(ligne + 1)]
        triangle.append(ligne_actuelle)
    return triangle


# =========== ENSEMBLES MATHÉMATIQUES ===========

def operatons_ensembles(ensemble_a, ensemble_b):
    """
    Effectue toutes les opérations sur deux ensembles
    """
    a = set(ensemble_a)
    b = set(ensemble_b)

    return {
        "union": a | b,
        "intersection": a & b,
        "différence_a_b": a - b,
        "différence_b_a": b - a,
        "différence_symétrique": a ^ b,
        "a_sous_ensemble_b": a.issubset(b),
        "b_sous_ensemble_a": b.issubset(a),
        "disjoints": a.isdisjoint(b)
    }

def demander_nombre(message):
    """Demande un nombre à l'utilisateur"""
    while True:
        try:
            return float(input(message))
        except ValueError:
            return "❌ Erreur: Veuillez entrer un nombre valide"


# ============= VISUALISATION ===============

def visualiser_suite(suite, titre="Suite mathématique"):
    """
    Visualise une suite avec matplotlib
    """
    n = len(suite)
    x = np.array(range(n))
    y = np.array(suite)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, "b-o", linewidth=2, makersize=8)
    plt.xlabel("n (index)", fontsize=12)
    plt.ylabel("U(n)", fontsize=12)
    plt.title(titre, fontsize=14, fontweight="bold")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def comparer_suites(suites_dict):
    """
    Compare plusieurs suites sur le même graphique
    suites_dict = {"nom1": suite1, "nom2": suite2, ...}
    """
    plt.figure(figsize=(12, 7))

    for nom, suite in suites_dict.items():
        n = len(suite)
        x = np.array(range(n))
        y = np.array(suite)
        plt.plot(x, y, '-o', label=nom, linewidth=2, makersize=6)

    plt.xlabel("n (index)", fontsize=12)
    plt.xlabel("U(n)", fontsize=12)
    plt.title("Comparaison de suites", fontsize=14, fontweight="bold")
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def visualiser_triangle_pascal(n):
    """
    Visualise le triangle de Pascal
    """
    triangle = triangle_pascal(n)

    plt.figure(figsize=(10, 8))

    for i, ligne in enumerate(triangle):
        y_pos = n - i -1
        for j, valeur in enumerate(ligne):
            x_pos = j - len(ligne) / 2 + 0.5

            # Taille du cercle proportionnelle à la valeur
            taille = min(valeur * 50, 500)

            plt.scatter(x_pos, y_pos, s=taille, c="blue", alpha=0.6)
            plt.text(x_pos, y_pos, str(valeur),
                     ha="center", va="center",
                     fontsize=10, fontweight="bold")

    plt.title(f"Triangle de Pascal ({n} lignes)",
              fontsize=14, fonweight="bold")
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ============= ANALYSE DE SUITES ===============

def analyse_suite(suite):
    """
    Analyse une suite moyenne, variance, tendance
    """
    arr = np.aaray(suite)

    analyse = {
        "longueur": len(suite),
        "min": np.min(arr),
        "max": np.max(arr),
        "moyenne": np.mean(arr),
        "mediane": np.median(arr),
        "ecart_type": np.std(arr),
        "variance": np.var(arr),
        "somme": np.sum(arr)
    }

    # Tendance (coissance, décroissnate, constante)
    differences= np.diff(arr)

    if np.all(differences > 0):
        analyse["tendance"] = "Strictement croissante"
    elif np.all(differences < 0):
        analyse["tendance"] = "Strictement décroissante"
    elif np.all(differences >= 0):
        analyse["tendance"] = "Croissante"
    elif np.all(differences <= 0):
        analyse["tendance"] = "Décroissante"
    else:
        analyse["tendance"] = "Ni croissante ni décroissante"

    return analyse 


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
