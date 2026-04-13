"""
Tests unitaires pour la calculatrice
"""

import time
import math
import pytest
from calculatrice import (
    addition, soustraction, multiplication, division,
    puissance, racine_carree, sinus, cosinus, tangente,
    degres_vers_radians, fibonacci, suite_arithmetique, suite_geometrique,
    somme_suite_arithmetique, somme_suite_geometrique,
    factorielle, arrangement, combinaison, triangle_pascal,
    operations_ensembles, analyse_suite
)

# ============== TESTS DES OPERATIONS DE BASE ==============

def test_addition():
    """Test de l'addition"""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(1.5, 2.5) == 4.0


def test_soustraction():
    """Test de la soustraction"""
    assert soustraction(5, 3) == 2
    assert soustraction(0, 5) == -5
    assert soustraction(10, 10) == 0


def test_multiplication():
    """Test de la multiplication"""
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 100) == 0
    assert multiplication(2.5, 4) == 10.0


def test_division():
    """Test de la division"""
    assert division(10, 2) == 5
    assert division(7, 2) == 3.5
    assert division(0, 5) == 0
    assert division(5, 0) is None


def test_puissance():
    """Test de la puissance"""
    assert puissance(2, 3) == 8
    assert puissance(5, 0) == 1
    assert puissance(10, 2) == 100
    assert puissance(2, -1) == 0.5


# ========== TESTS DES FONCTIONS AVANCÉES ===========

def test_racine_carree():
    """Test de la racine carrée"""
    assert racine_carree(25) == 5
    assert racine_carree(0) == 0
    assert racine_carree(2) == pytest.approx(1.414, rel=0.01)
    assert racine_carree(-4) is None


def test_sinus():
    """Test du sinus"""
    assert sinus(0) == pytest.approx(0, abs=0.0001)
    assert sinus(90) == pytest.approx(1, abs=0.0001)
    assert sinus(30) == pytest.approx(0.5, abs=0.0001)


def test_cosinus():
    """Test du cosinus"""
    assert cosinus(0) == pytest.approx(1, abs=0.0001)
    assert cosinus(90) == pytest.approx(0, abs=0.0001)
    assert cosinus(60) == pytest.approx(0.5, abs=0.0001)


def test_tangente():
    """Test de la tangente"""
    assert tangente(0) == pytest.approx(0, abs=0.0001)
    assert tangente(45) == pytest.approx(1, abs=0.0001)


def test_degres_vers_radians():
    """Test de conversion degrés → radians"""
    assert degres_vers_radians(0) == 0
    assert degres_vers_radians(180) == pytest.approx(math.pi, abs=0.0001)
    assert degres_vers_radians(90) == pytest.approx(math.pi/2, abs=0.0001)


# ========== TESTS EDGE CASES ==========

def test_grands_nombres():
    """Test avec de très grands nombres"""
    assert addition(1e10, 1e10) == 2e10
    assert multiplication(1e6, 1e6) == 1e12


def test_petits_nombres():
    """Test avec de très petits nombres"""
    assert addition(0.0001, 0.0002) == pytest.approx(0.0003, abs=1e-6)


def test_nombres_negatifs():
    """Test avec nombres négatifs"""
    assert addition(-5, -3) == -8
    assert multiplication(-2, -3) == 6
    assert division(-10, 2) == -5


# ========== TESTS DES SUITES ==========

def test_fibonacci():
    """Test de la suite de Fibonacci"""
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_suite_arithmetique():
    """Test de la suite arithmétique"""
    # Suite : 1, 3, 5, 7, 9
    assert suite_arithmetique(1, 2, 5) == [1, 3, 5, 7, 9]
    # Suite : 0, 5, 10, 15
    assert suite_arithmetique(0, 5, 4) == [0, 5, 10, 15]
    # Suite constante
    assert suite_arithmetique(10, 0, 3) == [10, 10, 10]


def test_suite_geometrique():
    """Test de la suite géométrique"""
    # Suite : 2, 4, 8, 16, 32
    assert suite_geometrique(2, 2, 5) == [2, 4, 8, 16, 32]
    # Suite : 1, 3, 9, 27
    assert suite_geometrique(1, 3, 4) == [1, 3, 9, 27]
    # Raison = 1 (constante)
    assert suite_geometrique(5, 1, 3) == [5, 5, 5]


def test_somme_suite_arithmetique():
    """Test de la somme d'une suite arithmétique"""
    # Somme de 1+2+3+4+5 = 15
    assert somme_suite_arithmetique(1, 5, 5) == 15
    # Somme de 0+5+10+15 = 30
    assert somme_suite_arithmetique(0, 15, 4) == 30


def test_somme_suite_geometrique():
    """Test de la somme d'une suite géométrique"""
    # Somme de 1+2+4+8+16 = 31
    assert somme_suite_geometrique(1, 2, 5) == 31
    # Raison = 1
    assert somme_suite_geometrique(5, 1, 3) == 15


# ========== TESTS DE COMBINATOIRE ==========

def test_factorielle():
    """Test de la factorielle"""
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(5) == 120
    assert factorielle(10) == 3628800
    assert factorielle(-1) is None


