import math
import pandas as pd
import matplotlib.pyplot as plt

m = 1.2 * (10**6)
c = 1 * (10**7)
k_final = 1.5380859375e9 

fatorDeAmortecimento = c / (2 * math.sqrt(k_final * m))

def getResultOmegaP(omegaP):
    return 2 * math.sqrt((1 - omegaP**2)**2 + 4 * (fatorDeAmortecimento**2) * (omegaP**2)) - 1

omegaP1 = 0
omegaP2 = 1

listOmegaP1 = []
listOmegaP2 = []
listOmegaP = []
listResultOmegaP = []

for i in range(0, 20):
    omegaP = (omegaP1 + omegaP2) / 2
    result = getResultOmegaP(omegaP)

    listOmegaP1.append(omegaP1)
    listOmegaP2.append(omegaP2)
    listOmegaP.append(omegaP)
    listResultOmegaP.append(result)

    if abs(result) < 1e-6:
        break

    if result < 0:
        omegaP2 = omegaP
    else:
        omegaP1 = omegaP

dataFrame = pd.DataFrame({
    'Omega/P1': listOmegaP1,
    'Omega/P2': listOmegaP2,
    'Omega/P': listOmegaP,
    'Resultado': listResultOmegaP
})

def getGraph():
    import numpy as np

    omega_range = np.linspace(0, 1, 500)
    values = [getResultOmegaP(w) for w in omega_range]

    plt.figure(figsize=(8, 5))
    plt.plot(omega_range, values, label='f(ωp)')
    plt.axhline(0, color='black', linestyle='--', label='Equilíbrio')
    plt.axvline(listOmegaP[-1], color='red', linestyle='--', label=f'ωp ≈ {listOmegaP[-1]:.4f}')
    plt.xlabel("ωp")
    plt.ylabel("f(ωp)")
    plt.title("Análise em Estradas Rugosas")
    plt.grid()
    plt.legend()
    return plt

def getGraphEvoK():
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(listOmegaP)), listOmegaP, marker='o', linestyle='-', color='green', label='Valor de ωp')
    plt.xlabel("Iteração")
    plt.ylabel("ωp")
    plt.title("Evolução de ωp no Método da Bisseção")
    plt.grid()
    plt.legend()
    return plt


