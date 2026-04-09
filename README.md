# 🧮 Calculatrice Scientifique Python

Projet d'apprentissage - Semestre 1, Semaine 1-2

## Description

Calculatrice scientifique en ligne de commande avec historique et sauvegarde.

## Fonctionnalités

- ➕ Opérations de base (addition, soustraction, multiplication, division)
- 🔢 Opérations avancées (puissance, racine carrée)
- 📐 Trigonométrie (sinus, cosinus, tangente)
- 🔄 Conversion degrés en radians
- 📋 Historique des calculs
- 💾 Sauvegarde dans un fichier
- 🧪 Tests unitaires complets

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip

### Étapes

```bash
# Cloner le projet
git clone <path_to_repository>

# Installer les dépendances
pip3 install pytest pytest-cov
```

## 💻 Utilisation

### Lancer la calculatrice

```bash
python3 calculatrice_v3.py
```

### Menu principal

```markdown
1. Addition (+)
2. Soustraction (-)
3. Multiplication (×)
4. Division (÷)
5. Puissance (^)
6. Racine carrée (√)
7. Sinus (sin)
8. Cosinus (cos)
9. Tangente (tan)
10. Convertir degrés → radians
11. Afficher l'historique
12. Sauvegarder l'historique
13. Effacer l'historique
0. QUITTER
```

### Exemples

```python
# Addition
Choix : 1
Premier nombre : 5
Deuxième nombre : 3
✅ 5.0 + 3.0 = 8.0

# Racine carrée
Choix : 6
Entrez le nombre : 25
✅ √25.0 = 5.0

# Sinus
Choix : 7
Entrez le nombre : 90
✅ sin(90.0°) = 1.0
```

## 🧪 Tests

### Lancer les tests

```bash
# Exécuter tous les tests
pytest test_calculatrice.py -v

# Exécuter les tests avec couverture
pytest test_calculatrice.py --cov=calculatrice

# Exécuter les tests sur une unité spécificque
pytest test_calculatrice.py::test_addition -v
```

### Résultats attendus

```bash
test_calculatrice.py::test_addition PASSED
test_calculatrice.py::test_soustraction PASSED
test_calculatrice.py::test_multiplication PASSED
test_calculatrice.py::test_division PASSED
...
=================== 15 passed in 0.05s ===================
```

## Structure du projet

```bash
calculatrice-s1/
│
├── calculatrice.py        # V3
├── test_calculatrice.py   # Tests unitaires
├── historique.txt         # Historique sauvegardé
├── README.md              # Documentation
└── .gitignore             # Fichiers à ignorer par Git
```

## Améliorations futures

- Interface graphique (GUI avec tkinter)
- Plus de fonctions (logarithmes, exponentielles)
- Graphiques de fonctions
- Mode scientifique vs simple
- Support des calculs matriciels
- Export en CSV/Excel
- Calcul d'expressions complexes ("2 + 3 * 4")

## Auteur

Chris Ndouassi - Projet d'apprentissage personnel

## Licence

Projet éducatif - Libre d'utilisation

## Remerciements

- Documentation Python officielle
- France université numérique
- Université Côte d'Azur