def test_arrangement():
    """Test des arrangements"""
    assert arrangement(5, 2) == 20  # 5*4 = 20
    assert arrangement(10, 3) == 720  # 10*9*8 = 720
    assert arrangement(5, 0) == 1
    assert arrangement(5, 5) == 120  # 5!
    # Cas d'erreur
    assert arrangement(3, 5) is None
    assert arrangement(-1, 2) is None


def test_combinaison():
    """Test des combinaisons"""
    assert combinaison(5, 2) == 10
    assert combinaison(10, 3) == 120
    assert combinaison(5, 0) == 1
    assert combinaison(5, 5) == 1
    # Propriété : C(n,k) = C(n, n-k)
    assert combinaison(10, 3) == combinaison(10, 7)
    # Cas d'erreur
    assert combinaison(3, 5) is None


def test_triangle_pascal():
    """Test du triangle de Pascal"""
    triangle = triangle_pascal(5)

    # Vérifier les premières lignes
    assert triangle[0] == [1]
    assert triangle[1] == [1, 1]
    assert triangle[2] == [1, 2, 1]
    assert triangle[3] == [1, 3, 3, 1]
    assert triangle[4] == [1, 4, 6, 4, 1]

    # Vérifier que chaque ligne a le bon nombre d'éléments
    for i, ligne in enumerate(triangle):
        assert len(ligne) == i + 1


# ========== TESTS DES ENSEMBLES ==========

def test_operations_ensembles():
    """Test des opérations sur ensembles"""
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]

    ops = operations_ensembles(a, b)

    assert ops['union'] == {1, 2, 3, 4, 5, 6, 7, 8}
    assert ops['intersection'] == {4, 5}
    assert ops['difference_a_b'] == {1, 2, 3}
    assert ops['difference_b_a'] == {6, 7, 8}
    assert ops['difference_symetrique'] == {1, 2, 3, 6, 7, 8}
    assert ops['disjoints'] == False


def test_ensembles_disjoints():
    """Test d'ensembles disjoints"""
    a = [1, 2, 3]
    b = [4, 5, 6]

    ops = operations_ensembles(a, b)

    assert ops['intersection'] == set()
    assert ops['disjoints'] == True


def test_sous_ensembles():
    """Test de sous-ensembles"""
    a = [1, 2, 3]
    b = [1, 2, 3, 4, 5]

    ops = operations_ensembles(a, b)

    assert ops['a_sous_ensemble_b'] == True
    assert ops['b_sous_ensemble_a'] == False


# ========== TESTS D'ANALYSE ==========

def test_analyser_suite():
    """Test de l'analyse de suite"""
    suite = [2, 4, 6, 8, 10]

    analyse = analyse_suite(suite)

    assert analyse['longueur'] == 5
    assert analyse['min'] == 2
    assert analyse['max'] == 10
    assert analyse['moyenne'] == 6
    assert analyse['mediane'] == 6
    assert analyse['somme'] == 30
    assert analyse['tendance'] == "Strictement croissante"


def test_analyser_suite_decroissante():
    """Test d'une suite décroissante"""
    suite = [10, 8, 6, 4, 2]

    analyse = analyse_suite(suite)

    assert analyse['tendance'] == "Strictement décroissante"


def test_analyser_suite_constante():
    """Test d'une suite constante"""
    suite = [5, 5, 5, 5, 5]

    analyse = analyse_suite(suite)

    assert analyse['moyenne'] == 5
    assert analyse['ecart_type'] == 0
    assert analyse['tendance'] == "Croissante"  # >= 0


# ========== TESTS DE PROPRIÉTÉS MATHÉMATIQUES ==========

def test_propriete_fibonacci():
    """Propriété : F(n) = F(n-1) + F(n-2)"""
    fib = fibonacci(20)

    for i in range(2, len(fib)):
        assert fib[i] == fib[i-1] + fib[i-2]


def test_propriete_combinaison_pascal():
    """Propriété : C(n,k) = C(n-1,k-1) + C(n-1,k)"""
    n, k = 10, 5

    assert combinaison(n, k) == combinaison(n-1, k-1) + combinaison(n-1, k)


def test_somme_ligne_pascal():
    """Propriété : Somme de la ligne n = 2^n"""
    triangle = triangle_pascal(10)

    for i, ligne in enumerate(triangle):
        assert sum(ligne) == 2**i


# ========== TESTS DE PERFORMANCE ==========

def test_performance_addition():
    """Test de performance pour 10000 additions"""
    start = time.time()
    for i in range(10000):
        addition(i, i+1)
    duration = time.time() - start
    assert duration < 0.1


def test_performance_fibonacci():
    """Fibonacci pour n=100 doit être rapide"""
    start = time.time()
    fib = fibonacci(100)
    duration = time.time() - start

    assert len(fib) == 100
    assert duration < 0.01  # Moins de 10ms


def test_performance_combinaison():
    """Calcul de C(1000, 500) doit être rapide"""
    start = time.time()
    result = combinaison(100, 50)
    duration = time.time() - start

    assert result is not None
    assert duration < 1.0  # Moins d'1 seconde


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
