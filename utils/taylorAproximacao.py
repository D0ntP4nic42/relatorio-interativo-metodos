import pandas as pd
import math

def fatorial(n):
    return 1 if n == 0 else math.prod(range(1, n + 1))

def calcular_taylor(x, h, max_m=5):
    resultados = []

    for m in range(1, max_m + 1):
        valor_real = x ** m
        valor_aproximado = (x - h) ** m + m * (x - h) ** (m - 1) * h
        resto = 0

        # Calculando o termo de erro (segunda derivada simplificada)
        derivada_2 = m * (m - 1) * (x - h) ** (m - 2) if m >= 2 else 0
        termo_erro = (derivada_2 / fatorial(2)) * h ** 2 if m >= 2 else 0
        resto += termo_erro

        resultados.append({
            "m": m,
            "Valor real": valor_real,
            "Valor aproximado (1ª ordem)": valor_aproximado,
            "Termo de erro (2ª ordem)": termo_erro,
            "Erro total": abs(valor_real - (valor_aproximado + termo_erro))
        })

    return pd.DataFrame(resultados)