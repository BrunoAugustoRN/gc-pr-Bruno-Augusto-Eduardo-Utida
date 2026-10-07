def subtrair(a, b):
    return a - b  # Corrigido: era b - a


def media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)  # Corrigido: era dividido por 2