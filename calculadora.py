"""Operações básicas com números."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def multiplicar(a, b):
    return a * b
