from app.calculadora import *

def test_somar():
    resultado = somar(2,3)

    assert resultado == 5

def test_subtrair():
    resultado = subtrair(10,3)

    assert resultado == 7

def test_multiplicar():
    resultado = multiplicar(10,3)

    assert resultado == 30