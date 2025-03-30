import math as math
import pandas as pd
import matplotlib.pyplot as plt


def getResult(k):
    return math.cos(0.05 * math.sqrt((k/m) - c**2/(4*m**2))) + c/(math.sqrt(4*k * m - c**2)) * math.sin(0.05 * math.sqrt(k/m - c**2/(4*m**2)))

def getGraph():
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(listK)), listResult, marker='o', linestyle='-', label='Resultado da equação')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8, label='Equilíbrio')
    plt.xlabel('Iteração')
    plt.ylabel('Resultado')
    plt.title('Convergência do Método da Bisseção')
    plt.legend()
    plt.grid()
    return plt

def getGraphEvoK():
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(listK)), listK, marker='o', linestyle='-', color='red', label='Valor de K')

    plt.xlabel('Iteração')
    plt.ylabel('Valor de K')
    plt.title('Evolução do Valor de K no Método da Bisseção')
    plt.grid()
    plt.legend()
    return plt

m = 1.2 * (10**6)
c = 1 * (10**7)
k1 = 1 * 10**9 
k2 = 2 * 10**9

listK1 = []
listK2 = []
listK = []
listResult = []

for i in range (0, 13):
    k = (k1 + k2)/2
    result = getResult(k)
    listK1.append(k1)
    listK2.append(k2)
    listK.append(k)
    listResult.append(result)

    if result < 0:
        k2 = k
    elif result > 0:
        k1 = k
    else:
        print("Resultado encontrado!")
        break

dataFrame = pd.DataFrame({'K1': listK1, 'K2': listK2, 'K': listK, 'Resultado': listResult})