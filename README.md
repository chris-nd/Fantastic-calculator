# 🧮 Calculatrice Scientifique Python

Projet d'apprentissage - S1, Sem1-2 -> Sem3-4
Structures de données, NumPy et Mathématiques discrètes

## Description

Application CLI de calculatrice scientifique interactive pour les calculs basiques et avancés (suites mathématiques, la combinatoire et les opérations sur ensembles), avec historique, sauvegarde, visualisation graphique et export CSV.

## Fonctionnalités

### Opérations de base

- addition, soustraction, multiplication, division
- puissance, racine carrée
- Trigonométrie (sinus, cosinus, tangente)
- Conversion degrés en radians

### Suites mathématiques

- **Suite de Fibonacci** : F(n) = F(n-1) + F(n-2)
- **Suite arithmétique** : u(n) = u(0) + n×r
- **Suite géométrique** : u(n) = u(0) × q^n
- **Comparaison** de plusieurs suites simultanément

### Combinatoire

- **Factorielle** : n!
- **Arrangements** : A(n,k) = n!/(n-k)!
- **Combinaisons** : C(n,k) = n!/(k!×(n-k)!)
- **Triangle de Pascal** avec visualisation

### Ensembles mathématiques

- ∪ Union
- ∩ Intersection
- − Différence
- △ Différence symétrique
- ⊆ Test de sous-ensemble

### Analyse statistique

- Moyenne, médiane, écart-type
- Min, max, somme
- Détection de tendance (croissante/décroissante)
- Variance

### Visualisation

- Graphiques interactifs avec Matplotlib
- Comparaison de suites
- Visualisation du triangle de Pascal

### Export

- Export CSV des suites
- Export des analyses complètes
- Export du triangle de Pascal

### Historique

- Historique des calculs
- Sauvegarde dans un fichier

### Tests

- Tests unitaires complets

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip

### Étapes

```bash
# Cloner le projet
git clone <path_to_repository>

# Installer les dépendances
pip3 install numpy matplotlib pytest pytest-cov

# Ou avec requirements.txt
pip3 install -r requirements.txt
```

## 💻 Utilisation

### Lancer le programme

```bash
python3 calculatrice.py
```

### Menu principal

```markdown
==================================
    CALCULATRICE SCIENTIFIQUE
  ➕ ➖ ✖️ ➗ 𝔁ª √ Sinus Cosinus
==================================

Choisissez une opération :

1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Puissance (^)
6. Racine carrée (√)
7. Sinus (sin)
8. Cosinus (cos)
9. Tangente (tan)
10. Convertir degrés -> radians

============= SUITES =============

11. Suite de Fibonacci
12. Suite arithmétique
13. Suite géométrique
14. Comparer plusieurs suites

========== COMBINATOIRES ==========

15. Factorielle
16. Arrangements A(n,k)
17. Combinaisons C(n,k)
18. Triangle de Pascal

=========== ENSEMBLES ===========

19. Opérations sur les ensembles

============ ANALYSES ============

20. Analyser une suite personnalisée

========== EXPORT EN CSV ==========

21. Exporter la dernière suite en CSV

=========== HISTORIQUE ===========

22. Afficher l'historique
23. Sauvegarder l'historique
24. Effacer l'historique

0. Quitter

==================================
```

### Exemples d'utilisation

```python
# Addition
Choix : 1
Premier nombre : 5
Deuxième nombre : 3
5.0 + 3.0 = 8.0

# Racine carrée
Choix : 6
Entrez le nombre : 25
√25.0 = 5.0

# Sinus
Choix : 7
Entrez le nombre : 90
sin(90.0°) = 1.0
```

### Fibonacci

```python
Choix : 1
Combien de termes ? 15
Suite de Fibonacci (15 termes) :
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

### Suite arithmétique

```python
Choix : 2
Premier terme : 5
Raison : 3
Nombre de termes : 8
Suite arithmétique :
[5, 8, 11, 14, 17, 20, 23, 26]
Somme de la suite : 124.0
```

### Triangle de Pascal

```python
Choix : 8
Nombre de lignes : 5
Triangle de Pascal (5 lignes) :
Ligne 0 : [1]
Ligne 1 : [1, 1]
Ligne 2 : [1, 2, 1]
Ligne 3 : [1, 3, 3, 1]
Ligne 4 : [1, 4, 6, 4, 1]
```

### Opérations sur ensembles

```python
Choix : 9
Ensemble A : 1,2,3,4,5
Ensemble B : 4,5,6,7,8

Ensembles :
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

Opérations :
A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8}
A ∩ B = {4, 5}
A - B = {1, 2, 3}
B - A = {6, 7, 8}
```

## 🧪 Tests

### Lancer tous les tests

```bash
pytest test_calculatrice.py -v
```

### Avec couverture de code

```bash
pytest test_calculatrice.py --cov=calculatrice
```

### Exécuter les tests sur une unité spécificque

```bash
pytest test_calculatrice.py::test_addition -v
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

## Ressources

### Documentation

- [NumPy Docs](https://numpy.org/doc/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Python CSV](https://docs.python.org/3/library/csv.html)

### Mathématiques

- [OEIS - Suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci)
- [Triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal)
- [Combinatoire](https://fr.wikipedia.org/wiki/Analyse_combinatoire)

## Auteur

Chris Ndouassi - Projet d'apprentissage personnel

## Licence

Projet éducatif - Libre d'utilisation

## Remerciements

- Documentation Python officielle
- France université numérique
- Université Côte d'Azur
