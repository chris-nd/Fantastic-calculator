# Ma première calculatrice

print("==================================")
print("    CALCULATRICE SCIENTIFIQUE    ")
print("            ➕ ➖ ✖️ ➗           ")
print("==================================")

print("Bienvenue")

# Demander le premier nombre
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calculer
addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2
division = nombre1 / nombre2

# Afficher les résultats
print("\nRésultats :")
print(f"==> {nombre1} + {nombre2} = {addition}")
print(f"==> {nombre1} - {nombre2} = {soustraction}")
print(f"==> {nombre1} * {nombre2} = {multiplication}")
print(f"==> {nombre1} / {nombre2} = {division}")