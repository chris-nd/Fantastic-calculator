"""
Tests unitaires pour la calculatrice
"""

import time
import math
import pytest
from calculatrice import (
    addition, soustraction, multiplication, division,
    puissance, racine_carree, sinus, cosinus, tangente,
    degres_vers_radians
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


# ========== TEST DE PERFORMANCE (bonus) ==========

def test_performance_addition():
    """Test de performance pour 10000 additions"""
    start = time.time()
    for i in range(10000):
        addition(i, i+1)
    duration = time.time() - start
    assert duration < 0.1
