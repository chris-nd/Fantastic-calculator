# Ma première calculatrice
print("==================================")
print("    CALCULATRICE SCIENTIFIQUE    ")
print("            ➕ ➖ ✖️ ➗           ")
print("==================================")

# Afficher le menu
print("Choisissez une opération :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Puissance (^)")

# Demander un choix
choix = input("\nVotre choix de (1-5) : ")

# Demander les nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calculer selon le choix
if choix == "1":
    resultat = nombre1 + nombre2
    opération = "+"
elif choix == "2":
    resultat = nombre1 - nombre2
    opération = "-"
elif choix == "3":
    resultat = nombre1 * nombre2
    opération = "*"
elif choix == "4":
    resultat = nombre1 / nombre2
    opération = "/"
elif choix == "5":
    resultat = nombre1 ** nombre2
    opération = "^"
else:
    print("Choix invalide !")
    resultat = None
    opération = None

# Afficher le résultat
if resultat is not None:
    print("\nRésultats :")
    print(f"==> {nombre1} {opération} {nombre2} = {resultat}")